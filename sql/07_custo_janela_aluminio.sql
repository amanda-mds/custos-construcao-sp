WITH receita AS (
    SELECT * FROM (VALUES
        (36896, 'Janela',   0.833300),
        (39961, 'Silicone', 0.667857),
        (4377,  'Parafuso', 9.200000),
        (6111,  'Servente', 0.156509),
        (4750,  'Pedreiro', 0.313018)
    ) AS r(codigo, item, coeficiente)
)
SELECT
    i.data,
    ROUND(SUM(r.coeficiente * i.preco), 2) AS custo_m2,
    COUNT(*) AS itens_encontrados
FROM receita r
JOIN insumos i ON i.codigo = r.codigo
GROUP BY i.data
ORDER BY i.data;