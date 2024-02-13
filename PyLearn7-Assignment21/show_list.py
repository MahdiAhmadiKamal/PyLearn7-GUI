from load_database import my_cursor

def show_list():
    # for data in my_cursor.execute("SELECT * FROM customers WHERE Country = 'France'"):
        # print(data)

    result = my_cursor.execute("SELECT * FROM products")
    products = result.fetchall()

    for product in products:
        print(product)