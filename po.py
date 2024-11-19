import pandas as pd
df = pd.read_csv("train.csv")

print(df["result"].mean())



X = df.drop("result", axis = 1)
y = df["result"]

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)








