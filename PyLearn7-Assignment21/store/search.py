from load_database import my_cursor

def search():
    product_id = input("Enter the product id: ")
    product_name = input("Enter the product name: ")
    result = my_cursor.execute(f"SELECT * FROM products WHERE ProductId='{product_id}' OR Name='{product_name}'")
    products = result.fetchall()
    for product in products:
        print(product)