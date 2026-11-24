import pandas as pd

arquivo = "../data/raw/sinapi/2026-10/SINAPI_Referência_2026_10.xlsx"
df = pd.read_excel(arquivo, sheet_name="ISD", header=9, engine="calamine")

df = df.iloc[:, [0, 1, 2, 3, 4]].join(df["SP"])
df.columns = ["classificacao", "codigo", "descricao", "unidade", "origem", "preco"]

print(df.head())
print(df.shape)

df = df.dropna(subset=["preco"])
df["descricao"] = df["descricao"].str.strip()
df["unidade"] = df["unidade"].str.strip()
df["data"] = pd.to_datetime("2026-10-01")

print(df.shape)
print(df.dtypes)

df.to_csv("../data/processed/insumos_novo.csv", index=False)
print("Salvo!")