# Using loop, it will print out odd numbers between 1 and 10 inclusive.

counter_col = 0
while counter_col <= 10:
    if counter_col % 2 != 0:
        print(counter_col)
    counter_col += 1
print()
