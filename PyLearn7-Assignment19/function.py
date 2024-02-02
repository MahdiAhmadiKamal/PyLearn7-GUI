import random

def non_repeating_random_2D_array(rows,cols):
  
    random_numbers = []
    noel=rows*cols                      
    while (len(random_numbers)) < noel:
        
        x = random.randint(1, noel)

        if x in random_numbers:
            random_numbers.remove(x)
            random_numbers.append(x)
        else:
            random_numbers.append(x)


    l= random_numbers
    # def convert_1d_to_2d(l, cols):
    # return [l[i:i + cols] for i in range(0, len(l), cols)]
    print([l[i:i + cols] for i in range(0, len(l), cols)])
    

non_repeating_random_2D_array(4,4)