#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DACH Abfindungs-, Kündigungsfrist- & Urlaubsabgeltungs-Rechner (DE / CH / AT)
Rechtsgrundlagen: § 1a KSchG, § 622 BGB, § 7 Abs. 4 BUrlG, Art. 335c OR, § 20 AngG
Web-App: https://dach-digitalwerk.netlify.app/abfindung-kuendigung/
Copyright (c) 2026 DACH Digitalwerk (MIT License)
"""

import argparse
import json
import math


def round_kschg_years(tenure_years: float) -> int:
    """
    Gemäß § 1a Abs. 2 Satz 2 KSchG ist ein Zeitraum von mehr als 6 Monaten (> 0.5 Jahre)
    auf ein volles Jahr aufzurunden.
    """
    full_years = int(math.floor(tenure_years))
    fraction = tenure_years - full_years
    if fraction > 0.5:
        return full_years + 1
    return max(0, full_years)


def get_notice_period(country: str, tenure_years: float, in_probation: bool = False) -> dict:
    country = country.upper()
    if country == "DE":
        if in_probation and tenure_years <= 0.5:
            return {
                "law": "§ 622 Abs. 3 BGB",
                "employerNotice": "2 Wochen (14 Kalendertage)",
                "employeeNotice": "2 Wochen (14 Kalendertage)",
                "terminationTerm": "Zu jedem beliebigen Tag",
            }
        tiers = [
            (20, "7 Monate", "§ 622 Abs. 2 Nr. 7 BGB"),
            (15, "6 Monate", "§ 622 Abs. 2 Nr. 6 BGB"),
            (12, "5 Monate", "§ 622 Abs. 2 Nr. 5 BGB"),
            (10, "4 Monate", "§ 622 Abs. 2 Nr. 4 BGB"),
            (8, "3 Monate", "§ 622 Abs. 2 Nr. 3 BGB"),
            (5, "2 Monate", "§ 622 Abs. 2 Nr. 2 BGB"),
            (2, "1 Monat", "§ 622 Abs. 2 Nr. 1 BGB"),
        ]
        for min_years, period, law in tiers:
            if tenure_years >= min_years:
                return {
                    "law": law,
                    "employerNotice": period,
                    "employeeNotice": "4 Wochen zum 15. oder Monatsende (§ 622 Abs. 1 BGB, sofern nicht vertraglich gleichgestellt)",
                    "terminationTerm": "Zum Ende eines Kalendermonats",
                }
        return {
            "law": "§ 622 Abs. 1 BGB",
            "employerNotice": "4 Wochen (28 Kalendertage)",
            "employeeNotice": "4 Wochen (28 Kalendertage)",
            "terminationTerm": "Zum 15. oder zum Ende eines Kalendermonats",
        }

    if country == "CH":
        if in_probation and tenure_years <= 0.25:
            return {
                "law": "Art. 335b Abs. 1 OR",
                "employerNotice": "7 Kalendertage",
                "employeeNotice": "7 Kalendertage",
                "terminationTerm": "Auf jeden beliebigen Tag",
            }
        if tenure_years < 1.0:
            period = "1 Monat"
        elif tenure_years < 9.0:
            period = "2 Monate"
        else:
            period = "3 Monate"
        return {
            "law": "Art. 335c Abs. 1 OR",
            "employerNotice": period,
            "employeeNotice": period,
            "terminationTerm": "Auf das Ende eines Monats",
        }

    # AT (§ 20 AngG / § 1159 ABGB)
    if tenure_years >= 25:
        period = "5 Monate"
    elif tenure_years >= 15:
        period = "4 Monate"
    elif tenure_years >= 5:
        period = "3 Monate"
    elif tenure_years >= 2:
        period = "2 Monate"
    else:
        period = "6 Wochen"
    return {
        "law": "§ 20 Abs. 2 AngG / § 1159 ABGB",
        "employerNotice": period,
        "employeeNotice": "1 Monat zum Monatsletzten (§ 20 Abs. 4 AngG)",
        "terminationTerm": "Zum Quartalsende (bzw. bei Vereinbarung zum 15. oder Monatsletzten)",
    }


def calculate_vacation_payout(
    country: str, monthly_gross: float, remaining_days: float, workdays_per_week: int = 5
) -> dict:
    country = country.upper()
    if country == "CH":
        daily_rate = monthly_gross / 21.75
        law = "Art. 329d Abs. 2 OR (Teiler 21,75 Arbeitstage/Monat)"
    else:
        # DE (§ 7 Abs. 4 i.V.m. § 11 BUrlG) & AT: (Monatsgehalt * 3) / (13 * Arbeitstage/Woche)
        daily_rate = (monthly_gross * 3.0) / (13.0 * max(1, workdays_per_week))
        law = "§ 7 Abs. 4 i.V.m. § 11 Abs. 1 BUrlG (13-Wochen-Referenz)"

    gross_payout = round(daily_rate * max(0.0, remaining_days), 2)
    return {
        "law": law,
        "dailyValue": round(daily_rate, 2),
        "remainingDays": remaining_days,
        "grossVacationPayout": gross_payout,
    }


def calculate_termination_package(
    country: str = "DE",
    monthly_gross: float = 4500.0,
    tenure_years: float = 5.6,
    factor: float = 0.5,
    remaining_vacation_days: float = 10.0,
    workdays_per_week: int = 5,
    in_probation: bool = False,
) -> dict:
    country = country.upper()
    currency = "CHF" if country == "CH" else "EUR"

    rounded_years = round_kschg_years(tenure_years) if country == "DE" else tenure_years
    severance_gross = round(monthly_gross * rounded_years * factor, 2)

    notice = get_notice_period(country, tenure_years, in_probation)
    vacation = calculate_vacation_payout(country, monthly_gross, remaining_vacation_days, workdays_per_week)

    # Approximate Fünftelregelung (§ 34 EStG) net retention for DE
    approx_tax_rate_regular = 0.34 if country != "CH" else 0.18
    approx_tax_rate_fuenftel = 0.24 if country != "CH" else 0.14
    estimated_tax_saving = round(severance_gross * (approx_tax_rate_regular - approx_tax_rate_fuenftel), 2)
    estimated_net_severance = round(severance_gross * (1.0 - approx_tax_rate_fuenftel), 2)

    return {
        "country": country,
        "currency": currency,
        "inputs": {
            "monthlyGross": monthly_gross,
            "tenureYears": tenure_years,
            "effectiveYearsForSeverance": rounded_years,
            "factor": factor,
            "remainingVacationDays": remaining_vacation_days,
        },
        "severance": {
            "law": "§ 1a Abs. 2 KSchG" if country == "DE" else ("Art. 339b OR / Sozialplan" if country == "CH" else "§ 23 AngG / BMSVG"),
            "grossSeverance": severance_gross,
            "estimatedNetSeverance": estimated_net_severance,
            "estimatedFuenftelTaxSaving": estimated_tax_saving,
            "socialSecurityContribution": 0.0,
        },
        "noticePeriod": notice,
        "vacationPayout": vacation,
        "totalGrossPackage": round(severance_gross + vacation["grossVacationPayout"], 2),
        "liveWebTool": "https://dach-digitalwerk.netlify.app/abfindung-kuendigung/",
    }


def main():
    parser = argparse.ArgumentParser(description="DACH Abfindungs- & Kündigungsfrist-Rechner CLI")
    parser.add_argument("--country", choices=["DE", "CH", "AT"], default="DE")
    parser.add_argument("--salary", type=float, default=4800.0, help="Bruttomonatsgehalt (EUR/CHF)")
    parser.add_argument("--years", type=float, default=5.6, help="Betriebszugehörigkeit in Jahren")
    parser.add_argument("--factor", type=float, default=0.5, help="Abfindungsfaktor (Standard 0.5 nach § 1a KSchG)")
    parser.add_argument("--vacation-days", type=float, default=10.0, help="Offene Resturlaubstage")
    parser.add_argument("--json", action="store_true", help="JSON-Ausgabe")
    args = parser.parse_args()

    res = calculate_termination_package(
        country=args.country,
        monthly_gross=args.salary,
        tenure_years=args.years,
        factor=args.factor,
        remaining_vacation_days=args.vacation_days,
    )

    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return

    cur = res["currency"]
    print("=" * 68)
    print(f" ⚖️ DACH ABFINDUNGS- & KÜNDIGUNGSFRIST-RECHNER ({res['country']})")
    print("=" * 68)
    print(f"Bruttomonatsgehalt       : {res['inputs']['monthlyGross']:.2f} {cur}")
    print(f"Betriebszugehörigkeit    : {res['inputs']['tenureYears']} Jahre (angerechnet: {res['inputs']['effectiveYearsForSeverance']} J.)")
    print(f"Abfindung (Brutto)       : {res['severance']['grossSeverance']:.2f} {cur} ({res['severance']['law']})")
    print(f"Geschätzte Abfindung Net.: {res['severance']['estimatedNetSeverance']:.2f} {cur} (SV-Abzüge: 0.00 {cur})")
    print(f"Urlaubsabgeltung (Brutto): {res['vacationPayout']['grossVacationPayout']:.2f} {cur} ({res['vacationPayout']['remainingDays']} Tage)")
    print(f"Gesamtpaket (Brutto)     : {res['totalGrossPackage']:.2f} {cur}")
    print("-" * 68)
    print(f"Gesetzl. Kündigungsfrist : {res['noticePeriod']['employerNotice']} ({res['noticePeriod']['law']})")
    print(f"Endtermin                : {res['noticePeriod']['terminationTerm']}")
    print("-" * 68)
    print(f"🌐 Interaktiver Rechner  : {res['liveWebTool']}")


if __name__ == "__main__":
    main()
