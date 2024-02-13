import sqlite3


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
    connection = sqlite3.connect("store.db")
    my_cursor = connection.cursor()

def show_list():
    # for data in my_cursor.execute("SELECT * FROM customers WHERE Country = 'France'"):
        # print(data)

    result = my_cursor.execute("SELECT * FROM products")
    products = result.fetchall()

    for product in products:
        print(product)

def add_new():
    new_product_name = input("Enter your new product name: ")
    my_cursor.execute(f"INSERT INTO products (Name) VALUES ('{new_product_name}')")
    connection.commit()

def edit():
    product_id = input("Enter the product id: ")
    product_name = input("Enter the product name: ")
    new_price = input("Enter the new price: ")
    my_cursor.execute(f"UPDATE products SET Price='{new_price}' WHERE ProductId='{product_id}' AND Name='{product_name}'")
    connection.commit()

def remove():
    product_id = input("Enter the product id: ")
    product_name = input("Enter the product name: ")
    my_cursor.execute(f"DELETE FROM products WHERE ProductId = '{product_id}' AND Name = '{product_name}'")
    connection.commit()

def search():
    product_id = input("Enter the product id: ")
    product_name = input("Enter the product name: ")
    result = my_cursor.execute(f"SELECT * FROM products WHERE ProductId='{product_id}' OR Name='{product_name}'")
    products = result.fetchall()
    for product in products:
        print(product)

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
    # elif choice == 6:
    #     buy()
    # elif choice == 7:
    #     qr_code()
    # elif choice == 8:
    #     exit(0)
    else:
        print ("Enter a number between 1 and 8.")
