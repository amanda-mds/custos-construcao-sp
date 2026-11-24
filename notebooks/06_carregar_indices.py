import pandas as pd
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

indices = pd.read_csv("../data/processed/indices.csv", parse_dates=["data"])
print(indices.head())

indices.to_sql("indices", engine, if_exists="replace", index=False)
print("Carregado!", len(indices), "linhas")