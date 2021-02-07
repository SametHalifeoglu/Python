# a = Append (text dosyasına ekleme yapar)

cities_file = open("cities.txt", "a")
print(cities_file.readable())
print(cities_file.writable())
cities_file.close()

print("---------------------------------------")

cities_file = open("cities.txt", "a")
cities_file.write("Budapest")
cities_file.close()

print("---------------------------------------")

cities_file = open("cities.txt", "r")
print(cities_file.read())
cities_file.close()

print("----------------Append new line-----------------------")

cities_file = open("cities.txt", "a")
cities_file.write("\nBaku")
cities_file.close()

# w=Write (text dosyasının içinde ne olduğuna bakmadan üzerine yazar.)

print("---------------Overwrite------------------------")

cities_file = open("cities.txt", "w")
cities_file.write("Baku")
cities_file.close()
cities_file = open("cities.txt", "r")
print(cities_file.read())
cities_file.close()

print("---------------Creating new files------------------------")

cities_file = open("cities1.txt", "w")
cities_file.write("Baku")
cities_file.close()

print("---------------------------------------")

cities_file = open("cities1.txt", "w")
cities_file.write("Baku")
cities_file.close()

print("---------------------------------------")

cities_file = open("index.html", "w")
cities_file.write("<p>This is HTML</p>")
cities_file.close()
cities_file = open("index.html", "r")
print(cities_file.read())
cities_file.close()


