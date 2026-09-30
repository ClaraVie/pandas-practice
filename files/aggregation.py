import pandas as pd

# Aggregate functions = Reduces a set o values into a single summary value
# Used to summarize and analyze data
# Often used with the groupby() function

df = pd.read_csv("pokemons.csv")

# Whole dataframe
# print(df.mean(numeric_only=True)) # it shows the average of numeric data
# print(df.sum(numeric_only=True)) # shows the sum
# print(df.min(numeric_only=True)) # shows the minimum
# print(df.max(numeric_only=True)) # shows the maximum
# print(df.count())

# Single column
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())
# print(df["Type2"].count()) # it's equals to 67 becouse some pokemons doesn't have a second type

group = df.groupby("Type1")
# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].min())
# print(group["Height"].max())
# print(group["Height"].count())