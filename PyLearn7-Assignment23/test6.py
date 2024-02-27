   

test_list = ['24', '18', '8', '21']
 
res = list(map(lambda sub:int(''.join(
      [ele for ele in sub if ele.isnumeric()])), test_list))

print(res)