from fastapi import HTTPException
from database.query import query_get, query_create, query_update
from .models import ProductModel, OrderModel, OrderItemModel
from typing import List

# ฟังก์ชันสำหรับดึงข้อมูลสินค้า
def get_all_products() -> List[ProductModel]:
    products = query_get("SELECT * FROM products", ())
    return products

def get_product_by_id(product_id: int) -> ProductModel:
    product = query_get("SELECT * FROM products WHERE product_id = %s", (product_id,))
    if not product:
        raise Exception("Product not found")
    return product[0]

def create_product(product: ProductModel) -> int:
    sql = "INSERT INTO products (name, description, price, stock, image_url) VALUES (%s, %s, %s, %s, %s)"
    params = (product.name, product.description, product.price, product.stock, product.image_url)
    return query_create(sql, params)

def update_product(product_id: int, product: ProductModel) -> bool:
    sql = "UPDATE products SET name = %s, description = %s, price = %s, stock = %s, image_url = %s WHERE product_id = %s"
    params = (product.name, product.description, product.price, product.stock, product.image_url, product_id)
    return query_update(sql, params)

def delete_product(product_id: int) -> bool:
    sql = "DELETE FROM products WHERE product_id = %s"
    return query_update(sql, (product_id,))

# ฟังก์ชันสำหรับสร้างคำสั่งซื้อ
def create_order(order: OrderModel) -> int:
    sql_order = "INSERT INTO orders (user_id, order_date, total_price) VALUES (%s, NOW(), %s)"
    order_id = query_create(sql_order, (order.user_id, order.total_price))
    
    for item in order.items:
        sql_item = "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)"
        query_create(sql_item, (order_id, item.product_id, item.quantity, item.price))
    
    return order_id