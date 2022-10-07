import pandas as pd
from pygrametl.datasources import CSVSource, HashJoiningSource

df = pd.read_csv("https://jbencook.s3.amazonaws.com/data/dummy-sales.csv")

df.rename(columns={"revenue": "sales"}, inplace=True)

product_categories = CSVSource(open('source_data/product_categories.csv', 'r', 16384, encoding='utf-8'), delimiter=';')

room_field_names = "room_id", "room_name", "description"
rooms = CSVSource(open('source_data/room.csv', 'r', 16384, encoding='utf-8'), delimiter=';',
                  fieldnames=room_field_names)

categories_fields_names = "category_id", "category_name"
categories = CSVSource(open('source_data/category.csv', 'r', 16384, encoding='utf-8'), delimiter=';',
                       fieldnames=categories_fields_names)

product_field_names = "product_id", "product_name", "price", 'active', "deactive_date", "quantity", "alcohol_content_ml", "start_date"
products = CSVSource(open('source_data/product.csv', 'r', 16384, encoding='utf-8'), delimiter=';',
                     fieldnames=product_field_names)

sale_field_names = "sale_id", "member_id", "product_id", "room_id", "timestamp", "price"
sales = CSVSource(open('source_data/sale.csv', 'r', 16384, encoding='utf-8'), delimiter=';',
                  fieldnames=sale_field_names)

salesAndRooms = HashJoiningSource(src1=sales, key1='room_id', src2=rooms, key2='room_id')
productAndCategories = HashJoiningSource(src1=products, key1='product_id', src2=product_categories, key2='product_id')
productAndCategories = HashJoiningSource(src1=categories, key1='category_id', src2=productAndCategories,
                                         key2='category_id')

joinedData = HashJoiningSource(src1=salesAndRooms, key1='product_id', src2=productAndCategories, key2='product_id')
