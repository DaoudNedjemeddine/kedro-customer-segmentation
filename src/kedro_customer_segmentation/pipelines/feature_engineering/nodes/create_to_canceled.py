import pandas as pd

def create_to_canceled(data: pd.DataFrame):
    df_cleaned = data.copy(deep = True)
    df_cleaned['QuantityCanceled'] = 0

    entry_to_remove = [] ; doubtfull_entry = []

    for index, col in  data.iterrows():
        if (col['Quantity'] > 0) or col['Description'] == 'Discount': continue        
        df_test = data[(data['CustomerID'] == col['CustomerID']) &
                            (data['StockCode']  == col['StockCode']) & 
                            (data['InvoiceDate'] < col['InvoiceDate']) & 
                            (data['Quantity']   > 0)].copy()
        #_________________________________
        # Cancelation WITHOUT counterpart
        if (df_test.shape[0] == 0): 
            doubtfull_entry.append(index)
        #________________________________
        # Cancelation WITH a counterpart
        elif (df_test.shape[0] == 1): 
            index_order = df_test.index[0]
            data.loc[index_order, 'QuantityCanceled'] = -col['Quantity']
            entry_to_remove.append(index)        
        #______________________________________________________________
        # Various counterparts exist in orders: we delete the last one
        elif (df_test.shape[0] > 1): 
            df_test.sort_index(axis=0 ,ascending=False, inplace = True)        
            for ind, val in df_test.iterrows():
                if val['Quantity'] < -col['Quantity']: continue
                data.loc[ind, 'QuantityCanceled'] = -col['Quantity']
                entry_to_remove.append(index) 
                break  
    return [entry_to_remove, doubtfull_entry]
