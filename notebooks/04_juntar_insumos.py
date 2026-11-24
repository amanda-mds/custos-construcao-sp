import pandas as pd

antigo = pd.read_csv("../data/processed/insumos_antigo.csv")
novo = pd.read_csv("../data/processed/insumos_novo.csv")

antigo["descricao"] = antigo["descricao"].str.strip()
antigo["unidade"] = antigo["unidade"].str.strip()

insumos = pd.concat([antigo, novo], ignore_index=True)

print(insumos.shape)
print(insumos["data"].value_counts().sort_index())

meses_por_codigo = insumos.groupby("codigo")["data"].nunique()
print(meses_por_codigo.value_counts().sort_index())

insumos["descricao"] = insumos["descricao"].str.replace("\\", "", regex=False)

insumos.to_csv("../data/processed/insumos.csv", index=False)
print("Salvo!")