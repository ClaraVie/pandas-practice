import pandas as pd

#DataFrame =  a tabular data structure with rows and columns

data = {
    "Name" : ["Spongebob", "Patrick", "Squidward"],
    "Age" : [30, 35, 50]
}

df = pd.DataFrame(data, index= ["Employee 1", "Employee 2", "Employee 3"])

#adding new columns
df["Job"] = ["Cook", "N/A", "Cashier"]

#adding new rows
new_rows =  pd.DataFrame(
    [{"Name": "Sandy","Age": 28, "Job": "Engineer"},
    {"Name": "Eugene", "Age": 50, "Job": "Manager"}],
    index=["Employee 4", "Employee 5"])

df=pd.concat([df,new_rows])
print(df)