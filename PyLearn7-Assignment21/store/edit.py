from load_database import connection, my_cursor

def edit():
    product_id = input("Enter the product id: ")
    result = my_cursor.execute(f"SELECT * FROM products WHERE ProductId='{product_id}'")
    product = result.fetchone()
    print(product)

    new_price = input("Enter the new price: ")
    new_count = input("Enter the new count: ")
    my_cursor.execute(f"UPDATE products SET Price='{new_price}' WHERE ProductId='{product_id}'")
    my_cursor.execute(f"UPDATE products SET Count='{new_count}' WHERE ProductId='{product_id}'")
    
    print("\nChanges applied successfully:")
    result = my_cursor.execute(f"SELECT * FROM products WHERE ProductId='{product_id}'")
    product = result.fetchone()
    print(product)
    connection.commit()