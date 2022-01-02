import pandas as pd

def drop_duplicates(data: pd.DataFrame):
    data.drop_duplicates(inplace = True)
    return data
