import pandas as pd
df = pd.read_csv("101010.csv")
print(df.info())


print(len(df[pd.isnull(df["Rating"])]))
df["Rating"] = df["Rating"].fillna(-1,inplace = True)

def make_size(size):
    if size[-1] == "M":
        return float(size[:-1])
    elif size[-1] == "k":
        return float(size[:-1])/1024
    return 0
df["Size"] = df["Size"].apply(make_size)
print(df[df["Category"] == "TOOLS"]["Size"].max())


def make_price(price):
    if price[0] == "$":
        return float(size[1:])
    return 0
df["Price"] = df["Price"].apply(make_size)
df["Profit"] = df["Installs"] * df["Price"]
print(df[df["Type"] == "Paid"]["Profit"].max())

