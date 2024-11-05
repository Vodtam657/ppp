import pandas as pd
df = pd.read_csv("101010.csv")
temp = df["Content Rating"].value_counts()
everyone = temp["Teen"]
everyone_10 = temp["Everyone 10+"]
print(everyone/everyone_10)
temp = df.groupby(by = "Category")["Size"].agg(["min", "max"])
print(df[df["Type"] == "Paid"].groupby(by = "Contend Rating")["Price"].agg(["min", "mean", "max"]))
temp = df.pivot_table(index = "Content Rating", columns = "Category", values = "Reviews", aggfunc = "max")
print(temp["EDUCATION", "FAMILY", "GAME"])

temp = df(by = "Rating").agg(["max"])