import sqlite3

connection = sqlite3.connect("store.db")
my_cursor = connection.cursor()