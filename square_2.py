# Enter a number and a square will be created according to the number you have entered.


num = int(input("Pick a number to create the size of your square: "))
row = 0

while row < num:
    col = 0
    while col < num:
        print("*", end="")
        col += 1
    row += 1
    print()



