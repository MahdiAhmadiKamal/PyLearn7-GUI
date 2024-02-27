import collections
a = [1, 2, 3, 4, 4]

# m=[item for item, count in collections.Counter(a).items() if count > 1]
for i in a:
    print(a.index(i))
# print(m)