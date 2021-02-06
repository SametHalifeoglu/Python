try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as err:
    print(err)


try:
    10/0
except ZeroDivisionError as err:
    print(err)


try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Value Error")


try:
    10/0
except ZeroDivisionError:
    print("Division Error")
