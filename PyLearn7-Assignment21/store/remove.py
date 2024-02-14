from load_database import connection, my_cursor


def remove():
    product_id = input("Enter the product id: ")
    result = my_cursor.execute(f"SELECT * FROM products WHERE ProductId='{product_id}'")
    product = result.fetchone()
    print(product)
    
    warning = input("You are removing a product from your products list. Are you sure? Y/N\n")
    if warning=="Y" or warning=="y":
        my_cursor.execute(f"DELETE FROM products WHERE ProductId = '{product_id}'")
        connection.commit()
        print("Changes applied successfully.\n")
