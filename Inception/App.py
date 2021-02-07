print("---------------------Variables & Data Types-----------------------------------")
character_name = "Christiano"
character_surname = "Ronaldo"
character_age = 40
is_Male = True

print("+ His name is " + character_name + " and his age is", character_age, ".")
print("- Is he male ?")
print("+", is_Male)
print("- What is full name?")
print("+ \"" + character_name, character_surname + "\".")
print("+ \"Christiano Ronaldo\".")
print("- Which club is he playing now?")
print("+ Real\n  Madrid")

print("---------------------Working With Strings-----------------------------------")

print(character_name.lower(), character_surname.lower())
print(character_name.upper(), character_surname.upper())
print(character_name.isupper())
print(character_name.upper().isupper())
print(len(character_name))
print(character_name[0])
print(character_name.index("C"))
print(character_name.replace("Chris", "Elon"))

print("----------------------Working With Numbers----------------------------------")

from math import *

print(3 + (4 * 5))
print(10 % 3)
my_num = 5
# print(my_num + " is my favorite number")
print(str(my_num) + " is my favorite number")
my_num = -5
print(abs(my_num))
# -5^2
print(pow(my_num, 2))
print(max(3, 5, 2, 8))

print(round(3.2))
print(round(3.7))

print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))

print("--------------------Getting Input From a User------------------------------------")

"""name = input("Enter your name: ")
print("Hello " + name + "!")"""

print("--------------------Building a Basic Calculator------------------------------------")

"""num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = num1 + num2
result1 = int(num1) + int(num2)

print("Result= "+result+" Result1= "+str(result1)+"")"""

print("--------------------Lists------------------------------------")

friends = ["Kevin", "Karen", "Jim"]
print(friends)
friends = ["Kevin", 1, True, 2, False]
print(friends)
friends = ["Kevin", 1, True, 2, False]
print(friends[2])
print(friends[-1])
print(friends[-5])
print(friends[1:])
print(friends[1:4])
friends[1] = "Mike"
print(friends)
print(friends[1])

print("--------------------Lists Functions------------------------------------")

friends = ["Kevin", "Karen", "Jim"]
lucky_numbers = [1, 5, 9, 7, 11]

friends.extend(lucky_numbers)
print(friends)

friends = ["Kevin", "Karen", "Jim"]

friends.append("Creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.clear()
print(friends)

friends = ["Kevin", "Karen", "Jim"]
friends.pop()
print(friends)

friends = ["Kevin", "Karen", "Jim", "Jim", "Bobby"]
print(friends.count("Jim"))

friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends = ["Kevin", "Karen", "Jim", "Jim", "Bobby"]
friends2 = friends.copy()
print(friends2)

print("--------------------Tuples------------------------------------")

# Tuples never be modified (add, change, remove etc.)
coordinates = (4, 5)
print(coordinates)
coordinates = [(1, 2), (3, 4), (5, 6)]
print(coordinates)

print("--------------------Comments------------------------------------")

# Comments

'''
comment1
comment2
comment3
'''





