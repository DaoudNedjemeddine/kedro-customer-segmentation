import pandas as pd

def create_data_nb_products_per_basket(data: pd.DataFrame):
    temp = data.groupby(by=['CustomerID', 'InvoiceNo'], as_index=False)['InvoiceDate'].count()
    nb_products_per_basket = temp.rename(columns = {'InvoiceDate':'Number of products'})
    return nb_products_per_basket
