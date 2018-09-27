#Construct a box by inputting the height and width.

width = int(input("What is the width of your box? "))
height = int(input("What is the height of your box? "))
last_height = height - 1
last_width = width - 1

y = 0
while y <= last_height:
    x = 0
    if 1 <= y < last_height:
        while x <= last_width:
            if 1 <= x < last_width:
                print(" ", end="")
            else:    
                print("*", end="")
            x += 1
    elif y <= last_height:
        x = 0
        while x <= last_width:
            print("*", end="")
            x += 1
    y += 1
    print()
print()

#Reference - 5x5 
# y = 0
# while y <= 4:
#     x = 0
#     if 1 <= y < 4:
#         while x <= 4:
#             if 1 <= x < 4:
#                 print("x", end="")
#             else:    
#                 print(x, end="")
#             x += 1
#     elif y <= 4:
#         x = 0
#         while x <= 4:
#             print(x, end="")
#             x += 1
#     y += 1
#     print()