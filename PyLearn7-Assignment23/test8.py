
l1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

l2 =[[row[i] for row in l1] for i in range(len(l1[0]))]
for row in l2:
    print(row)

