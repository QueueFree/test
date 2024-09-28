CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name_products VARCHAR(255) NOT NULL,
    category VARCHAR(399) NOT NULL,
    size_products VARCHAR(255) NOT NULL,
    price_products INTEGER NOT NULL,
    product_id INTEGER VARCHAR(255) NOT NULL,
    photo VARCHAR(499) NOT NULL
    )
"""


INSERT_PRODUCTS_QUERY = """
    INSERT INTO products (product_id, name_products, category, size_products, price_products, photo)
    VALUES (?, ?, ?, ?, ?, ?)
"""
