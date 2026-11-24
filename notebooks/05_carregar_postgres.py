import pandas as pd
from getpass import getpass
from sqlalchemy import create_engine, URL

senha = input("Senha do PostgreSQL: ")

url = URL.create(
    "postgresql+psycopg",
    username="postgres",
    password=senha,
    host="localhost",
    port=5432,
    database="custos_construcao",
)
engine = create_engine(url)

insumos = pd.read_csv("../data/processed/insumos.csv", parse_dates=["data"])
insumos.to_sql("insumos", engine, if_exists="append", index=False)

print("Carregado!", len(insumos), "linhas")