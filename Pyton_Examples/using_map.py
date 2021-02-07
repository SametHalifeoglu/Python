name_array = ["John", "Peter", "Lily"]
age_array = [5, 7, 10]


def say_hello(name, age):
    person = name + " " + str(age)
    return person


print("...............................................................")


list(map(lambda x: print(x + 1, end=''), range(int(input("Give a parameter: ")))))



