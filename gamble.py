# Import required python libraries
import random
import time

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
    if player in id:
        position = id.index(player)
        money = amount[position]
    else:
        print("Player ID doesn't exist")

def gamble(bet):
    global player
    global money
    x = random.randint(0,9)

    if bet <= money:
        if chances[x] == True:
            money += bet
            print(player, "betted", bet, "and brought back", 2*bet)
            print("===============================================================================================")
            position = id.index(player)
            amount[position] = money
        else:
            money -= bet
            print(player, "betted", bet, "and lost", bet)
            print("===============================================================================================")
            position = id.index(player)
            amount[position] = money
    else:
        print("You can not bet more than you own, your current balance is", money)
        print("===============================================================================================")
    
    if money == 0:
        print("You have no money left, hence you will be executed in")
        for i in range(3,0,-1):
            print(i)
            time.sleep(1)
        target = id.index(player)
        id.pop(target)
        amount.pop(target)
        print("*POP* Execution complete.")

def total():
    global money

    print("You have", str(money), "amount of money.")
    print("===============================================================================================")


while True:
    task = int(input("Enter number corresponding to the preferred task\n1. New user\n2. Change user\n3. Gamble money\n4. Show my total money\n5. Check users / amount\n6. Exit\n=========================>  "))

    if task == 1:
        new()
    elif task == 2:
        user()
    elif task == 3:
        bet = int(input("Enter amount to be betted  "))
        gamble(bet)
    elif task == 4:
        total()
    elif task == 5:
        for i in range(0, len(id)):
            print("ID -", id[i], " & Amount -", amount[i] )
    elif task == 6:
        break
    else:
        print("Invalid input!")
