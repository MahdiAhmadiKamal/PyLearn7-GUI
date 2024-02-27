test_list = ['24', '18', '8', '21']
 
# define a function to extract the number from a string
def extract_num(string):
    try:
        return int(string.split()[0])
    except IndexError:
        return None
 
# use map() to apply the extract_num() function to each element of the list
nums = map(extract_num, test_list)
 
# use filter() to remove any None values from the list
res = list(filter(lambda x: x is not None, nums))
 
print("The list after Extracting numbers : ", res)