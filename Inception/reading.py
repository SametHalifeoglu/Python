cities_file = open("cities.txt", "r")
print(cities_file.readable())
print(cities_file.read())
cities_file.close()

print("---------------------------------------")

cities_file = open("cities.txt", "r")
print(cities_file.readline())
cities_file.close()

print("---------------------------------------")

cities_file = open("cities.txt", "r")
print(cities_file.readline())
print(cities_file.readline())
print(cities_file.readline())
cities_file.close()

print("---------------------------------------")

cities_file = open("cities.txt", "r")
print(cities_file.readlines())
cities_file.close()

print("---------------------------------------")

cities_file = open("cities.txt", "r")
print(cities_file.readlines()[4])
cities_file.close()

print("---------------------------------------")

cities_file = open("cities.txt", "r")
for city in cities_file.readlines():
    print(city)

print("---------------------------------------")





