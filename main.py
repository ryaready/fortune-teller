# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from random import choice
answer = choice(['yes', 'no', 'maybe'])
satisfied = False
while not satisfied:
    print("Hello, it is I, Aishwarya the psychic, how may I assist you")
    customer = input("I want to know if: ")
    print(answer)
    print("Are you satisfied with the reading?")
    customer_says = input()
    if customer_says == 'yes' or customer_says == 'satisfied':
        satisfied = True
        print('well have a nice day')
    else:
        print("ask again")
    print('\n')