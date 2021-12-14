x = 2

y = "hello"

# list = unordered set of variables
my_first_list = ['apple', 1, 'banana', 2]

cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}


# EXERCISES

# - Write a loop that uses `while` instead of the built-in looping structure

# - Write a loop that loop over the keys in a dictionary and prints the values

# - Write the functions `is_odd` and `is_even` that are shown in the lecture

# - Loop over `my_first_list` and square the value if the value is a number, and 
# print the calories of the fruit if it’s a fruit (hint: use the dictionary to look up the calories)


for f in my_first_list: 
    print(f)

for f in my_first_list: 
    pass
print(f)

def sq_int(x):
    y = x**2
    return y

y = 5
x = 4
def describe_even(x):
    if is_even(x):
        print("It's even!")
    elif is_odd(x):
        print("It's odd!")
    else: 
        print("It's neither even nor odd")
    


for key, value in cal_lookup.items():
    print(value)


# - Write the functions `is_odd` and `is_even` that are shown in the lecture

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def is_odd(x):
    # if x % 2 != 0:
    if (isinstance(x, float) and x.is_integer() or isinstance(x, int)) and x % 2 != 0:
        return True
    else:
        return False

"""
Loop over my_first_list and square the value if the value is a number, 
and print the calories of the fruit if it’s a fruit (hint: use the dictionary to look up the calories)
"""
for x in my_first_list:
    if isinstance(x, str):
        try:
            result = cal_lookup.get(x, None)
        except: 
            result = "Item was not in the dictionary :("
    else isinstance(x, int):
        print(x**2)
    else:
        result = "Item was not a number and was not in the dictionary"
    print(result)


def dictionary_sq(dictionary: dict):
    """
    This function returns the squared value of every value in the dictionary

    Arguments:
    dictionary : dict, required
    """

    for key, value in dictionary.items():
        print(value**2)



