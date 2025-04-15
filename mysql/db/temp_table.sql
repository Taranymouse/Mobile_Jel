-- ตารางผู้ใช้ (ลูกค้า)
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    password VARCHAR(255)
);

-- ตารางสินค้าเสื้อผ้า
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200),
    description TEXT,
    price DECIMAL(10,2),
    stock INT
);

-- ตารางคำสั่งซื้อสินค้า
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    order_date DATETIME,
    total_price DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- ตารางรายละเอียดคำสั่งซื้อ
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- ผู้ใช้ตัวอย่าง
INSERT INTO users (name, email, phone, password)
VALUES ('Somchai', 'somchai@example.com', '0812345678', 'hashedpassword123');

-- สินค้าตัวอย่าง
INSERT INTO products (name, description, price, stock)
VALUES 
('T-Shirt', 'Cotton T-Shirt', 300.00, 50),
('Jeans', 'Blue Denim Jeans', 1200.00, 30);