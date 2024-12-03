import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

df = pd.read_csv("train.csv")

df["bdate"] = df["bdate"].fillna("01.01.1900")
df["bdate"] = pd.to_datetime(df["bdate"], format = "%d.%m.%Y", errors = "coerce")

current_year = pd.to_datetime("today").year
df["age"] = current_year = df["bdate"].dt.year
df["age"] = data["age"].fillna(df["age"].median())
df.drop(columns=["bdate"], inplace=True)








