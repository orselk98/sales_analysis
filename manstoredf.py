import pandas as pd

df = pd.DataFrame(
    {
        "Name":[
            "Orsel Kapllani",
            "Bjorn Kapllani",
            "Merita Kapllani",
            "Adrian Kapllani",
        ],
        "Age":[27,20,55,54],
        "Sex":["male","male","female", "male"],
    }
)
print(df)
df["Age"]
print(df["Age"])

ages= pd.Series([27,20,55,54], name="Age")
print(ages)

print(df["Age"].max())

print(df.describe())