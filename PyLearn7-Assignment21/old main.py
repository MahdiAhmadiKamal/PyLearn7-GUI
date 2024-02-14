import sqlite3

PRODUCT_IDs_LIST=[]
PRODUCT_NAMEs_LIST=[]

def show_menu():
    print("1. show list")
    print("2. add new")
    print("3. edit")
    print("4. remove")
    print("5. search")
    print("6. buy")
    print("7. qr code")
    print("8. exit")

def load_database():
    global connection
    global my_cursor
    global product_ids
    connection = sqlite3.connect("store.db")
    my_cursor = connection.cursor()
    
    results = my_cursor.execute("SELECT * FROM products")
    products = results.fetchall()

    for product in products:
        PRODUCT_IDs_LIST.append(product[0])
        PRODUCT_NAMEs_LIST.append(product[1])
    
    print(PRODUCT_IDs_LIST)
    print(PRODUCT_NAMEs_LIST)
        

def show_list():

    print("\n list of products:")

    result = my_cursor.execute("SELECT * FROM products")
    products = result.fetchall()

    for product in products:
        print(product)
    
    print("")

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
        


def search():
    product_id = input("Enter the product id: ")
    product_name = input("Enter the product name: ")
    result = my_cursor.execute(f"SELECT * FROM products WHERE ProductId='{product_id}' OR Name='{product_name}'")
    products = result.fetchall()
    for product in products:
        print(product)

def buy():
    
    while True:
        product_id = input("Enter 'f' to finish or enter the product ID: ")
        
        if product_id == "f":
            break
        elif int(product_id) in PRODUCT_IDs_LIST:
            result = my_cursor.execute(f"SELECT * FROM products WHERE ProductId='{product_id}'")
            product = result.fetchone()
            print(product)

            asked = int(input("How many of this product do you want? "))

            print("\n...Your purchase so far...")
            my_cursor.execute(f"INSERT INTO purchased_products (ProductId, Name, Price) SELECT ProductId, Name, Price FROM products WHERE ProductId='{product_id}'")
            my_cursor.execute(f"UPDATE purchased_products SET Count='{asked}' WHERE ProductId='{product_id}'")
            
            my_cursor.execute(f"UPDATE products SET Count=Count-{asked} WHERE ProductId='{product_id}'")
            connection.commit()

            result = my_cursor.execute(f"SELECT * FROM purchased_products")
            purchased_products = result.fetchall()
           
            for purchased_product in purchased_products:
                print(purchased_product)
        
        else:
            print ('There is no product with this ID in stock.')

            
load_database()
while True:
    show_menu()
    choice = int(input())

    if choice == 1:
        show_list()
    elif choice == 2:
        add_new()
    elif choice == 3:
        edit()
    elif choice == 4:
        remove()
    elif choice == 5:
        search()
    elif choice == 6:
        buy()
    elif choice == 8:
        exit(0)
    else:
        print ("Enter a number between 1 and 8.")
