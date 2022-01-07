import pandas as pd

def create_df_produits(data: pd.DataFrame):
    df_produits = pd.DataFrame(data['Description'].unique()).rename(columns = {0:'Description'})
    return df_produits