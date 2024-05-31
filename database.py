import sqlite3

def create_connection():
    connection = sqlite3.connect('clothing_store.db')
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''DROP TABLE IF EXISTS products''')
    cursor.execute('''CREATE TABLE products
                      (id INTEGER PRIMARY KEY, 
                      name TEXT NOT NULL, 
                      price REAL NOT NULL, 
                      quantity INTEGER NOT NULL,
                      image_path TEXT,
                      color TEXT NOT NULL,
                      size TEXT NOT NULL)''')
    connection.commit()
    connection.close()

def add_product(product_id, name, price, quantity, image_path, color, size):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO products (id, name, price, quantity, image_path, color, size) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                   (product_id, name, price, quantity, image_path, color, size))
    connection.commit()
    connection.close()

def get_products():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    connection.close()
    return products

def get_product_by_id(product_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
    product = cursor.fetchone()
    connection.close()
    return product

def delete_product(product_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    connection.commit()
    connection.close()

def update_product(product_id, name, price, quantity, image_path, color, size):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET name=?, price=?, quantity=?, image_path=?, color=?, size=? WHERE id=?", 
                   (name, price, quantity, image_path, color, size, product_id))
    connection.commit()
    connection.close()
