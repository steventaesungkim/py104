#You will be able to determine the start and end of a sequence while using a loop.


start = int(input("Pick a number to start: "))
end = int(input("Pick a number to end: "))

counter_col = start
while counter_col <= end:
    print(counter_col)
    counter_col += 1
print()
