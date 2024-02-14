from load_database import connection, my_cursor, PRODUCT_IDs_LIST, PRODUCT_NAMEs_LIST


def buy():
    
    while True:
        product_id = input("Enter 'f' to finish or enter the product ID: ")
        
        if product_id == "f":
            result = my_cursor.execute("SELECT SUM (TotalPrice) FROM purchase_invoice")
            cost = result.fetchone()
            my_cursor.execute(f"INSERT INTO purchase_invoice (TotalPrice) VALUES ('to be paid: {cost}')")
            connection.commit()
            print("\n<<<Your purchase invoice is ready>>>\n")
            break
        elif int(product_id) in PRODUCT_IDs_LIST:
            result = my_cursor.execute(f"SELECT * FROM products WHERE ProductId='{product_id}'")
            product = result.fetchone()
            print(product)
            availabe = int(product[3])
            asked = int(input("How many of this product do you want? "))

            if asked > availabe or availabe == 0:
                print ("Not enough of this product in stock.")

            elif asked <= availabe:
                print("\n...Your purchase so far...")
                my_cursor.execute(f"INSERT INTO purchase_invoice (ProductId, Name, Price) SELECT ProductId, Name, Price FROM products WHERE ProductId='{product_id}'")
                my_cursor.execute(f"UPDATE purchase_invoice SET Count='{asked}' WHERE ProductId='{product_id}'")
                my_cursor.execute(f"UPDATE purchase_invoice SET TotalPrice=Price*Count WHERE ProductId='{product_id}'")

                my_cursor.execute(f"UPDATE products SET Count=Count-{asked} WHERE ProductId='{product_id}'")
                connection.commit()

                result = my_cursor.execute(f"SELECT * FROM purchase_invoice")
                purchased_products = result.fetchall()
            
                for purchased_product in purchased_products:
                    print(purchased_product)    
        
        else:
            print ('There is no product with this ID in stock.')