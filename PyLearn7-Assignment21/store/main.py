# import sqlite3
# import load_database
from show_list import *
from add_new import *
from edit import *
from remove import *
from search import *
from buy import *

print ("\n...Welcome to my clothing store application...\n")
def show_menu():
    print("1. show list")
    print("2. add new")
    print("3. edit")
    print("4. remove")
    print("5. search")
    print("6. buy")
    print("7. exit")


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
    elif choice == 7:
        exit(0)
    else:
        print ("Enter a number between 1 and 8.")
