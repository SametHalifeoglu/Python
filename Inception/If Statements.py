print("--------------------Statements 1-----------------------")
is_Male = True

if is_Male:
    print("You're a male")
else:
    print("You're not a male")


print("--------------------Statements 2-----------------------")
is_Male = False
is_tall = True

if is_Male or is_tall:
    print("You're a male or tall or both")
else:
    print("You neither male nor tall")


print("--------------------Statements 3-----------------------")
is_Male = True
is_tall = True

if is_Male and is_tall:
    print("You're a tall male")
else:
    print("You are either not male or not tall or both")


print("--------------------Statements 4-----------------------")
is_Male = False
is_tall = True

if is_Male and is_tall:
    print("You're a tall male")
elif is_Male and not is_tall:
    print("You're a short male")
elif is_tall and not is_Male:
    print("You're tall but not male")
else:
    print("You are not a male and not tall")

