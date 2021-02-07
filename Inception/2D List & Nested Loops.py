number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print("*****************************")

print(number_grid[1][2])
print(number_grid[2][0])

print("*****************************")

for row in number_grid:
    print(row)
    for col in range(len(row)):
        print(col)

print("*****************************")
for row in number_grid:
    for col in row:
        print(col)


