import pandas as pd

def create_to_canceled(df_initial: pd.DataFrame):
    df_cleaned = df_initial.copy(deep = True)
    df_cleaned['QuantityCanceled'] = 0

    entry_to_remove = [] ; doubtfull_entry = []

    for index, col in  df_initial.iterrows():
        print(index)
        if (col['Quantity'] > 0) or col['Description'] == 'Discount': continue        
        df_test = df_initial[(df_initial['CustomerID'] == col['CustomerID']) &
                            (df_initial['StockCode']  == col['StockCode']) & 
                            (df_initial['InvoiceDate'] < col['InvoiceDate']) & 
                            (df_initial['Quantity']   > 0)].copy()
        #_________________________________
        # Cancelation WITHOUT counterpart
        if (df_test.shape[0] == 0): 
            doubtfull_entry.append(index)
        #________________________________
        # Cancelation WITH a counterpart
        elif (df_test.shape[0] == 1): 
            index_order = df_test.index[0]
            df_cleaned.loc[index_order, 'QuantityCanceled'] = -col['Quantity']
            entry_to_remove.append(index)        
        #______________________________________________________________
        # Various counterparts exist in orders: we delete the last one
        elif (df_test.shape[0] > 1): 
            df_test.sort_index(axis=0 ,ascending=False, inplace = True)        
            for ind, val in df_test.iterrows():
                if val['Quantity'] < -col['Quantity']: continue
                df_cleaned.loc[ind, 'QuantityCanceled'] = -col['Quantity']
                entry_to_remove.append(index) 
                break  
    entry_to_remove = pd.DataFrame(entry_to_remove, columns=['index'])
    doubtfull_entry = pd.DataFrame(doubtfull_entry, columns=['index'])
    return [entry_to_remove, doubtfull_entry]
