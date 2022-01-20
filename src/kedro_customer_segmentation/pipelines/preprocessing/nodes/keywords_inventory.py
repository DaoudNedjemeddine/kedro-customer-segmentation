import pandas as pd
import nltk

def keywords_inventory(data: pd.DataFrame):
    data = pd.DataFrame(data['Description'].unique()).rename(columns = {0:'Description'})
    is_noun = lambda pos: pos[:2] == 'NN'
    colonne = 'Description'
    stemmer = nltk.stem.SnowballStemmer("english")
    keywords_roots  = dict()  # collect the words / root
    keywords_select = dict()  # association: root <-> keyword
    category_keys   = []
    count_keywords  = dict()
    icount = 0
    for s in data[colonne]:
        if pd.isnull(s): continue
        lines = s.lower()
        tokenized = nltk.word_tokenize(lines)
        nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
        
        for t in nouns:
            t = t.lower() ; racine = stemmer.stem(t)
            if racine in keywords_roots:                
                keywords_roots[racine].add(t)
                count_keywords[racine] += 1                
            else:
                keywords_roots[racine] = {t}
                count_keywords[racine] = 1
    
    for s in keywords_roots.keys():
        if len(keywords_roots[s]) > 1:  
            min_length = 1000
            for k in keywords_roots[s]:
                if len(k) < min_length:
                    clef = k ; min_length = len(k)            
            category_keys.append(clef)
            keywords_select[s] = clef
        else:
            category_keys.append(list(keywords_roots[s])[0])
            keywords_select[s] = list(keywords_roots[s])[0]   
    print(category_keys)
    category_keys = pd.DataFrame(category_keys)
    rows = []
    for i in keywords_select:
        rows.append([i, keywords_select[i]])
    keywords_select = pd.DataFrame(rows)
    rows = []
    for i in count_keywords:
        rows.append([i, count_keywords[i]])
    count_keywords = pd.DataFrame(rows)
    return category_keys, keywords_select, count_keywords