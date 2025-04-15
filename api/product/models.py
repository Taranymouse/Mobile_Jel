from pydantic import BaseModel
from typing import Optional, List

class ProductModel(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    image_url: Optional[str] = None  # เพิ่มฟิลด์ image_url

class OrderItemModel(BaseModel):
    product_id: int
    quantity: int
    price: float

class OrderModel(BaseModel):
    id: Optional[int] = None
    user_id: int
    order_date: Optional[str] = None
    total_price: float
    items: List[OrderItemModel]