import re
from datetime import timezone, datetime
from typing import TypedDict

import dateutil.parser

htmlCleanRegEx = re.compile('<.*?>')


def remove_html_tags(text: str):
    replaced = re.sub(htmlCleanRegEx, '', text)
    return replaced


class DataRow(TypedDict):
    member_id: str
    product_id: str
    room_id: str
    timestamp: str
    price: str
    product_name: str
    description: str
    active: str
    deactivate_date: str
    quantity: str
    alcohol_content_ml: str
    start_date: str
    category_id: str
    room_name: str


class CleanedData:
    year: int
    day: int
    month: int
    hour: int
    product_name: str
    price: float
    venue_type: str
    venue_name: str

    def __str__(self):
        return ', '.join("%s: %s" % item for item in self.__dict__.items())


def clean(row: DataRow):
    result = CleanedData()
    time = dateutil.parser.parse(row['timestamp'])
    result.year = time.year
    result.day = time.day
    result.month = time.strftime("%B")
    result.hour = time.hour

    time_zone = str(time).split('+')[1]
    if time_zone == '02:00':
        result.season = "Winter"
    else:
        result.season = "Summer"


    result.product_name = remove_html_tags(row['product_name'])
    result.product_category = row['category_name']

    result.sale_price = float(row['price']) / 100

    result.type = row['description']
    result.name = row['room_name']

    result.sold_at = time
    result.day_name = time.strftime("%A")
    return result.__dict__
