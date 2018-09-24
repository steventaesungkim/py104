#This will tally up the number of coins each time you say "yes."
#It will stop running once you say "no."

coin = 0
statement = "You have %d coins. " % (coin)
stop = "Bye! "

print(statement)
answer = (input("Do you want another coin? ")).upper()


while answer == "YES":
    coin += 1
    statement = "You have %d coins. " % (coin)
    print(statement)
    answer = (input("Do you want another coin? ")).upper()
print(stop)




# if question.upper() == "NO":
#     while question.upper == "YES":
#         print(question)
#         coin += 1
#         if question.upper == "NO":
#             print(stop)
# print(stop)








# coin = 0
# statement = "You have 0 coins."


# print(statement)
# question = input("Do you want another coin? ")
# yes_add_coin.upper() == "YES"
# no_add_coin.upper() == "NO"



# stop = input("Bye! ")

# if yes_add_coin != no_add_coin:
#     while yes_add_coin == no_add_coin:
#         coin += 1
#         if yes_add_coin != no_add_coin:
#             print(stop)
#         print(question)
# print(stop)


#################################

#g(x)
# if yes_add_coin != no_add_coin:
# stop
#
# f(x)
# while yes == no:
#   coin += 1  
#       if yes != no
#       print stop
#   print question
# stop
