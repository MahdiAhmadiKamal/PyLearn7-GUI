test_list = ['24', None, '8', '21']
new = []
for i in test_list:
    try:
        j = int(i.split()[0])
        new.append(j)
    except(AttributeError):
        new.append(i)
        pass

print(new)