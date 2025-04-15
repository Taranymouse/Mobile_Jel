from pydantic import BaseModel
from typing import Optional, List

class ProductModel(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    promotion_price: Optional[float] = None  # เพิ่มฟิลด์ promotion_price
    stock: int
    category: Optional[str] = None  # เพิ่มฟิลด์ category
    image_url: Optional[str] = None

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