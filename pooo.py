import pandas as pd
df = pd.read_csv("IMDB-Movie-Data.csv")


print(df["Genre"].min())