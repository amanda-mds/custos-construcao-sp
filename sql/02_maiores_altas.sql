SELECT
    a.codigo,
    b.descricao,
    a.preco AS preco_2020,
    b.preco AS preco_2026,
    ROUND((b.preco / a.preco - 1) * 100, 1) AS variacao_pct
FROM insumos a
JOIN insumos b ON a.codigo = b.codigo
WHERE a.data = '2020-01-01'
  AND b.data = '2026-10-01'
  AND a.preco >= 1
  AND a.unidade = b.unidade
  AND a.descricao = b.descricao
ORDER BY variacao_pct DESC
LIMIT 20;