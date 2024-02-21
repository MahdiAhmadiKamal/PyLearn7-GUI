p = [5,6,7,8,9]
q = [7,8,10]

# r = [item for item in p if item not in q]
r = [item for item in p or q if item in q and p]
print(r)


