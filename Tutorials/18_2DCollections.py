# 2D collections = a collection inside another collection
# works like a grid/matrix with rows and columns
# access with [row][column]

our2dcollection = [["apple", "banana", "pineapple", "berry"],
                   ["pizza", "momos", "fries"],
                   ["burger", "potatoes", "tawsif"]]

# access specific element
print(our2dcollection[0][2])    # pineapple - row 0, column 2
print(our2dcollection[2][2])    # tawsif    - row 2, column 2

# print each row as a list
for collection in our2dcollection:
    print(collection)

# print without brackets in row column format
for collection in our2dcollection:
    for food in collection:
        print(food, end=" ")   # space between elements
    print()                    # new line after each row

# 2D list with same size rows - proper matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matrix[1][1])   # 5 - center element

for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
# 1 2 3
# 4 5 6
# 7 8 9

# same concept works with tuples
our2dtuple = (("apple", "banana", "pineapple"),
              ("pizza", "momos", "fries"))

print(our2dtuple[0][1])   # banana

# basic CP usage (optional)
# n, m = map(int, input().split())
# grid = []
# for _ in range(n):
#     row = list(map(int, input().split()))
#     grid.append(row)
# print(grid[i][j])   # access element at row i, column j