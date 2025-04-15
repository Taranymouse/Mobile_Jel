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
    promotion_price DECIMAL(10,2) DEFAULT NULL, -- เพิ่มคอลัมน์สำหรับราคาสำหรับโปรโมชั่น
    stock INT,
    category VARCHAR(50), -- เพิ่มคอลัมน์สำหรับประเภทสินค้า
    image_url TEXT
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
-- เพิ่มสินค้าตัวอย่างใหม่
INSERT INTO products (name, description, price, promotion_price, stock, category, image_url)
VALUES 
('Hoodie', 'Warm cotton hoodie', 800.00, NULL, 20, 'Shirt', 'https://images.unsplash.com/photo-1620799140188-3b2a02fd9a77?q=80&w=2272&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D/images/hoodie.jpg'),
('Sneakers', 'Comfortable running sneakers', 1500.00, NULL, 15, 'Pants', 'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8U25lYWtlcnN8ZW58MHx8MHx8fDA%3D/images/sneakers.jpg'),
('Cap', 'Stylish baseball cap', 200.00, NULL, 100, 'Shirt', 'https://plus.unsplash.com/premium_photo-1677405099651-53669fdee9df?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8Q2FwfGVufDB8fDB8fHww/images/cap.jpg'),
('Jacket', 'Waterproof jacket', 2500.00, NULL, 10, 'Shirt', 'https://images.unsplash.com/photo-1525457136159-8878648a7ad0?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDR8fEphY2tldHxlbnwwfHwwfHx8MA%3D%3D/images/jacket.jpg'),
('Socks', 'Cotton socks (pack of 3)', 150.00, NULL, 200, 'Shirt', 'https://images.unsplash.com/photo-1616531758364-731625b1f273?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8U29ja3N8ZW58MHx8MHx8fDA%3D/images/socks.jpg'),
('Scarf', 'Wool scarf for winter', 500.00, NULL, 50, 'Dress', 'https://plus.unsplash.com/premium_photo-1695603438043-1b9ab6ebe1a8?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fFNjYXJmfGVufDB8fDB8fHww/images/scarf.jpg'),
('Gloves', 'Leather gloves', 700.00, NULL, 30, 'Dress', 'https://images.unsplash.com/photo-1611690889004-c009a7e03712?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fEdsb3Zlc3xlbnwwfHwwfHx8MA%3D%3D/images/gloves.jpg'),
('Backpack', 'Durable travel backpack', 1800.00, 1500.00, 25, 'Promotion', 'https://plus.unsplash.com/premium_photo-1670444333487-0064c6399f88?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fEJhY2twYWNrfGVufDB8fDB8fHww/images/backpack.jpg'),
('Watch', 'Digital sports watch', 1200.00, 1000.00, 40, 'Promotion', 'https://plus.unsplash.com/premium_photo-1681504446264-708b83f4ea12?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8V2F0Y2h8ZW58MHx8MHx8fDA%3D/images/watch.jpg'),
('Sunglasses', 'UV protection sunglasses', 900.00, 700.00, 60, 'Promotion', 'https://plus.unsplash.com/premium_photo-1692340973681-e96b10bda346?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8U3VuZ2xhc3Nlc3xlbnwwfHwwfHx8MA%3D%3D/images/sunglasses.jpg');