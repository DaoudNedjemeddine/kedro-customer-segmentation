import pandas as pd

def create_matrix(data: pd.DataFrame,count_keywords: pd.DataFrame,keywords_select: pd.DataFrame):
    list_products = []
    for row in count_keywords.values:
        word = row[0]
        if word in ['pink', 'blue', 'tag', 'green', 'orange']: 
            continue
        if len(word) < 3 or row[1] < 13: 
            continue
        if ('+' in word) or ('/' in word): 
            continue
        list_products.append([word, row[1]])
    list_products.sort(key = lambda x:x[1], reverse = True)
    liste_produits = data['Description'].unique()
    X = pd.DataFrame()
    for key, occurence in list_products:
        X.loc[:, key] = list(map(lambda x:int(key.upper() in x), liste_produits))
    threshold = [0, 1, 2, 3, 5, 10]
    label_col = []
    for i in range(len(threshold)):
        if i == len(threshold)-1:
            col = '.>{}'.format(threshold[i])
        else:
            col = '{}<.<{}'.format(threshold[i],threshold[i+1])
        label_col.append(col)
        X.loc[:, col] = 0

    for i, prod in enumerate(liste_produits):
        prix = data[ data['Description'] == prod]['UnitPrice'].mean()
        j = 0
        while prix > threshold[j]:
            j+=1
            if j == len(threshold): break
        X.loc[i, label_col[j-1]] = 1
    matrix = pd.DataFrame(X.values)
    return matrix