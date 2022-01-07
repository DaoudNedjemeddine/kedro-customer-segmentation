import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_samples, silhouette_score


def create_customer_categories(data: pd.DataFrame,clusters: pd.DataFrame):
    liste_produits = data['Description'].unique()
    corresp = dict()
    for key, val in zip (liste_produits, clusters):
        corresp[key] = val 
    #__________________________________________________________________________
    data['categ_product'] = data.loc[:, 'Description'].map(corresp)

    for i in range(5):
        col = 'categ_{}'.format(i)        
        df_temp = data[data['categ_product'] == i]
        price_temp = df_temp['UnitPrice'] * (df_temp['Quantity'] - df_temp['QuantityCanceled'])
        price_temp = price_temp.apply(lambda x:x if x > 0 else 0)
        data.loc[:, col] = price_temp
        data[col].fillna(0, inplace = True)
    #__________________________________________________________________________________________________
    data[['InvoiceNo', 'Description', 'categ_product', 'categ_0', 'categ_1', 'categ_2', 'categ_3','categ_4']][:5]
    #___________________________________________
    # somme des achats / utilisateur & commande
    temp = data.groupby(by=['CustomerID', 'InvoiceNo'], as_index=False)['TotalPrice'].sum()
    basket_price = temp.rename(columns = {'TotalPrice':'Basket Price'})
    #____________________________________________________________
    # pourcentage du prix de la commande / categorie de produit
    for i in range(5):
        col = 'categ_{}'.format(i) 
        temp = data.groupby(by=['CustomerID', 'InvoiceNo'], as_index=False)[col].sum()
        basket_price.loc[:, col] = temp[col]
    #_____________________
    # date de la commande
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
    data['InvoiceDate_int'] = data['InvoiceDate'].astype('int64')
    temp = data.groupby(by=['CustomerID', 'InvoiceNo'], as_index=False)['InvoiceDate_int'].mean()
    data.drop('InvoiceDate_int', axis = 1, inplace = True)
    basket_price.loc[:, 'InvoiceDate'] = pd.to_datetime(temp['InvoiceDate_int'])
    #______________________________________
    # selection des entrées significatives:
    basket_price = basket_price[basket_price['Basket Price'] > 0]
    basket_price.sort_values('CustomerID', ascending = True)[:5]
    #________________________________________________________________
    # nb de visites et stats sur le montant du panier / utilisateurs
    transactions_per_user=basket_price.groupby(by=['CustomerID'])['Basket Price'].agg(['count','min','max','mean','sum'])
    for i in range(5):
        col = 'categ_{}'.format(i)
        transactions_per_user.loc[:,col] = basket_price.groupby(by=['CustomerID'])[col].sum() /\
                                                transactions_per_user['sum']*100

    transactions_per_user.reset_index(drop = False, inplace = True)
    basket_price.groupby(by=['CustomerID'])['categ_0'].sum()
    transactions_per_user.sort_values('CustomerID', ascending = True)[:5]
    last_date = basket_price['InvoiceDate'].max().date()

    first_registration = pd.DataFrame(basket_price.groupby(by=['CustomerID'])['InvoiceDate'].min())
    last_purchase      = pd.DataFrame(basket_price.groupby(by=['CustomerID'])['InvoiceDate'].max())

    test  = first_registration.applymap(lambda xk:(last_date - x.date()).days)
    test2 = last_purchase.applymap(lambda x:(last_date - x.date()).days)

    transactions_per_user.loc[:, 'LastPurchase'] = test2.reset_index(drop = False)['InvoiceDate']
    transactions_per_user.loc[:, 'FirstPurchase'] = test.reset_index(drop = False)['InvoiceDate']

    transactions_per_user[:5]
    list_cols = ['count','min','max','mean','categ_0','categ_1','categ_2','categ_3','categ_4']
    #_____________________________________________________________
    selected_customers = transactions_per_user.copy(deep = True)
    matrix = selected_customers[list_cols].values
    scaler = StandardScaler()
    scaler.fit(matrix)
    print('variables mean values: \n' + 90*'-' + '\n' , scaler.mean_)
    scaled_matrix = scaler.transform(matrix)
    n_clusters = 11
    kmeans = KMeans(init='k-means++', n_clusters = n_clusters, n_init=100)
    kmeans.fit(scaled_matrix)
    clusters_clients = kmeans.predict(scaled_matrix)
    silhouette_avg = silhouette_score(scaled_matrix, clusters_clients)
    print('score de silhouette: {:<.3f}'.format(silhouette_avg))
    selected_customers.loc[:, 'cluster'] = clusters_clients
    return selected_customers

