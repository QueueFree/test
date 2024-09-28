import sqlite3
from db import queries

db = sqlite3.connect('test.db')
cursor = db.cursor()


async def sql_create():
    if db:
        print('база данных создана')

    cursor.execute(queries.CREATE_TABLE_PRODUCTS)

    db.commit()


async def sql_insert_products(product_id, name_products, category, size_products, price_products, photo):
    cursor.execute(queries.INSERT_PRODUCTS_QUERY, (
        product_id,
        name_products,
        category,
        size_products,
        price_products,
        photo
    ))

    db.commit()
    db.close()
