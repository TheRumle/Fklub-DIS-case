import psycopg2 as psycopg2
import pygrametl

import sources
from datacleaning.cleaner import clean

pgconn = psycopg2.connect(user='postgres', password='admin')
connection = pygrametl.ConnectionWrapper(pgconn)
connection.setasdefault()
connection.execute('set search_path to pygrametlexa')

if __name__ == '__main__':
    cleaned_products = []
    cleaned_sales = []
    cleaned = []
    for row in sources.joinedData:
        cleanedRow = clean(row)
        print(cleanedRow)


        # Write to dimensions table


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
