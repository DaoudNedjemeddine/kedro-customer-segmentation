import pandas as pd

def drop_to_canceled(data: pd.DataFrame,entry_to_remove: pd.DataFrame,doubtfull_entry: pd.DataFrame):
    data.drop(entry_to_remove['index'].tolist(), axis = 0,inplace=True)
    data.drop(doubtfull_entry['index'].tolist(), axis = 0,inplace=True)
    return data
