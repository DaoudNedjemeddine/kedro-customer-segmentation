from .Class_fit import Class_Fit
import numpy as np

def tree(X_train,Y_train,X_test,Y_test):
    tr = Class_Fit(clf = tree.DecisionTreeClassifier)
    tr.grid_search(parameters = [{'criterion' : ['entropy', 'gini'], 'max_features' :['sqrt', 'log2']}], Kfold = 5)
    tr.grid_fit(X = X_train, Y = Y_train)
    tr.grid_predict(X_test, Y_test)
    return tree ; 