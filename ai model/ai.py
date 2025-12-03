import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

def train_model():
    df = pd.read_csv("data_balita.csv")

    stunting_categories = ['stunted', 'severely stunted']
    df['is_stunted'] = df['Status Gizi'].apply(lambda x: 1 if x in stunting_categories else 0)

    X = df[['Umur (bulan)', 'Tinggi Badan (cm)']]
    y = df['is_stunted']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    with open("model/model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model trained & saved as model.pkl")

if __name__ == "__main__":
    train_model()
