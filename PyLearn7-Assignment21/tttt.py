result = my_cursor.execute(f"SELECT Count FROM products WHERE ProductId='{product_id}'")
num = result.fetchone()
print(num[0])