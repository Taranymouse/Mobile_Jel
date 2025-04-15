from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from product import get_all_products, get_product_by_id, create_product, update_product, delete_product, create_order
from product.models import ProductModel, OrderModel
from typing import List
from database.query import query_get  # เพิ่มการนำเข้า query_get

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Clothing Store API!"}

# GET all products
@app.get("/products", response_model=List[ProductModel])
async def read_products():
    try:
        products = get_all_products()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET product by ID
@app.get("/products/{product_id}", response_model=ProductModel)
async def read_product(product_id: int):
    try:
        product = get_product_by_id(product_id)
        return product
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# POST create a new product
@app.post("/products", response_model=ProductModel, status_code=status.HTTP_201_CREATED)
async def create_new_product(product: ProductModel):
    try:
        product_id = create_product(product)
        return {**product.dict(), "id": product_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# PUT update a product by ID
@app.put("/products/{product_id}", response_model=ProductModel)
async def update_existing_product(product_id: int, product: ProductModel):
    try:
        update_product(product_id, product)
        return {**product.dict(), "id": product_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# DELETE a product by ID
@app.delete("/products/{product_id}")
async def delete_existing_product(product_id: int):
    try:
        delete_product(product_id)
        return {"message": "Product deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# POST create a new order
@app.post("/orders", status_code=status.HTTP_201_CREATED)
async def create_new_order(order: OrderModel):
    try:
        order_id = create_order(order)
        return {"message": "Order created successfully", "order_id": order_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/products/category/{category}", response_model=List[ProductModel])
async def read_products_by_category(category: str):
    try:
        products = query_get("SELECT * FROM products WHERE category = %s", (category,))
        return [ProductModel(
            id=product["product_id"],
            name=product["name"],
            description=product["description"],
            price=product["price"],
            promotion_price=product["promotion_price"],
            stock=product["stock"],
            category=product["category"],
            image_url=product["image_url"]
        ) for product in products]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/products/promotions", response_model=List[ProductModel])
async def read_promotion_products():
    try:
        products = query_get("SELECT * FROM products WHERE promotion_price IS NOT NULL", ())
        return [ProductModel(
            id=product["product_id"],
            name=product["name"],
            description=product["description"],
            price=product["price"],
            promotion_price=product["promotion_price"],
            stock=product["stock"],
            category=product["category"],
            image_url=product["image_url"]
        ) for product in products]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))