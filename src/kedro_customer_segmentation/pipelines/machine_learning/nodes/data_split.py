from sklearn import preprocessing, model_selection, metrics, feature_selection
from sklearn import preprocessing, model_selection, metrics, feature_selection
from sklearn import model_selection
import pandas as pd


def data_split(selected_customers: pd.DataFrame):
    columns = ['mean', 'categ_0', 'categ_1', 'categ_2', 'categ_3', 'categ_4' ]
    X = selected_customers[columns]
    Y = selected_customers['cluster']
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, train_size = 0.8)
    return [X_train, X_test, Y_train, Y_test] 


