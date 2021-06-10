# To split the bill in the restaurant and to avoid fights among friends
import random
d = {}

print("Enter the number of friends joining (including you):")
friends = int(input())

if friends <= 0:
    print("\nNo one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for name in range(friends):
        d[input()] = 0

    print("Enter the total bill value:")
    bill = int(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    feature = input()

    list_names = [name for name in d.keys()]
    if feature == 'No':
        print("\nNo one is going to be lucky")

        for key, value in d.items():
            d[key] = round((bill / friends), 2)

    if feature == 'Yes':
        lucky_one = random.choice(list_names)
        print(f'{lucky_one} is the lucky one!')

        for key, value in d.items():
            if key != lucky_one:
                d[key] = round((bill / (friends - 1)), 2)

    print(d)
