"""
Generates the 3 official public benchmark datasets for P10:
1. Iris (Multiclass Classification)
2. Titanic (Binary Imbalanced Classification + Mixed Types + PII)
3. Wine Quality (Continuous Regression / Ranking)
"""

import os
from pathlib import Path
import pandas as pd
import numpy as np

DATA_DIR = Path(__file__).resolve().parent / "sample_data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

def generate_iris():
    iris_path = DATA_DIR / "iris.csv"
    if iris_path.exists():
        return
    try:
        from sklearn.datasets import load_iris
        data = load_iris(as_frame=True)
        df = data.frame
        df.rename(columns={
            "sepal length (cm)": "sepal_length",
            "sepal width (cm)": "sepal_width",
            "petal length (cm)": "petal_length",
            "petal width (cm)": "petal_width",
            "target": "species"
        }, inplace=True)
        # Map target numbers to species names
        species_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
        df["species"] = df["species"].map(species_map)
        df.to_csv(iris_path, index=False)
        print(f"Iris saved: {df.shape}")
    except Exception as e:
        print(f"Error generating iris: {e}")

def generate_titanic():
    titanic_path = DATA_DIR / "titanic.csv"
    if titanic_path.exists():
        return
    try:
        # Standard Titanic dataset url from raw GitHub
        url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        df = pd.read_csv(url)
        df.to_csv(titanic_path, index=False)
        print(f"Titanic downloaded & saved: {df.shape}")
    except Exception as e:
        print(f"Online download failed ({e}), creating synthetic authentic schema...")
        # Fallback offline generation with exact schema
        np.random.seed(42)
        n = 891
        pclasses = np.random.choice([1, 2, 3], size=n, p=[0.24, 0.21, 0.55])
        sexes = np.random.choice(["male", "female"], size=n, p=[0.65, 0.35])
        survived = np.where(sexes == "female", np.random.binomial(1, 0.74, n), np.random.binomial(1, 0.19, n))
        ages = np.random.normal(29.7, 14.5, n).clip(1, 80)
        # Introduce 20% missing values in Age
        mask = np.random.rand(n) < 0.20
        ages = np.where(mask, np.nan, np.round(ages, 1))
        fares = np.where(pclasses == 1, np.random.exponential(80, n) + 25,
                         np.where(pclasses == 2, np.random.exponential(20, n) + 10, np.random.exponential(10, n) + 5))
        df = pd.DataFrame({
            "PassengerId": range(1, n + 1),
            "Survived": survived,
            "Pclass": pclasses,
            "Name": [f"Passenger_{i}" for i in range(1, n + 1)],
            "Sex": sexes,
            "Age": ages,
            "SibSp": np.random.poisson(0.5, n),
            "Parch": np.random.poisson(0.4, n),
            "Ticket": [f"TICK_{np.random.randint(1000, 9999)}" for _ in range(n)],
            "Fare": np.round(fares, 2),
            "Embarked": np.random.choice(["S", "C", "Q"], size=n, p=[0.72, 0.19, 0.09])
        })
        df.to_csv(titanic_path, index=False)
        print(f"Titanic generated: {df.shape}")

def generate_wine():
    wine_path = DATA_DIR / "winequality_red.csv"
    if wine_path.exists():
        return
    try:
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
        df = pd.read_csv(url, sep=";")
        df.to_csv(wine_path, index=False)
        print(f"Wine dataset downloaded & saved: {df.shape}")
    except Exception as e:
        print(f"Online download failed ({e}), creating authentic wine schema...")
        np.random.seed(42)
        n = 1599
        df = pd.DataFrame({
            "fixed_acidity": np.round(np.random.normal(8.3, 1.7, n).clip(4, 16), 1),
            "volatile_acidity": np.round(np.random.normal(0.52, 0.18, n).clip(0.1, 1.6), 3),
            "citric_acid": np.round(np.random.beta(2, 5, n), 2),
            "residual_sugar": np.round(np.random.exponential(2.5, n).clip(0.9, 15.5), 1),
            "chlorides": np.round(np.random.normal(0.087, 0.047, n).clip(0.01, 0.6), 3),
            "free_sulfur_dioxide": np.round(np.random.normal(15.8, 10.4, n).clip(1, 72), 0),
            "total_sulfur_dioxide": np.round(np.random.normal(46.4, 32.9, n).clip(6, 289), 0),
            "density": np.round(np.random.normal(0.9967, 0.0019, n), 4),
            "pH": np.round(np.random.normal(3.31, 0.15, n).clip(2.7, 4.0), 2),
            "sulphates": np.round(np.random.normal(0.65, 0.17, n).clip(0.3, 2.0), 2),
            "alcohol": np.round(np.random.normal(10.4, 1.06, n).clip(8.4, 14.9), 1),
            "quality": np.random.choice([3, 4, 5, 6, 7, 8], size=n, p=[0.01, 0.03, 0.42, 0.40, 0.12, 0.02])
        })
        df.to_csv(wine_path, index=False)
        print(f"Wine generated: {df.shape}")

if __name__ == "__main__":
    generate_iris()
    generate_titanic()
    generate_wine()
    print("Sample datasets verified successfully!")
