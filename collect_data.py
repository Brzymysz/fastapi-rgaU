import re
import sqlite3
import requests
from os import path
from bs4 import BeautifulSoup

def process_file() -> str:
    # Check if html files exists
    if not path.exists('content.html'):
        
        # Get html content of the website
        try:
            response = requests.get('https://calculla.pl/slownik_matematyczny_en_pl', timeout=2)
        except (Exception, TimeoutError) as e:
            raise e
        
        with open('content.html', 'w+') as f:
            f.write(response.content.decode('utf-8'))
    
    return 'content.html'


def collect_data(file_path: str) -> None:
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')

    category_regex = re.compile(r'outSectionHeader\d+')

    categories_soup = soup.find_all(id=category_regex)
    tables_soup = soup.find_all('tr')
    
    #* Contain all 110 categories in str format
    categories = [ str(category.contents[1].string) for category in categories_soup]

    #* Contain all rows with phrases (headers included) 
    row_data = [(str(row.contents[0].contents[0].string), str(row.contents[1].contents[0].string)) for row in tables_soup]

    category_rows = []
    index = -1
    for row in row_data:
        if row[0].startswith('Fraza') and row[1].startswith('Fraza'):
            index += 1
            category_rows.append([])
        else:
            category_rows[index].append(row)
    
    try:
        con = sqlite3.connect('db.sqlite')
        cursor = con.cursor()
    except Exception:
        print('Something went wrong with opening the database!')

    for category_row, category in zip(category_rows,categories):
        for pl_word, en_word in category_row:
            cursor.execute("INSERT INTO words(pl_word, en_word, category) VALUES (?,?,?)", [pl_word, en_word, category])
            con.commit()


def main():
    path = process_file()
    collect_data(path)

if __name__ == '__main__':
    main()
