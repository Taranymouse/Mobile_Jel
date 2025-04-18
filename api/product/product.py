from fastapi import HTTPException
from database.query import query_get, query_create, query_update
from .models import ProductModel, OrderModel, OrderItemModel
from typing import List

# ฟังก์ชันสำหรับดึงข้อมูลสินค้า
def get_all_products() -> List[ProductModel]:
    products = query_get("SELECT * FROM products", ())
    return [ProductModel(
        id=product["product_id"],
        name=product["name"],
        description=product["description"],
        price=product["price"],
        promotion_price=product["promotion_price"],  # เพิ่ม promotion_price
        stock=product["stock"],
        category=product["category"],  # เพิ่ม category
        image_url=product["image_url"]
    ) for product in products]

def get_product_by_id(product_id: int) -> ProductModel:
    product = query_get("SELECT * FROM products WHERE product_id = %s", (product_id,))
    if not product:
        raise Exception("Product not found")
    # แมป product_id ไปยัง id
    return ProductModel(id=product[0]["product_id"], 
                        name=product[0]["name"], 
                        description=product[0]["description"], 
                        price=product[0]["price"], 
                        stock=product[0]["stock"])

def create_product(product: ProductModel) -> int:
    sql = """
        INSERT INTO products (name, description, price, promotion_price, stock, category, image_url)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        product.name,
        product.description,
        product.price,
        product.promotion_price,
        product.stock,
        product.category,
        product.image_url
    )
    return query_create(sql, params)

def update_product(product_id: int, product: ProductModel) -> bool:
    # ตรวจสอบว่า promotion_price ถูกตั้งค่าหรือไม่
    category = "Promotion" if product.promotion_price is not None else product.category

    sql = """
        UPDATE products 
        SET name = %s, description = %s, price = %s, promotion_price = %s, 
            stock = %s, category = %s, image_url = %s 
        WHERE product_id = %s
    """
    params = (
        product.name,
        product.description,
        product.price,
        product.promotion_price,
        product.stock,
        category,  # อัปเดต category
        product.image_url,
        product_id
    )
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