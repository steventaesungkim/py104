#You will be able to determine the start and end of a sequence while using a loop.


begin = int(input("Pick a number to start: "))
end = int(input("Pick a number to end: "))

counter_col = begin
while counter_col <= end:
    print(counter_col)
    counter_col += 1
print()



##For loop example
counter_col = begin
num = range(begin, (end + 1), -1)

for counter_col in num:
    print(counter_col)
print()

