SELECT data, COUNT(*) AS qtd_insumos
FROM insumos
GROUP BY data
ORDER BY data;