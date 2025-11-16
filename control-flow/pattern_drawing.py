
size = int(input("Enter the size of the pattern: "))

row = 0

# Outer loop: controls the number of rows
while row < size:
    # Inner loop: prints asterisks for each column in the row
    for col in range(size):
        print("*", end="")
        
    print()
    row += 1
