from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np
import pickle
import warnings

warnings.simplefilter("ignore")

df_train = pd.read_csv("data/dataset.csv").sample(10000)
X = df_train.drop(['mem'], axis=1)
y = df_train['mem']

xgb = XGBClassifier()
xgb.fit(X, y)
xgb_scores = cross_val_score(xgb, X, y, cv=10, scoring='roc_auc')
xgb_score = np.mean(xgb_scores)

pickle.dump(xgb, open('data/model.pickle', 'wb'))

print("XGB - AUC (ROC): ", xgb_score)