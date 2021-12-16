# set up 
y = 5
x = 4
my_list = ['apple', 1, 'banana', 2]
cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}


# EXERCISES
# - Write a loop that uses `while` instead of the built-in looping structure
average = .45
current = 100

while current >= average:
    print(f"Current rate is {current}. That's above average!")
    current *= .8

# - Write a loop that loop over the keys in a dictionary and prints the values
for key, value in cal_lookup.items():
    print(value)

# - Write the functions `is_odd` and `is_even` that are shown in the lecture
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def is_odd(x):
    if (isinstance(x, float) and x.is_integer() or isinstance(x, int)) and x % 2 != 0:
        return True
    else:
        return False

def describe_even(x):
    if is_even(x):
        print("It's even!")
    elif is_odd(x):
        print("It's odd!")
    else: 
        print("It's neither even nor odd")

# Loop over `my_first_list` and square the value if the value is a number, and 
# print the calories of the fruit if it’s a fruit
for item in my_list:
    if isinstance(item, str):
        try:
            result = cal_lookup.get(item, None)
        except: 
            result = "Item was not in the dictionary :("
    elif isinstance(item, int):
        print(item**2)
    else:
        result = "Item was not a number and was not in the dictionary. Try again"
    print(result)

# Write a function that: Takes a dictionary as an argument, Loops over the keys in the dictionary,
# Prints the square of the value in the value. Hint: use the `cal_lookup` dictionary for testing.

def dictionary_sq(dictionary: dict):
    """
    This function returns the squared value of every value in the dictionary.

    Arguments:
        dictionary: dict, required
    Returns:
        squared value of every value in the dictionary.
    """

    for key, value in dictionary.items():
        print(value**2)



