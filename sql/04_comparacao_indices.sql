SELECT
    p.de,
    p.ate,
    ROUND(((EXP(SUM(LN(1 + i.incc_var / 100))) - 1) * 100)::numeric, 1) AS incc_acum_pct,
    ROUND(((EXP(SUM(LN(1 + i.ipca_var / 100))) - 1) * 100)::numeric, 1) AS ipca_acum_pct
FROM (VALUES
        (DATE '2020-01-01', DATE '2022-01-01'),
        (DATE '2022-01-01', DATE '2024-12-01'),
        (DATE '2024-12-01', DATE '2026-10-01')
     ) AS p(de, ate)
JOIN indices i ON i.data > p.de AND i.data <= p.ate
GROUP BY p.de, p.ate
ORDER BY p.de;