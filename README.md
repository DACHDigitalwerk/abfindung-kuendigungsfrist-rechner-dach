# Abfindungs-, Kündigungsfrist- & Urlaubsabgeltungs-Rechner DACH (DE / CH / AT) 🇩🇪 🇨🇭 🇦🇹

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![DACH Arbeitsrecht](https://img.shields.io/badge/Rechtsgrundlagen-§_1a_KSchG_|_§_622_BGB_|_Art._335c_OR_|_§_20_AngG-emerald.svg)](https://dach-digitalwerk.netlify.app/abfindung-kuendigung/)
[![Live Web-App](https://img.shields.io/badge/Web_App-100%25_Kostenlos_&_Lokal_im_Browser-indigo.svg)](https://dach-digitalwerk.netlify.app/abfindung-kuendigung/)
[![Steuerrecht](https://img.shields.io/badge/Steuer-§_34_EStG_Fünftelregelung_&_SV--frei-amber.svg)](https://dach-digitalwerk.netlify.app/abfindung-kuendigung/)

> ⚖️ **Open-Source Berechnungs-Engine & Referenz-Dokumentation für Abfindung, gesetzliche Kündigungsfristen, Sperrzeit-Risiko und Urlaubsabgeltung im DACH-Raum (Deutschland, Schweiz, Österreich).**  
> Entwickelt für Arbeitnehmer, Personalabteilungen (HR), Betriebsräte und Legal-Tech-Anwendungen – 100 % lokal ausführbar ohne Cloud-Datenweitergabe.

---

### 🌐 Interaktiver Online-Rechner (Sofort im Browser nutzen)

**Berechnen Sie Abfindungshöhe, Netto-Steuervorteil (Fünftelregelung), exaktes Austrittsdatum und Urlaubsabgeltung direkt im Browser:**  
👉 **[https://dach-digitalwerk.netlify.app/abfindung-kuendigung/](https://dach-digitalwerk.netlify.app/abfindung-kuendigung/)**

*(Ergänzend: Prüfen Sie Ihr Arbeitszeugnis direkt im Anschluss mit dem kostenlosen **[DACH Arbeitszeugnis-Geheimcode-Decoder](https://dach-digitalwerk.netlify.app/arbeitszeugnis/)**)*

---

## Inhaltsverzeichnis
1. [Abfindungsberechnung nach § 1a KSchG (Deutschland), OR (Schweiz) & AngG (Österreich)](#1-abfindungsberechnung-nach--1a-kschg-deutschland-or-schweiz--angg-österreich)
2. [Gesetzliche Kündigungsfristen: § 622 BGB, Art. 335c OR & § 20 AngG](#2-gesetzliche-kündigungsfristen--622-bgb-art-335c-or--20-angg)
3. [Urlaubsabgeltung & Resturlaub auszahlen (§ 7 Abs. 4 BUrlG / Art. 329d OR)](#3-urlaubsabgeltung--resturlaub-auszahlen--7-abs-4-burlg--art-329d-or)
4. [Versteuerung der Abfindung (§ 34 EStG Fünftelregelung & SV-Freiheit)](#4-versteuerung-der-abfindung--34-estg-fünftelregelung--sv-freiheit)
5. [Sperrzeit beim Arbeitslosengeld (§ 159 SGB III / Art. 30 AVIG)](#5-sperrzeit-beim-arbeitslosengeld--159-sgb-iii--art-30-avig)
6. [CLI- & Code-Nutzung (Python & Node.js)](#6-cli---code-nutzung-python--nodejs)
7. [Lizenz & Weiterführende Tools](#7-lizenz--weiterführende-tools)

---

## 1. Abfindungsberechnung nach § 1a KSchG (Deutschland), OR (Schweiz) & AngG (Österreich)

### 🇩🇪 Deutschland: Regelabfindung nach § 1a Kündigungsschutzgesetz (KSchG)

Gemäß **[§ 1a Abs. 2 KSchG](https://www.gesetze-im-internet.de/kschg/__1a.html)** beträgt die gesetzliche Regelabfindung bei betriebsbedingter Kündigung **0,5 Monatsverdienste für jedes Jahr des Bestehens des Arbeitsverhältnisses**:

$$\text{Abfindung}_{\text{Brutto}} = \text{Bruttomonatsgehalt} \times \text{Betriebszugehörigkeit (gerundet)} \times \text{Faktor } F$$

* **Gesetzliche Rundungsregel (§ 1a Abs. 2 Satz 2 KSchG):**  
  Bei der Ermittlung der Dauer des Arbeitsverhältnisses ist ein Zeitraum von **mehr als sechs Monaten (> 6 Monate) auf ein volles Jahr aufzurunden** (Beispiel: 5 Jahre und 7 Monate $\rightarrow$ **6,0 Jahre**).
* **Maßgeblicher Monatsverdienst (§ 10 Abs. 3 KSchG):**  
  Als Monatsverdienst gilt, was dem Arbeitnehmer bei der für ihn maßgebenden regelmäßigen Arbeitszeit in dem Monat, in dem das Arbeitsverhältnis endet, an **Geld- und Sachbezügen** zusteht (inkl. anteiligem 13. Monatsgehalt, Weihnachtsgeld, Urlaubsgeld, Provisionen und geldwertem Vorteil eines Dienstwagens).

#### Typische Abfindungsfaktoren $F$ in der Praxis:

| Faktor $F$ | Anwendungsfall / Verhandlungsposition |
| :--- | :--- |
| **$F = 0,25 \text{ – } 0,40$** | Kleinbetrieb ($\le 10$ Vollzeit-Mitarbeiter ohne KSchG-Schutz) oder starkes Arbeitgeber-Beweismaterial |
| **$F = 0,50$ (Regelwert)** | Gesetzlicher Standard nach **§ 1a KSchG** sowie gerichtlicher Vergleichsmaßstab der Arbeitsgerichte |
| **$F = 0,75 \text{ – } 1,00$** | Hohes Prozessrisiko für den Arbeitgeber (fehlerhafte Sozialauswahl nach § 1 Abs. 3 KSchG, fehlende Betriebsratsanhörung nach § 102 BetrVG) |
| **$F = 1,00 \text{ – } 1,50+$** | Besonderer Kündigungsschutz (Schwerbehinderung, Elternzeit, Datenschutzbeauftragter, Betriebsrat) oder Aufhebungsvertrag auf dringenden Arbeitgeberwunsch (Turbo-/Sprinterklausel) |

---

### 🇨🇭 Schweiz: Abgangsentschädigung (Art. 339b OR) & Freistellungs-Vergleich

Im Schweizer Obligationenrecht gilt grundsätzlich Kündigungsfreiheit (Art. 335 OR). Eine Entschädigung entsteht in drei Konstellationen:
1. **Gesetzliche Abgangsentschädigung ([Art. 339b–339d OR](https://www.fedlex.admin.ch/eli/cc/27/317_321_377/de#art_339_b)):**  
   Endet das Arbeitsverhältnis eines mindestens **50-jährigen Arbeitnehmers nach 20 oder mehr Dienstjahren**, schuldet der Arbeitgeber **2 bis 8 Monatslöhne** (sofern keine gleichwertige Pensionskassenleistung nach BVG anrechenbar ist, Art. 339d OR).
2. **Missbräuchliche Kündigung ([Art. 336a OR](https://www.fedlex.admin.ch/eli/cc/27/317_321_377/de#art_336_a)):**  
   Strafentschädigung von bis zu **6 Monatslöhnen** (Einsprache vor Ablauf der Kündigungsfrist nach Art. 336b OR zwingend erforderlich!).
3. **Freiwillige Abgangsentschädigung / Sozialplan:**  
   In Schweizer Aufhebungsvereinbarungen üblicherweise **0,5 bis 1,0 Monatslöhne pro Dienstjahr** zuzüglich bezahlter Freistellung.

---

### 🇦🇹 Österreich: Abfertigung Neu (BMSVG) vs. Abfertigung Alt (§ 23 AngG)

* **Abfertigung Neu (Eintritt ab 01.01.2003 – BMSVG):**  
  Der Arbeitgeber zahlt monatlich **1,53 % des Bruttoentgelts** (inkl. Sonderzahlungen) in eine Betriebliche Vorsorgekasse (BV-Kasse). Bei Arbeitgeberkündigung, einvernehmlicher Auflösung oder berechtigtem Austritt nach mindestens 36 Beitragsmonaten besteht Anspruch auf Auszahlung.
* **Abfertigung Alt (§ 23 AngG – Eintritt vor 01.01.2003):**  
  Gestaffelt nach Dienstjahren von **2 Monatsentgelten** (ab 3 Jahren) bis zu **12 Monatsentgelten** (ab 25 Dienstjahren), steuerbegünstigt mit **6 % festem Lohnsteuersatz** (§ 67 Abs. 3 EStG AT).

---

## 2. Gesetzliche Kündigungsfristen: § 622 BGB, Art. 335c OR & § 20 AngG

### 🇩🇪 Deutschland: § 622 BGB (Staffelung nach Betriebszugehörigkeit)

Nach **[§ 622 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__622.html)** beträgt die Grundkündigungsfrist für Arbeitnehmer und Arbeitgeber **4 Wochen zum 15. oder zum Ende eines Kalendermonats** (in der Probezeit bis max. 6 Monate: **2 Wochen zu jedem Tag**, § 622 Abs. 3 BGB).

Für eine **Kündigung durch den Arbeitgeber** verlängert sich die Frist gemäß **§ 622 Abs. 2 BGB** zwingend wie folgt:

| Betriebszugehörigkeit | Gesetzliche Kündigungsfrist (Arbeitgeber) | Endtermin | Rechtsgrundlage |
| :--- | :--- | :--- | :--- |
| **In der Probezeit** (max. 6 Monate) | **2 Wochen** (14 Kalendertage) | Zu jedem beliebigen Tag | § 622 Abs. 3 BGB |
| **Unter 2 Jahren** | **4 Wochen** (28 Kalendertage) | Zum 15. oder Monatsende | § 622 Abs. 1 BGB |
| **Ab 2 Jahren** | **1 Monat** | Zum Ende eines Kalendermonats | § 622 Abs. 2 Nr. 1 BGB |
| **Ab 5 Jahren** | **2 Monate** | Zum Ende eines Kalendermonats | § 622 Abs. 2 Nr. 2 BGB |
| **Ab 8 Jahren** | **3 Monate** | Zum Ende eines Kalendermonats | § 622 Abs. 2 Nr. 3 BGB |
| **Ab 10 Jahren** | **4 Monate** | Zum Ende eines Kalendermonats | § 622 Abs. 2 Nr. 4 BGB |
| **Ab 12 Jahren** | **5 Monate** | Zum Ende eines Kalendermonats | § 622 Abs. 2 Nr. 5 BGB |
| **Ab 15 Jahren** | **6 Monate** | Zum Ende eines Kalendermonats | § 622 Abs. 2 Nr. 6 BGB |
| **Ab 20 Jahren** | **7 Monate** | Zum Ende eines Kalendermonats | § 622 Abs. 2 Nr. 7 BGB |

---

### 🇨🇭 Schweiz: Art. 335b & Art. 335c Obligationenrecht (OR)

Sofern durch Einzelarbeitsvertrag oder Gesamtarbeitsvertrag (GAV) nichts anderes vereinbart wurde (Mindestfrist 1 Monat nach Art. 335c Abs. 2 OR), gelten nach **[Art. 335c Abs. 1 OR](https://www.fedlex.admin.ch/eli/cc/27/317_321_377/de#art_335_c)** folgende Fristen:

| Dienstjahr | Gesetzliche Kündigungsfrist (CH) | Kündigungstermin | Rechtsgrundlage |
| :--- | :--- | :--- | :--- |
| **Probezeit** (1–3 Monate) | **7 Kalendertage** | Auf jeden beliebigen Tag | Art. 335b Abs. 1 OR |
| **Im 1. Dienstjahr** | **1 Monat** | Auf das Ende eines Monats | Art. 335c Abs. 1 OR |
| **Im 2. bis und mit 9. Dienstjahr** | **2 Monate** | Auf das Ende eines Monats | Art. 335c Abs. 1 OR |
| **Ab dem 10. Dienstjahr** | **3 Monate** | Auf das Ende eines Monats | Art. 335c Abs. 1 OR |

> ⚠️ **Wichtig – Unterbruch durch Krankheit/Unfall (Art. 336c Abs. 2 OR):**  
> Erkrankt der Arbeitnehmer während der laufenden Kündigungsfrist nach Arbeitgeberkündigung, steht die Frist während der Sperrfrist still (30 Tage im 1. Dienstjahr, 90 Tage im 2.–5. Dienstjahr, 180 Tage ab dem 6. Dienstjahr) und verlängert sich anschließend bis zum nächsten Monatsende (Art. 336c Abs. 3 OR).

---

### 🇦🇹 Österreich: § 20 AngG & § 1159 ABGB (Angleichung Arbeiter & Angestellte)

Für Arbeitgeberkündigungen gilt in Österreich (sowohl für Angestellte nach § 20 Abs. 2 AngG als auch für Arbeiter nach § 1159 ABGB) zum Quartalsende (bzw. bei Vereinbarung zum 15. oder Monatsletzten):
* **1. bis 2. Dienstjahr:** 6 Wochen
* **Ab dem vollendeten 2. Dienstjahr:** 2 Monate
* **Ab dem vollendeten 5. Dienstjahr:** 3 Monate
* **Ab dem vollendeten 15. Dienstjahr:** 4 Monate
* **Ab dem vollendeten 25. Dienstjahr:** 5 Monate

---

## 3. Urlaubsabgeltung & Resturlaub auszahlen (§ 7 Abs. 4 BUrlG / Art. 329d OR)

Kann der Resturlaub wegen der Beendigung des Arbeitsverhältnisses ganz oder teilweise nicht mehr in Natur gewährt werden, ist er zwingend in Geld abzugelten (**§ 7 Abs. 4 Bundesurlaubsgesetz – BUrlG**):

### 🇩🇪 Berechnungsformel nach BAG-Rechtsprechung (Deutschland)
Die Berechnung basiert auf dem Durchschnittsverdienst der letzten 13 Wochen (1 Quartal = 3 Monate) vor Beendigung des Arbeitsverhältnisses (§ 11 Abs. 1 BUrlG):

$$\text{Urlaubsabgeltung}_{\text{Brutto}} = \frac{\text{Bruttomonatsgehalt} \times 3}{13 \times \text{Arbeitstage pro Woche}} \times \text{Offene Resturlaubstage}$$

*(Bei einer klassischen 5-Tage-Woche entspricht der Teiler $13 \times 5 = 65$ Arbeitstagen im Quartal; ein einzelner Urlaubstag ist damit exakt $\frac{3}{65} \approx 4,615\,\%$ eines Bruttomonatsgehalts wert).*

### 🇨🇭 Berechnungsformel Schweiz (Art. 329d OR)
In der Schweiz gilt ein striktes **Abgeltungsverbot während des laufenden Arbeitsverhältnisses** (Art. 329d Abs. 2 OR). Bei Beendigung und Unzumutbarkeit des Ferienbezugs berechnet sich der Tageswert über durchschnittlich **21,75 Arbeitstage pro Monat** (bei 5-Tage-Woche):

$$\text{Ferienentschädigung}_{\text{CHF}} = \frac{\text{Bruttomonatslohn (inkl. 13. Monatslohn-Anteil)}}{21,75} \times \text{Offene Ferientage}$$

---

## 4. Versteuerung der Abfindung (§ 34 EStG Fünftelregelung & SV-Freiheit)

1. **100 % Sozialversicherungsfrei in Deutschland (§ 14 SGB IV):**  
   Eine echte Abfindung, die als Entschädigung für den Verlust des Arbeitsplatzes gezahlt wird (BSG-Rechtsprechung), unterliegt **nicht** der Sozialversicherungspflicht. Es fallen **0,00 € Abzüge** für Kranken-, Pflege-, Renten- und Arbeitslosenversicherung an!
2. **Steuerbegünstigung durch die Fünftelregelung (§ 34 Abs. 1 EStG):**  
   Fließt die Abfindung zusammengeballt in einem einzigen Kalenderjahr zu (*Zusammenballung von Einkünften*), wird die Progression durch die **Fünftelregelung** gemildert:
   $$\Delta ESt_{\text{Abfindung}} = 5 \times \left[ ESt\left(\text{zvE}_{\text{ohne}} + \frac{\text{Abfindung}}{5}\right) - ESt\left(\text{zvE}_{\text{ohne}}\right) \right]$$
   > **Hinweis ab 2025/2026 (Wachstumschancengesetz):** Der Arbeitgeber wendet die Fünftelregelung nicht mehr automatisch im monatlichen Lohnsteuerabzug an – Arbeitnehmer holen sich die volle Steuerersparnis über die **Einkommensteuererklärung (Anlage N)** vom Finanzamt zurück!

---

## 5. Sperrzeit beim Arbeitslosengeld (§ 159 SGB III / Art. 30 AVIG)

* **🇩🇪 Deutschland (§ 159 Abs. 1 Satz 2 Nr. 1 SGB III):**  
  Unterzeichnet ein Arbeitnehmer ohne *wichtigen Grund* einen **Aufhebungsvertrag**, verhängt die Agentur für Arbeit regelmäßig eine **Sperrzeit von 12 Wochen** (und kürzt die Gesamtbezugsdauer des ALG I um ein Viertel, § 148 Abs. 1 Nr. 4 SGB III).  
  **Ausnahme (Kein Sperrzeit-Eintritt):**
  1. Arbeitgeberseitige betriebs- oder personenbedingte Kündigung mit Abfindungsangebot nach **§ 1a KSchG**, *oder*
  2. Aufhebungsvertrag zur Vermeidung einer konkret angedrohten, rechtmäßigen betriebs-/personenbedingten Arbeitgeberkündigung unter Einhaltung der ordentlichen Kündigungsfrist und einer Abfindung im Korridor der fachlichen Weisungen der BA.
* **🇨🇭 Schweiz (Art. 30 Abs. 1 lit. a AVIG):**  
  Bei selbstverschuldeter Arbeitslosigkeit (Eigenkündigung ohne Zusicherung einer neuen Stelle oder Aufhebungsvertrag auf eigenen Wunsch) drohen **31 bis 60 Einstelltage** bei der Arbeitslosenkasse (RAV).

---

## 6. CLI- & Code-Nutzung (Python & Node.js)

Dieses Repository enthält zwei produktionsreife, abhängigkeitsfreie Berechnungs-Module (`abfindung_rechner.py` und `abfindung_rechner.js`).

### Python 3 CLI ausführen:
```bash
python abfindung_rechner.py --country DE --salary 5200 --years 6.7 --factor 0.5 --vacation-days 12
```

### Node.js CLI ausführen:
```bash
node abfindung_rechner.js DE 5200 6.7 0.5 12
```

### Als JavaScript-Modul einbinden:
```javascript
const { calculateTerminationPackage } = require('./abfindung_rechner.js');

const result = calculateTerminationPackage({
  country: 'DE',
  monthlyGross: 5200,
  tenureYears: 6.7,      // 6 Jahre & 8 Monate -> wird nach § 1a Abs. 2 KSchG auf 7 Jahre aufgerundet
  factor: 0.5,
  remainingVacationDays: 12,
  workdaysPerWeek: 5
});

console.log(result);
```

---

## 7. Lizenz & Weiterführende Tools

* 🌐 **Live-Rechner (Abfindung, Kündigungsfrist & Resturlaub):**  
  [https://dach-digitalwerk.netlify.app/abfindung-kuendigung/](https://dach-digitalwerk.netlify.app/abfindung-kuendigung/)
* 🔍 **Live-Decoder (Arbeitszeugnis & Geheimcodes prüfen):**  
  [https://dach-digitalwerk.netlify.app/arbeitszeugnis/](https://dach-digitalwerk.netlify.app/arbeitszeugnis/)
* 🧾 **Schweizer QR-Rechnung & XRechnung 3.0 Generator:**  
  [https://dach-digitalwerk.netlify.app/qr-suite/](https://dach-digitalwerk.netlify.app/qr-suite/)

Veröffentlicht unter der **MIT License** – Copyright © 2026 [DACH Digitalwerk](https://dach-digitalwerk.netlify.app).
