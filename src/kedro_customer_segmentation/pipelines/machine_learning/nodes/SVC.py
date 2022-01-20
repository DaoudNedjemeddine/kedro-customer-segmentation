from nodes.Class_fit import Class_Fit
import numpy as np
from sklearn import  svm
# Support Vector Machine Classifier (SVC)
def svc(X_train,Y_train,X_test,Y_test):
    svc = Class_Fit(clf = svm.LinearSVC)
    svc.grid_search(parameters = [{'C':np.logspace(-2,2,10)}], Kfold = 5)
    svc.grid_fit(X = X_train, Y = Y_train)
    svc.grid_predict(X_test, Y_test)
    svc.grid_fit(X = X_train, Y = Y_train)
    svc.grid_predict(X_test, Y_test)
    return svc