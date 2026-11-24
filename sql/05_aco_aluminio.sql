WITH pares AS (
    SELECT
        a.data AS de,
        b.data AS ate,
        CASE
            WHEN a.descricao ILIKE '%ALUMINIO%' THEN 'Alumínio'
            WHEN a.descricao ILIKE '%ACO %' OR a.descricao ILIKE '%ACO,%' THEN 'Aço'
            ELSE 'Outros'
        END AS grupo,
        (b.preco / a.preco - 1) * 100 AS variacao_pct
    FROM insumos a
    JOIN insumos b ON a.codigo = b.codigo AND a.descricao = b.descricao
    WHERE a.preco >= 1
      AND (a.data, b.data) IN (('2020-01-01','2022-01-01'),
                               ('2022-01-01','2024-12-01'),
                               ('2024-12-01','2026-10-01'))
)
SELECT
    de,
    ate,
    grupo,
    COUNT(*) AS qtd_itens,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY variacao_pct)::numeric, 1) AS mediana_pct
FROM pares
GROUP BY de, ate, grupo
ORDER BY de, grupo;