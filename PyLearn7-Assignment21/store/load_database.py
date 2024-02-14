import sqlite3

PRODUCT_IDs_LIST=[]
PRODUCT_NAMEs_LIST=[]

connection = sqlite3.connect("store.db")
my_cursor = connection.cursor()

    
results = my_cursor.execute("SELECT * FROM products")
products = results.fetchall()

for product in products:
    PRODUCT_IDs_LIST.append(product[0])
    PRODUCT_NAMEs_LIST.append(product[1])
