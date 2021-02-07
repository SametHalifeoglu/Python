my_list = [2, 3, 4]
new_list = list(map(lambda x: (x + 2), my_list))
print(new_list)

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print(new_list)


def my_func():
    return lambda x: x + 2


