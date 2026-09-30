import pandas as pd

#we can use .csv or json files

df = pd.read_csv("pokemons.csv")

#if using json
#df = pd.read_json("file_name")

print(df.to_string())