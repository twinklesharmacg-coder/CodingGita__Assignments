# Q36
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "admin123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")


# Q37
age = int(input("Enter age: "))
test = input("Enter test status: ")

if age >= 18:
    if test == "pass":
        print("License Approved")
    else:
        print("Test Not Passed")
else:
    print("Age Not Eligible")


# Q38
balance = int(input("Enter balance: "))
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    if amount % 100 == 0:
        print("Withdrawal Successful")
    else:
        print("Enter amount in multiples of 100")
else:
    print("Insufficient Balance")


# Q39
…
[11:32, 30/09/2026] Preya Cg: # Q44
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a > b:
    if a > c:
        print("A is Greatest")
    else:
        print("C is Greatest")
else:
    if b > c:
        print("B is Greatest")
    else:
        print("C is Greatest")


# Q45
attendance = int(input("Enter attendance: "))
marks = int(input("Enter marks: "))

if attendance >= 75:
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    elif marks >= 60:
        print("C")
    elif marks >= 40:
        print("D")
    else:
        print("F")
else:
    print("Not Eligible")


# Q46
salary = int(input("Enter salary: "))
rating = int(input("Enter rating: "))

if salary >= 30000:
    if rating >= 4:
        print("Bonus: 20%")
      
    elif rating >= 3:
        print("Bonus: 10%")
    else:
        print("Bonus: 5%")
else:
    print("No Bonus")


# Q47
age = int(input("Enter age: "))
passenger = input("Enter passenger type: ")
distance = int(input("Enter distance: "))

if age < 5:
    print("Free")
elif age >= 60:
    print("Senior Passenger")
else:
    if passenger == "regular":
        if distance <= 10:
            print("Regular Fare")
        else:
            print("Long Distance Fare")
    else:
        print("Normal Passenger")


# Q48
stock = int(input("Enter stock: "))
payment = input("Enter payment status: ")

if stock > 0:
    if payment == "paid":
        print("Order Confirmed")
    elif payment == "pending":
        print("Payment Pending")
    else:
        print("Invalid Payment Status")
else:
    print("Out of Stock")


# Q49
age = int(input("Enter age: "))
passenger = input("Enter passenger type: ")
ticket = input("Enter ticket type: ")

if age >= 60:
    print("Senior Passenger")
elif age >= 18:
    if passenger == "regular":
        if ticket == "AC":
            print("AC Ticket")
        elif ticket == "Sleeper":
            print("Sleeper Ticket")
        else:
            print("Invalid Ticket")
    else:
        print("General Passenger")
else:
    print("Child Passenger")
