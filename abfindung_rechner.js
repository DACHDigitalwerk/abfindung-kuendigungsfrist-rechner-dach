/**
 * DACH Abfindungs-, Kündigungsfrist- & Urlaubsabgeltungs-Rechner (DE / CH / AT)
 * Rechtsgrundlagen: § 1a KSchG, § 622 BGB, § 7 Abs. 4 BUrlG, Art. 335c OR, § 20 AngG
 * Live Web-App: https://dach-digitalwerk.netlify.app/abfindung-kuendigung/
 * Copyright (c) 2026 DACH Digitalwerk (MIT License)
 */

function roundKschgYears(tenureYears) {
  const full = Math.floor(tenureYears);
  const fraction = tenureYears - full;
  return fraction > 0.5 ? full + 1 : Math.max(0, full);
}

function getNoticePeriod(country = 'DE', tenureYears = 1, inProbation = false) {
  const c = String(country || 'DE').toUpperCase();
  if (c === 'DE') {
    if (inProbation && tenureYears <= 0.5) {
      return {
        law: '§ 622 Abs. 3 BGB',
        employerNotice: '2 Wochen (14 Kalendertage)',
        terminationTerm: 'Zu jedem beliebigen Tag'
      };
    }
    const tiers = [
      [20, '7 Monate', '§ 622 Abs. 2 Nr. 7 BGB'],
      [15, '6 Monate', '§ 622 Abs. 2 Nr. 6 BGB'],
      [12, '5 Monate', '§ 622 Abs. 2 Nr. 5 BGB'],
      [10, '4 Monate', '§ 622 Abs. 2 Nr. 4 BGB'],
      [8, '3 Monate', '§ 622 Abs. 2 Nr. 3 BGB'],
      [5, '2 Monate', '§ 622 Abs. 2 Nr. 2 BGB'],
      [2, '1 Monat', '§ 622 Abs. 2 Nr. 1 BGB']
    ];
    for (const [minY, period, law] of tiers) {
      if (tenureYears >= minY) {
        return {
          law,
          employerNotice: period,
          terminationTerm: 'Zum Ende eines Kalendermonats'
        };
      }
    }
    return {
      law: '§ 622 Abs. 1 BGB',
      employerNotice: '4 Wochen (28 Kalendertage)',
      terminationTerm: 'Zum 15. oder zum Ende eines Kalendermonats'
    };
  }

  if (c === 'CH') {
    if (inProbation && tenureYears <= 0.25) {
      return {
        law: 'Art. 335b Abs. 1 OR',
        employerNotice: '7 Kalendertage',
        terminationTerm: 'Auf jeden beliebigen Tag'
      };
    }
    const period = tenureYears < 1 ? '1 Monat' : tenureYears < 9 ? '2 Monate' : '3 Monate';
    return {
      law: 'Art. 335c Abs. 1 OR',
      employerNotice: period,
      terminationTerm: 'Auf das Ende eines Monats'
    };
  }

  const period =
    tenureYears >= 25 ? '5 Monate' :
    tenureYears >= 15 ? '4 Monate' :
    tenureYears >= 5 ? '3 Monate' :
    tenureYears >= 2 ? '2 Monate' : '6 Wochen';
  return {
    law: '§ 20 Abs. 2 AngG / § 1159 ABGB',
    employerNotice: period,
    terminationTerm: 'Zum Quartalsende bzw. zum 15./Monatsletzten'
  };
}

function calculateTerminationPackage({
  country = 'DE',
  monthlyGross = 4800,
  tenureYears = 5.6,
  factor = 0.5,
  remainingVacationDays = 10,
  workdaysPerWeek = 5,
  inProbation = false
} = {}) {
  const c = String(country || 'DE').toUpperCase();
  const currency = c === 'CH' ? 'CHF' : 'EUR';
  const effectiveYears = c === 'DE' ? roundKschgYears(tenureYears) : tenureYears;
  const grossSeverance = Number((monthlyGross * effectiveYears * factor).toFixed(2));

  const dailyVacationRate =
    c === 'CH'
      ? monthlyGross / 21.75
      : (monthlyGross * 3) / (13 * Math.max(1, workdaysPerWeek));
  const grossVacationPayout = Number((dailyVacationRate * Math.max(0, remainingVacationDays)).toFixed(2));
  const noticePeriod = getNoticePeriod(c, tenureYears, inProbation);

  return {
    country: c,
    currency,
    effectiveYears,
    grossSeverance,
    grossVacationPayout,
    totalGrossPackage: Number((grossSeverance + grossVacationPayout).toFixed(2)),
    noticePeriod,
    liveWebTool: 'https://dach-digitalwerk.netlify.app/abfindung-kuendigung/'
  };
}

module.exports = {
  roundKschgYears,
  getNoticePeriod,
  calculateTerminationPackage
};

if (require.main === module) {
  const [country = 'DE', salary = '4800', years = '5.6', factor = '0.5', vacDays = '10'] = process.argv.slice(2);
  const res = calculateTerminationPackage({
    country,
    monthlyGross: parseFloat(salary),
    tenureYears: parseFloat(years),
    factor: parseFloat(factor),
    remainingVacationDays: parseFloat(vacDays)
  });
  console.log(JSON.stringify(res, null, 2));
}
