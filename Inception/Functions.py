def say_hi():
    print("Hello User")


say_hi()


def say_something(something):
    print("Hello" + something)


say_something(" World")


def say_full_name(name, surname):
    print("Hello" + name, surname + "")


say_full_name(" Chris", "John")

print("--------------------Return Statements-----------------------")


def cube(num):
    return num * num * num


print(cube(3))

print("--------------------If Statements-----------------------")


def state(num1, num2):
    if num1 == num2:
        print("Equal")
    elif num1 > num2:
        print("Big or equal")
    elif num1 < num2:
        print("Small or equal")
    else:
        print("Error")


state(3, 3)


def state1(num1, num2):
    if num1 != num2:
        print("Not equal")


state1(3, 4)
