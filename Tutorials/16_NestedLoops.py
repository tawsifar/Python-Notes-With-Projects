# nested loops = a loop inside another loop
# outer loop runs once, inner loop completes fully, then outer moves to next iteration

# how end works in print
for x in range(1, 10):
    print(x, end=" ")   # stays on same line, replaces default newline with space
print()                 # manual line break after loop
# output: 1 2 3 4 5 6 7 8 9

# basic nested loop
for x in range(3):          # outer loop runs 3 times
    for y in range(1, 10):  # inner loop runs 9 times per outer iteration
        print(y, end=" ")
    print()                 # line break after each inner loop completes
# output:
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9

# user defined grid
rows   = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
sign   = input("Enter the sign: ")

for x in range(rows):
    for y in range(column):
        print(sign, end="")  # end="" means no space or newline between signs
    print()                  # move to next line after each row

# multiplication table using nested loops
print("\nMultiplication Table:")
for i in range(1, 6):         # rows 1 to 5
    for j in range(1, 6):     # columns 1 to 5
        print(f"{i*j:4}", end="")   # :4 keeps columns evenly spaced
    print()

# basic CP usage (optional)
# nested loops are common in CP for grid/matrix problems
# for i in range(n):
#     for j in range(m):
#         grid[i][j] = int(input())   # reading a 2D grid
# be careful with time complexity, O(n^2) can be slow for large n in CP