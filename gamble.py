import random

# Global lists
chances = [True, False, False, True, False, False, False, True, False, False]
id = []
amount = []

def new():
    i = random.randint(1,100)

    if i in id:
        new()
    else:
        id.append(i)
        amount.append(int(10000))
        print("Your assigned id is", i, "and you have been granted 10k as beginners' bonus")
        print("===============================================================================================")

    # Automatically set player and money
    global player
    global money

    player = i
    position = id.index(player)
    money = amount[position]


def user():
    global player
    global money

    player = int(input("Enter your user id:  "))
    position = id.index(player)
    money = amount[position]


def gamble(bet):
    global player
    global money
    x = random.randint(0,9)

    if bet <= money:
        if chances[x] == True:
            money += bet
            print(player, "betted", bet, "and brought back", 2*bet)
            print("===============================================================================================")
        else:
            money -= bet
            print(player, "betted", bet, "and lost", bet)
            print("===============================================================================================")
    else:
        print("You can not bet more than you own, your current balance is", money)
        print("===============================================================================================")


def total():
    global money

    print("You have", str(money), "amount of money.")
    print("===============================================================================================")


while True:
    task = int(input("Enter number corresponding to the preferred task\n1. New user\n2. Change user\n3. Gamble money\n4. Show my total money\n5. Exit\n=========================>  "))

    if task == 1:
        new()
        continue
    elif task == 2:
        user()
        continue
    elif task == 3:
        bet = int(input("Enter amount to be betted  "))
        gamble(bet)
        continue
    elif task == 4:
        total()
        continue
    elif task == 5:
        break
    else:
        print("Invalid input!")
        continue
