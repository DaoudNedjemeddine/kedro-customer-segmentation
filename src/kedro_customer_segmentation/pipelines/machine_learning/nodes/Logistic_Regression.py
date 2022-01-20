from .Class_fit import Class_Fit
from sklearn import linear_model
import numpy as np

def Logistic_Regression(X_train,Y_train,X_test,Y_test):
    lr = Class_Fit(clf = linear_model.LogisticRegression)
    lr.grid_search(parameters = [{'C':np.logspace(-2,2,20)}], Kfold = 5)
    lr.grid_fit(X = X_train, Y = Y_train)
    lr.grid_predict(X_test, Y_test)
    return lr