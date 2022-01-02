import pandas as pd

def drop_missing(data: pd.DataFrame):
	data.dropna(axis = 0, subset = ['CustomerID'], inplace = True)
	return data
