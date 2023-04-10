from fastapi import FastAPI, Path
from typing import Optional
from random import sample
import sqlite3

app = FastAPI()

def query_db(query_str: str) -> tuple:
    try:
        with sqlite3.connect('./cleaned_db.sqlite') as con:
            cur = con.cursor()
    except sqlite3.Error:
        return None
    print(query_str)
    res = cur.execute(query_str)
    return res


@app.get('/')
def home():
    return {"Test": "Test_data"}


#! Endpoint that returns all words categories
@app.get('/categories')
def categories():
    res = query_db('SELECT DISTINCT category FROM words;')
    data = [x[0] for x in res.fetchall()]
    data_dict = {k:v for k,v in enumerate(data)}
    return data_dict


#! Endpoint that returns number of words from certain category
@app.get('/words/{category}')
def words(category: str = Path(None, description="Specify words category"), count: Optional[int] = None):
    # Get the id scope
    ids_query = f'SELECT id FROM words WHERE category = \'{category}\';'
    res_ids_query = query_db(ids_query)
    ids_list = [str(x[0]) for x in res_ids_query.fetchall()]

    # Check if enough words
    if count != None and count < len(ids_list):
        # Select random ids of words
        random_ids = sample(ids_list, k=count)
        random_ids_set = ','.join(random_ids)

        # query for all words from random id set
        sql = f'SELECT pl_word, en_word FROM words WHERE id in ({random_ids_set});'
        res = query_db(sql)
    else:
        # Query for all words from category
        sql = f'SELECT pl_word, en_word FROM words WHERE category = \'{category}\';'
        res = query_db(sql)
    
    # Fetch data from executed query
    words_list = res.fetchall()
    if words_list == None:
        return {"Bad request": "Nothing to return"}
    
    # prettify data before JSON converting to JSON
    words_dict = {}
    for i,v in enumerate(words_list):
        words_dict[i]= {'pl_word':v[0], 'en_word':v[1]}
    return words_dict

