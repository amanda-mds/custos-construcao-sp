import pandas as pd

ipca = pd.read_csv("../data/raw/ipca/ipca_433.csv", sep=";", decimal=",",
                   encoding="latin-1", skipfooter=1, engine="python")
ipca.columns = ["data", "ipca_var"]
ipca["data"] = pd.to_datetime(ipca["data"], format="%m/%Y")
print(ipca.head())
print(ipca.tail())


incc = pd.read_csv("../data/raw/incc/incc_192.csv", sep=";", decimal=",",
                   encoding="latin-1", skipfooter=1, engine="python", usecols=[0, 1])
incc.columns = ["data", "incc_var"]
incc["data"] = pd.to_datetime(incc["data"], format="%m/%Y")
print(incc.head())
print(incc.tail())

indices = pd.merge(ipca, incc, on="data")
print(indices.head())

indices.to_csv("../data/processed/indices.csv", index=False)
print("Arquivo salvo!")