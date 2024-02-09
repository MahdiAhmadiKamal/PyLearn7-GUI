
print("\nThis program checks the list's symmetry.")
list = []

m = int(input("enter number of elements in your list: "))
print ("")
print ("You should enter the elements from first to last.")

for i in range (m):
    n = float(input("enter your element:"))
    list.append(n)

print ("your list: ", list)

for i in range (len(list)//2):
    if list[i]!=list[-i-1]:
        print("Your list is asymmetric.\n")
        break
else:
    print("Your list is symmetric.\n")
