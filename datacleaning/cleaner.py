import re

import dateutil.parser

from datacleaning.row_classes import DataRow

htmlCleanRegEx = re.compile('<.*?>')


def remove_html_tags(text: str):
    replaced = re.sub(htmlCleanRegEx, '', text)
    return replaced


class CleanedData:
    sale_id: str
    year: int
    day: int
    month: int
    hour: int
    product_name: str
    is_active: bool
    total_sold: float
    venue_type: str
    venue_name: str
    buyer:str

    def __str__(self):
        return ', '.join("%s: %s" % item for item in self.__dict__.items())

def clean(row: DataRow) -> CleanedData:

    result = CleanedData()
    result.sale_id = row['sale_id']
    time = dateutil.parser.parse(row['timestamp'])
    result.year = time.year
    result.day = time.day
    result.month = time.month
    result.hour = time.hour
    result.product_name = remove_html_tags(row['product_name'])
    result.price = row['price']
    result.venue_type = row['description']
    result.venue_name = row['room_name']
    result.buyer = row['member_id']
    return result
