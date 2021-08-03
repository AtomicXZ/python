# Import required libraries
import mysql.connector as sql
import random

# Setup SQL
db = sql.connect(
    host = "localhost",
    user = "root",
    passwd = "qwerty123",
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS python")
cursor.execute("USE python")
cursor.execute("CREATE TABLE IF NOT EXISTS hotel (cid INT PRIMARY KEY NOT NULL, name VARCHAR(50), address VARCHAR(255), phoneno BIGINT, bill BIGINT)")
cursor.execute("CREATE TABLE IF NOT EXISTS bill (cid INT NOT NULL, item VARCHAR(50), quantity INT, price INT)")
cursor.execute("CREATE TABLE IF NOT EXISTS rooms (cid INT NOT NULL, room INT, room_price INT)")
print(
"""██████████████████████████████████████████████████████████████████████████████████████████
█▄─█▀▀▀█─▄█▄─▄▄─█▄─▄███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄▄─███─▄─▄─█─▄▄─███─█─█─▄▄─█─▄─▄─█▄─▄▄─█▄─▄███
██─█─█─█─███─▄█▀██─██▀█─███▀█─██─██─█▄█─███─▄█▀█████─███─██─███─▄─█─██─███─████─▄█▀██─██▀█
▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▀▀▄▀▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀
""")

def new():
    global cid

    name = input("Enter your name:  ")
    address = input("Enter your address:  ")
    phoneno = int(input("Enter your phone number:  "))
    while True:
        if len(str(phoneno)) != 10:
            print("Incorrect phone number format, does not contain 10 digits!")
            phoneno = int(input("Please enter phone number again:  "))
        else:
            break

    print("**** Generating customer ID for you, please wait ****")
    while True:
        cid = random.randint(1,999)
        cursor.execute("SELECT * FROM hotel WHERE cid = %s", (cid,))
        record = cursor.fetchall()
        if not record:
            print("Your Customer ID is", cid)
            cursor.execute("INSERT INTO hotel VALUES (%s, %s, %s, %s, 0)", (cid, name, address, phoneno))
            break             

def book():
    choice = int(input("What kind of room would you like to book:  \n1. Standard - ₹3000/night\n2. Deluxe - ₹5000/night\n3. Royal - ₹10000/night\n=========================>  "))
    if choice == 1:
        noofrooms = int(input("You have chosen Standard room, please enter quantity of rooms:  "))

        cursor.execute("SELECT * FROM rooms WHERE cid = %s",(noofrooms,))
        count = cursor.fetchall()
        for i in range(1, noofrooms+1):
            roomno = random.randint(1, 300)
            while True:
                roomno = random.randint(1, 300)
                cursor.execute("SELECT * FROM rooms WHERE room = %s", (roomno,))
                result = cursor.fetchall()
                if not result:
                    break
            cursor.execute("INSERT INTO rooms VALUES (%s, %s, 3000)", (cid, roomno))
    elif choice == 2:
        noofrooms = int(input("You have chosen Deluxe room, please enter quantity of rooms:  "))

        cursor.execute("SELECT * FROM rooms WHERE cid = %s",(noofrooms,))
        count = cursor.fetchall()
        for i in range(1, noofrooms+1):
            roomno = random.randint(1, 300)
            while True:
                roomno = random.randint(1, 300)
                cursor.execute("SELECT * FROM rooms WHERE room = %s", (roomno,))
                result = cursor.fetchall()
                if not result:
                    break
            cursor.execute("INSERT INTO rooms VALUES (%s, %s, 5000)", (cid, roomno))
    elif choice == 3:
        noofrooms = int(input("You have chosen Royal room, please enter quantity of rooms:  "))

        cursor.execute("SELECT * FROM rooms WHERE cid = %s",(noofrooms,))
        count = cursor.fetchall()
        for i in range(1, noofrooms+1):
            roomno = random.randint(1, 300)
            while True:
                roomno = random.randint(1, 300)
                cursor.execute("SELECT * FROM rooms WHERE room = %s", (roomno,))
                result = cursor.fetchall()
                if not result:
                    break
            cursor.execute("INSERT INTO rooms VALUES (%s, %s, 10000)", (cid, roomno))
    else:
        print("Invalid choice!")
        book()


def food():
    choice = int(input("Select the course you'd like to order\n1. Breakfast\n2. Lunch\n3. Supper\n4. Dinner\n5. Beverages\n6. Exit\n=========================>  "))

    if choice == 1:
        choice = int(input("What would you like to have for breakfast?\n\n1. Sandwiches - ₹50\n2. Dosa - ₹80\n3. Pav Bhaji - ₹80\n4. Breakfast Thali - ₹200\n=========================>  "))
        if choice == 1:
            order = "Sandwiches"
            p = 50
            q = int(input("Enter quantity:  "))
        elif choice == 2:
            order = "Dosa"
            p = 80
            q = int(input("Enter quantity:  "))
        elif choice == 3:
            order = "Pav Bhaji"
            p = 80
            q = int(input("Enter quantity:  "))
        elif choice == 4:
            order = "Breakfast Thali"
            p = 200
            q = int(input("Enter quantity:  "))
        else:
            print("Invalid choice, redirecting to main ordering page, please order properly this time")
            food()
    elif choice == 2:
        choice = int(input("What would you like to have for lunch?\n\n1. Lunch Thali (veg) - ₹200\n2. Lunch Thali (non-veg) - ₹250\n3. Supreme Thali - ₹300\n4. Supreme non-veg Thali - ₹400\n=========================>  "))
        if choice == 1:
            order = "Lunch Thali (veg)"
            p = 200
            q = int(input("Enter quantity:  "))
        elif choice == 2:
            order = "Lunch Thali (non-veg)"
            p = 250
            q = int(input("Enter quantity:  "))
        elif choice == 3:
            order = "Supreme Thali"
            p = 300
            q = int(input("Enter quantity:  "))
        elif choice == 4:
            order = "Supreme non-veg Thali"
            p = 400
            q = int(input("Enter quantity:  "))
        else:
            print("Invalid choice, redirecting to main ordering page, please order properly this time")
            food()
    elif choice == 3:
        choice = int(input("What would you like to have for supper?\n\n1. Hakka Noddles - ₹80\n2. Cheese Sandwiches (2) - ₹50\n3. French Fries - ₹40\n4. Snack Paradise - ₹200\n=========================>  "))
        if choice == 1:
            order = "Hakka Noddles"
            p = 80
            q = int(input("Enter quantity:  "))
        elif choice == 2:
            order = "Cheese Sandwiches"
            p = 50
            q = int(input("Enter quantity:  "))
        elif choice == 3:
            order = "French Fries"
            p = 40
            q = int(input("Enter quantity:  "))
        elif choice == 4:
            order = "Snack Paradise"
            p = 200
            q = int(input("Enter quantity:  "))
        else:
            print("Invalid choice, redirecting to main ordering page, please order properly this time")
            food()
    elif choice == 4:
        choice = int(input("What would you like to have for dinner?\n\n1. Dinner Thali (veg) - ₹200\n2. Dinner Thali (non-veg) - ₹250\n3. Supreme Thali - ₹300\n4. Supreme non-veg Thali - ₹400\n=========================>  "))
        if choice == 1:
            order = "Dinner Thali (veg)"
            p = 200
            q = int(input("Enter quantity:  "))
        elif choice == 2:
            order = "Dinner Thali (non-veg)"
            p = 250
            q = int(input("Enter quantity:  "))
        elif choice == 3:
            order = "Supreme Thali"
            p = 300
            q = int(input("Enter quantity:  "))
        elif choice == 4:
            order = "Supreme non-veg Thali"
            p = 400
            q = int(input("Enter quantity:  "))
        else:
            print("Invalid choice, redirecting to main ordering page, please order properly this time")
            food()
    elif choice == 5:
        choice = int(input("What beverage would you like to have?\n\n1. Cold Drink - ₹40\n2. Mineral Water - ₹20\n3. Milk Shake - ₹60\n4. Smoothie - ₹60\n=========================>  "))
        if choice == 1:
            order = "Cold Drink"
            p = 40
            q = int(input("Enter quantity:  "))
        elif choice == 2:
            order = "Mineral Water"
            p = 20
            q = int(input("Enter quantity:  "))
        elif choice == 3:
            order = "Milk Shake"
            p = 60
            q = int(input("Enter quantity:  "))
        elif choice == 4:
            order = "Smoothie"
            p = 60
            q = int(input("Enter quantity:  "))
        else:
            print("Invalid choice, redirecting to main ordering page, please order properly this time")
            food()
    elif choice == 6:
        print("Returning to main menu.")
    else:
        print("Invalid choice, redirecting to main ordering page, please order properly this time")
        food()

    if choice != 6:
        cursor.execute("SELECT * FROM bill WHERE item = %s AND cid = %s", (order, cid))
        record = cursor.fetchall()

        if not record:
            cursor.execute("INSERT INTO bill VALUES (%s, %s, %s, %s)", (cid, order, q, p*q))
        else:
            cursor.execute("SELECT quantity FROM bill WHERE item = %s", (order,))
            q += int(cursor.fetchone()[0])
            cursor.execute("UPDATE bill SET quantity = %s, price = %s WHERE cid = %s AND item = %s", (q, p*q, cid, order))


def calcbill():

    bill = 0
    cursor.execute("SELECT cid, name FROM hotel WHERE cid = %s", (cid,))
    i = cursor.fetchone()
    print("You are " + str(i[1]) + " [ ID - " + str(i[0]) + " ] " + "and your bill is:\n")

    cursor.execute("SELECT room, room_price FROM rooms WHERE cid = %s", (cid,))
    print("Room bill:\nRoom\t\tPrice")
    l = cursor.fetchall()
    for i in l:
        print(str(i[0])+"\t\t"+str(i[1]))
        bill += i[1]

    cursor.execute("SELECT item, quantity, price FROM bill WHERE cid = %s", (cid,))
    other_commodities =  cursor.fetchall()
    print("\nOther commodities:")
    for i in other_commodities:
        print("Item name :",i[0])
        print("Quantity :",i[1])
        print("Total price : Rs.",i[2])
        bill += i[2]

    print("\nTotal bill - ₹" + str(bill))
    cursor.execute("UPDATE hotel SET bill = %s WHERE cid = %s", (bill, cid))

while True:
    task = int(input("Please select one of the following\n1. Create a new Customer ID\n2. Enter an existing Customer ID\n=========================>  "))
    if task == 1:
        new()
        break
    elif task == 2:
        cid = int(input("Please enter your Customer ID:  "))
        break
    else:
        print("Invalid input!")

while True:
    task = int(input("Enter number corresponding to the preferred task\n1. New Customer\n2. Change Customer ID\n3. Book Room\n4. Order food\n5. Calculate Bill\n6. Exit\n=========================>  "))

    if task == 1:
        new()
    elif task == 2:
        cid = int(input("Please enter your Customer ID:  "))
    elif task == 3:
        book()
    elif task == 4:
        food()
    elif task == 5:
        calcbill()
    elif task == 6:
        calcbill()
        db.commit()
        break
    else:
        print("Invalid input!")
