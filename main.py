from tqdm import tqdm

import sources
from bulkloader import connection
from datacleaning.clean import clean
from dimensions import product_dimension, time_dimension, venue_dimension, sales

HANDLED = dict()


def aggregate(sale):
    key = frozenset((sale['hour'], sale['day'], sale['month'], sale['year'],
                     sale['product_name'], sale['name'], sale['type'], sale['product_category']))

    if HANDLED.get(key) is None:
        HANDLED[key] = sale
    else:
        HANDLED[key]['sale_price'] += sale['sale_price']
    return HANDLED


def insert(rows):
    for row in tqdm(rows, desc="Inserting into fact table..."):
        sales.insert(row)
    connection.commit()
    print("COMMITTED " + str(len(rows)) + "!")


if __name__ == '__main__':
    i = 0
    for row in tqdm(sources.joinedData, desc="Loading rows...."):
        row = clean(row)
        row['product_id'] = product_dimension.ensure(row)
        row['time_id'] = time_dimension.ensure(row)
        row['venue_id'] = venue_dimension.ensure(row)
        aggregate(row)
        i += 1
        if i >= 5000:
            insert(HANDLED.values())
            HANDLED = dict()
            i = 0

connection.commit()
