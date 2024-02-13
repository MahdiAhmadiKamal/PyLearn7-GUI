from load_database import connection, my_cursor

def edit():
    product_id = input("Enter the product id: ")
    product_name = input("Enter the product name: ")
    new_price = input("Enter the new price: ")
    my_cursor.execute(f"UPDATE products SET Price='{new_price}' WHERE ProductId='{product_id}' AND Name='{product_name}'")
    connection.commit()