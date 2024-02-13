from load_database import connection, my_cursor

def add_new():
    new_product_name = input("Enter your new product name: ")
    my_cursor.execute(f"INSERT INTO products (Name) VALUES ('{new_product_name}')")
    connection.commit()