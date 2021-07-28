# Import required python libraries
import random
import time
import mysql.connector as sql

# Setup SQL
db = sql.connect(
    host = "localhost",
    user = "root",
    passwd = "qwerty123",
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS python")
cursor.execute("USE python")
cursor.execute("CREATE TABLE IF NOT EXISTS gamble (ID INT(3) PRIMARY KEY NOT NULL, amount BIGINT(255))")

# Global lists
chances = [True, False, False, True, False, False, False, True, False, False]

def new():
    i = random.randint(1,100)
    cursor.execute("SELECT * FROM gamble WHERE ID = %s", (i,))
    record = cursor.fetchall()

    if not record:
        cursor.execute("INSERT INTO gamble VALUES (%s, 10000)", (i,))
        print("Your assigned id is", i, "and you have been granted 10k as beginners' bonus")
        print("===============================================================================================")
    else:
        new()

    # Automatically set player and money
    global player
    global money

    player = i
    cursor.execute("SELECT amount FROM gamble WHERE ID = %s", (player,))
    money = int(cursor.fetchone()[0])

def user():
    global player
    global money

    player = int(input("Enter your user id:  "))
    cursor.execute("SELECT * FROM gamble WHERE ID = %s", (player,))
    record = cursor.fetchall()

    if record:
        cursor.execute("SELECT amount FROM gamble WHERE ID = %s", (player,))
        money = int(cursor.fetchone()[0])
    else:
        print("Player ID doesn't exist")
        print("===============================================================================================")

def gamble(bet):
    global player
    global money
    x = random.randint(0,9)

    if bet <= money:
        if chances[x] == True:
            money += bet
            print(player, "betted", bet, "and brought back", 2*bet)
            print("===============================================================================================")
            cursor.execute("UPDATE gamble SET amount = %s WHERE ID = %s", (money, player))
        else:
            money -= bet
            print(player, "betted", bet, "and lost", bet)
            print("===============================================================================================")
            cursor.execute("UPDATE gamble SET amount = %s WHERE ID = %s", (money, player))
    else:
        print("You can not bet more than you own, your current balance is", money)
        print("===============================================================================================")
    
    if money == 0:
        print("You have no money left, hence you will be executed in")
        for i in range(3,0,-1):
            print(i)
            time.sleep(1)
        cursor.execute("DELETE FROM gamble WHERE ID = %s", (player,))
        print("*POP* Execution complete.")
        print("===============================================================================================")

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
        cursor.execute("SELECT * FROM gamble")
        print(cursor.fetchall())
    elif task == 6:
        db.commit()
        break
    else:
        print("Invalid input!")
