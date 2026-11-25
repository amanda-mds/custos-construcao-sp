import pandas as pd

pd.set_option("display.max_colwidth", 150)
pd.set_option("display.width", 250)

arquivo = "../data/raw/sinapi/2026-10/SINAPI_Referência_2026_10.xlsx"

comp = pd.read_excel(arquivo, sheet_name="Analítico", header=9, engine="calamine")

comp.columns = ["grupo", "cod_composicao", "tipo_item", "cod_item",
                "descricao", "unidade", "coeficiente", "situacao"]

itens = comp[comp["tipo_item"].notna()].copy()
cabecalhos = comp[comp["tipo_item"].isna()].copy()

# 1) Esquadrias de alumínio (pergunta 5)
esquadrias = cabecalhos[
    cabecalhos["descricao"].str.contains("ALUM[IÍ]NIO", case=False, na=False)
    & cabecalhos["descricao"].str.contains("JANELA|PORTA", case=False, na=False)
]
print("Esquadrias de alumínio encontradas:", len(esquadrias))

janela = itens[itens["cod_composicao"] == 94570]
print("\nItens da janela 94570:")
print(janela[["tipo_item", "cod_item", "unidade", "coeficiente"]].to_string(index=False))

# 2) Paredes de alvenaria (pergunta 3)
paredes = cabecalhos[
    cabecalhos["descricao"].str.contains("ALVENARIA DE VEDA", case=False, na=False)
    & cabecalhos["descricao"].str.contains("CER[AÂ]MICO", case=False, na=False)
]
print("\nParedes de alvenaria encontradas:", len(paredes))

parede = itens[itens["cod_composicao"] == 103330]
print("\nItens da parede 103330:")
print(parede[["tipo_item", "cod_item", "unidade", "coeficiente"]].to_string(index=False))