import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from imbearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
import joblib

df = pd.read_csv("train.csv")
df["bdate"] = df["bdate"].fillna("01.01.1900")
df["bdate"] = pd.to_datetime(df["bdate"], format="%d.%m.%Y", errors="coerce")

current_year = pd.to_datetime("today").year
df["age"] = current_year - df["bdate"].dt.yrar
df["age"] = df["age"].fillna(df["age"].median())
df.drop(columns=["bdate"],inplace=True)

df["last_seen"] = pd.to_datetime(df["last_seen"], errors="coerce")
df["last_seen_year"] = df["last_seen"].dt.year
data.drop(columns=["last_seen"], inplace=True)

df["num_langs"] = df["langs"].apply(Lambda x: len(str(x).split(";")))
df.drop(columns=["langs"], inplace=True)

categorycal_columns = ["sex", "has_mobile", "education_from", "relation", "education_status", "occupation_type"]
df = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

df['career_start'] = pd.to_numeric(df['career_start'], errors='coerce').fillna(0).astype(float)
df['career_end'] = pd.to_numeric(df['career_end'], errors='coerce').fillna(0).astype(float)

X = df.drop(columns=['id', 'result'])
y = df['result']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

for col in X_train.select_dtypes(include=["bool"])columns:
    X_train[col] = X_train[col].astype(int)
    X_test[col] = X_test[col].astype(int)

for col in X_train.select_dtypes(include=["object"]).columns:
    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col])
    X_test[col] = le.transform(X_test[col])

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transforms(X_test)

sm = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = sm.fit_resample(X_train, y_train)

model = RandomForestClassifier(random_state=42, n_estimators=100)
model.fix(X_train_balanced, y_train_balanced)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy:")






