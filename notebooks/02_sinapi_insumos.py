import pandas as pd
from pathlib import Path

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)


def limpar_insumos_antigo(pasta):
    arquivo = list(Path(pasta).glob("*Insumos*"))[0]
    tabela = pd.read_excel(arquivo, header=6, engine="calamine")
    tabela.columns = ["codigo", "descricao", "unidade", "origem", "preco"]
    tabela = tabela.dropna(subset=["preco"])
    tabela["preco"] = (tabela["preco"].astype(str)
                       .str.replace(".", "", regex=False)
                       .str.replace(",", ".", regex=False)
                       .astype(float))
    tabela["data"] = pd.to_datetime(Path(pasta).name + "-01")
    tabela["descricao"] = tabela["descricao"].str.strip()
    tabela["unidade"] = tabela["unidade"].str.strip()
    return tabela

tabelas = []
for mes in ["2020-01", "2022-01", "2024-12"]:
    tabelas.append(limpar_insumos_antigo("../data/raw/sinapi/" + mes))

insumos = pd.concat(tabelas)
print(len(insumos), "linhas no total")
insumos.to_csv("../data/processed/insumos_antigo.csv", index=False)