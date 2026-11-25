import pandas as pd

pd.set_option("display.max_colwidth", 80)
pd.set_option("display.width", 200)

arquivo = "../data/raw/sinapi/2026-10/SINAPI_Referência_2026_10.xlsx"

comp = pd.read_excel(arquivo, sheet_name="Analítico", header=9, engine="calamine")

comp.columns = ["grupo", "cod_composicao", "tipo_item", "cod_item",
                "descricao", "unidade", "coeficiente", "situacao"]

itens = comp[comp["tipo_item"].notna()].copy()

janela = itens[itens["cod_composicao"] == 94570]

print(janela[["tipo_item", "cod_item", "unidade", "coeficiente"]].to_string(index=False))