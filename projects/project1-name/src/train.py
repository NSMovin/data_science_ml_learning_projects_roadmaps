# Simple training script that saves a toy model artifact
import joblib
from sklearn.linear_model import LinearRegression
import numpy as np
import os

def train_and_save(path='models/linear_model.joblib'):
    X = np.arange(10).reshape(-1,1)
    y = 2*X.ravel() + 1
    model = LinearRegression()
    model.fit(X, y)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)
    print(f"Saved model to {path}")

if __name__ == '__main__':
    train_and_save()
