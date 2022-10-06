from typing import TypedDict


class Fact:
    product_Id: int
    venue_Id: int
    timeId: int
    SalesPrice: float


class DataRow(TypedDict):
    id: str
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
    room_name:str
