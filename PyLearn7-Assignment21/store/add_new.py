from load_database import connection, my_cursor

def add_new():
    new_name = input("Enter your new product name: ")
    new_price = int(input("Enter the price of your new product: "))
    new_count = int(input("Enter the number of your new product: "))
    my_cursor.execute(f"INSERT INTO products (Name, Price, Count) VALUES ('{new_name}', '{new_price}', '{new_count}')")

    print("\nProduct added successfully:")
    result = my_cursor.execute(f"SELECT * FROM products WHERE Name='{new_name}'")
    new_product = result.fetchone()
    print(new_product)
    connection.commit()