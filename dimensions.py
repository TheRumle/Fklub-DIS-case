from pygrametl.tables import CachedDimension, BulkFactTable

from bulkloader import pgcopybulkloader

product_dimension = CachedDimension(
    name='public.product_dimension',
    key='product_Id ',
    attributes=['product_name', 'product_category'])

time_dimension = CachedDimension(
    key='time_id',
    name='time_dimension',
    attributes=['year', 'month', 'day', 'hour', 'day_name', 'sold_at', 'season']
)

venue_dimension = CachedDimension(
    key='venue_id',
    name='venue_dimension',
    attributes=['name', 'type']
)

sales = BulkFactTable(
    name='sales',
    keyrefs=['time_id', 'venue_id', 'product_id'],
    measures=['sale_price'],
    bulkloader=pgcopybulkloader
)
