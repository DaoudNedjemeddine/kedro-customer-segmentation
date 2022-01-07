import pandas as pd

def add_column_TotalPrice(data: pd.DataFrame):
    data['TotalPrice'] = data['UnitPrice'] * (data['Quantity'] - data['QuantityCanceled'])
    return data
