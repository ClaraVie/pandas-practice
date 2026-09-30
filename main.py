import pandas as pd

# Data cleaning is the process of fixing/removing:
# imcomplete, incorrect, or irrelevant @ dataclass
# 75% of work done with Pandas is data cleaning

df =  pd.read_csv("pokemons.csv")

# 1. Drop irrelevant columns
# df = df.drop(columns=["Legendary", "No"])

# 2. Handle missing data
# df = df.dropna(subset=["Type2"])
df = df.fillna({"Type2": "None"})

# 3. Fix incosistent values
df["Type1"] = df["Type1"].replace({
    "Grass": "GRASS",
    "Water": "WATER",
    "Fire": "FIRE",
})

# 4. Standardize text
# df["Name"] = df["Name"].str.upper()


# 5. Fix data types
# df["Legendary"] = df["Legendary"].astype(bool)

# 6. Removing duplicate values
df = df.drop_duplicates()

print(df.to_string())
