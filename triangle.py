#Building a triangle with a determine height

#7x5
y = 0
while y <= 6:
    x = 0
    if 1 <= y < 6:
        while x <= 4:
            if 1 <= x < 4:
                print("x", end="")
            else:    
                print(x, end="")
            x += 1
    elif y <= 6:
        x = 0
        while x <= 4:
            print(x, end="")
            x += 1
    y += 1
    print()

#### NOT COMPLETED
