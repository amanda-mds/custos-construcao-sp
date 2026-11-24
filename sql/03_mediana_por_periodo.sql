SELECT
    a.data AS de,
    b.data AS ate,
    COUNT(*) AS qtd_itens,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY (b.preco / a.preco - 1) * 100)::numeric, 1) AS mediana_pct
FROM insumos a
JOIN insumos b ON a.codigo = b.codigo AND a.descricao = b.descricao
WHERE a.preco >= 1
  AND (a.data, b.data) IN (('2020-01-01','2022-01-01'),
                           ('2022-01-01','2024-12-01'),
                           ('2024-12-01','2026-10-01'))
GROUP BY a.data, b.data
ORDER BY a.data;