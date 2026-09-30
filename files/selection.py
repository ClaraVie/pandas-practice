import pandas as pd

df = pd.read_csv("pokemons.csv", index_col="Name")

# SELECTION BT COLUMN
# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())
# print(df[["Name", "Height", "Weight"]].to_string())

#SELECTION BY ROW/S
# print(df.loc["Charizard"])
# print(df.loc["Charizard"])
# print()
# print("DIFFERENT OUTPUT")
# print(df.loc["Charizard", ["Height", "Weight"]])

#SELECTING A RANGE OF ROWS
# print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])
# print(df.iloc[0:10]) # getting the fisrt 10 rows
# print(df.iloc[0:10:2]) # getting 10 with a pace of 2
# print(df.iloc[0:10:2, 0:3]) # adding args related to the columns

pokemon = input("Enter Pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found in")