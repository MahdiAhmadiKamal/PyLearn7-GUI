import sqlite3

connection = sqlite3.connect("chinook.db")
my_cursor = connection.cursor()

# for data in my_cursor.execute("SELECT * FROM customers WHERE Country = 'France'"):
    # print(data)

result = my_cursor.execute("SELECT * FROM customers WHERE Country = 'France'")
french_customers = result.fetchall()

for customer in french_customers:
    print(customer)

# my_cursor.execute("INSERT INTO genres (GenreId, Name) VALUES (26, 'Traditional')")
# connection.commit()

# my_cursor.execute("UPDATE customers SET City='Mashhad', Country='Iran' WHERE FirstName='Helena' AND CustomerId=6")
# connection.commit()

my_cursor.execute("DELETE FROM artists WHERE ArtistId=10")
connection.commit()