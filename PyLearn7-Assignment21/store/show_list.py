from load_database import my_cursor

def show_list():

    print("\nlist of products:")
    print ("\nID   name   price   count\n")
    result = my_cursor.execute("SELECT * FROM products")
    products = result.fetchall()

    for product in products:
        print(product)
    
    print("")