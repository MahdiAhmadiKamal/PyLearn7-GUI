import sqlite3

selected_products=[]
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

    result = my_cursor.execute("SELECT ProductId FROM products")
    product_ids = result.fetchall()
    ll=list(product_ids)
    print(ll)


def show_list():
    # for data in my_cursor.execute("SELECT * FROM customers WHERE Country = 'France'"):
        # print(data)

    result = my_cursor.execute("SELECT * FROM products")
    products = result.fetchall()

    for product in products:
        print(product)

def add_new():
    new_name = input("Enter your new product name: ")
    new_price = int(input("Enter the price of your new product: "))
    new_count = int(input("Enter the number of your new product: "))
    my_cursor.execute(f"INSERT INTO products (Name) VALUES ('{new_name}')")
    my_cursor.execute(f"INSERT INTO products (Name) VALUES ('{new_price}')")
    my_cursor.execute(f"INSERT INTO products (Name) VALUES ('{new_count}')")
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
    
    connection.commit()

def remove():
    product_id = input("Enter the product id: ")
    result = my_cursor.execute(f"SELECT * FROM products WHERE ProductId='{product_id}'")
    product = result.fetchone()
    print(product)
    my_cursor.execute(f"DELETE FROM products WHERE ProductId = '{product_id}'")
    connection.commit()

def search():
    product_id = input("Enter the product id: ")
    product_name = input("Enter the product name: ")
    result = my_cursor.execute(f"SELECT * FROM products WHERE ProductId='{product_id}' OR Name='{product_name}'")
    products = result.fetchall()
    for product in products:
        print(product)

def buy():
    
    while True:
        product_id = input ("Enter 'f' to finish or enter the product id: ")
        
        if product_id == "f":
            break
        else:
            result = my_cursor.execute(f"SELECT * FROM products WHERE ProductId='{product_id}'")
            product = result.fetchone()
            print(product)

            asked = int(input("How many of this product do you want? "))

            my_cursor.execute(f"INSERT INTO purchased_products (ProductId, Name, Price) SELECT ProductId, Name, Price FROM products WHERE ProductId='{product_id}'")
            my_cursor.execute(f"UPDATE purchased_products SET Count='{asked}' WHERE ProductId='{product_id}'")
            
            my_cursor.execute(f"UPDATE products SET Count=Count-{asked} WHERE ProductId='{product_id}'")
            connection.commit()

            result = my_cursor.execute(f"SELECT * FROM purchased_products")
            purchased_products = result.fetchall()
           
            for purchased_product in purchased_products:
                print(purchased_product)

            
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
