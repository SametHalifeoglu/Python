

script = ""
for i in input("Give a parameter: "):

    if i == "." or i == ",":
        script = script + "\n"
    else:
        script = script + str(i)

print(script)

print(".....................................................................")

regex_pattern = "[.,]"  # Do not delete 'r'.

import re

print("\n".join(re.split(regex_pattern, input("Give a parameter: "))))
print(".....................................................................")

print(*filter(None, re.split(regex_pattern, input("Give a parameter: "))), sep="\n")


