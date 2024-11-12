import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv("titanic.csv")

df.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis = 1, inplace = True)
df.info()

df["Embarked"].fillna("S", inplace=True)

age_1 = df[df["Pclass"] == 1]["Age"].median()
age_2 = df[df["Pclass"] == 2]["Age"].median()
age_3 = df[df["Pclass"] == 3]["Age"].median()

def age(row):
    if pd.isnull(row["Age"]):
        if row["Pclass"] == 1:
            return age_1
        if row["Pclass"] == 2:
            return age_2
        return age_3
    return row["Age"]

df["Age"] = df.apply(age, axis = 1)

def fill_sex(sex):
    if sex == "male":
        return 0
    df["Sex"] = df["Sex"].apply(fill_sex)

    df[list(pd.get_dummies(df["Embarked"]).columns)] = pd.get_dummies(df["Embarked"])
    df.drop("Embarked", axis = 1, implace = True)

#leeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

x = df.drop("Survived", axis = 1)
y = df["Survived"]

x_train, x_text, y_train, y_test = train_test_split(x, y, test_size=0.25)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_train = sc.transform(x_test)

classfier = KNeighborsClassifier(n_neighbors = 5)
classfier.fit(x_train, y_train)


y_pred = classfier.predict(x_test)
print("Відсоток правильнопередбачених результатів:", accuracy_score(y_test, y_pred)*100)
print("Confusion matrix:")
print(confusion_matrix(y_test, y_pred))












