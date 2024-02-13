from load_database import connection, my_cursor


def remove():
    product_id = input("Enter the product id: ")
    product_name = input("Enter the product name: ")
    my_cursor.execute(f"DELETE FROM products WHERE ProductId = '{product_id}' AND Name = '{product_name}'")
    connection.commit()