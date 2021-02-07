func = lambda x: x * 2
print(func(2))

print(".................................................")

# Lambda functions are used along with built-in functions like filter(), map() etc.
# Example use with filter()
# The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to "True".

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print(new_list)

print(".................................................")

# Example use with map()
# The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.

my_list = [1, 5, 4, 6]

new_list = list(map(lambda x: x * 2, my_list))

print(new_list)

print(".................................................")


def my_func(n):
    return lambda a: a * n


output = my_func(2)
print(output(3))

print(".................................................")


output = list(map(my_func(3), my_list))
print(output)

