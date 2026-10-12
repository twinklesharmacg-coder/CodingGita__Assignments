# Q58
student_id = input("Enter student ID: ")

parts = student_id.split("-")

branch = parts[2]

if branch == "CSE":
    print("CSE Student")
else:
    print("Non-CSE Student")


# Q59
email = input("Enter email: ")

parts = email.split("@")
domain = parts[1]

if domain == "gmail.com":
    print("Gmail User")
else:
    print("Other Email Provider")


# Q60
name = input("Enter full name: ")

parts = name.split(" ")

first = parts[0]
last = parts[2]

username = first + "." + last

if "." in username:
    print("Valid Username Format")
else:
    print("Invalid Username Format")

# Q61
num = int(input("Enter number: "))

if num >= 0 and num <= 9:
    print("One Digit")
elif num >= 10 and num <= 99:
    print("Two Digits")
elif num >= 100 and num <= 999:
    print("Three Digits")
else:
    print("Four or More Digits")


# Q62
price = int(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total >= 5000:
    discount = 20
elif total >= 2000:
    discount = 10
else:
    discount = 0

discount_amount = total * discount / 100
final_amount = total - discount_amount

print("Total:", total)
print("Discount:", discount, "%")
print("Final Amount:", final_amount)


# Q63
units = int(input("Enter units: "))

if units <= 100:
    rate = 5
elif units <= 300:
    rate = 7
else:
    rate = 10

bill = units * rate

print("Units:", units)
print("Rate:", rate)
print("Bill:", bill)


# Q64
balance = 10000

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Balance:", balance)

    case 2:
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print("New Balance:", balance)

    case 3:
        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance = balance - amount
            print("New Balance:", balance)
        else:
            print("Insufficient Balance")

    case 4:
        print("Exit")

    case _:
        print("Invalid Choice")


# Q65
choice = int(input("Enter item number: "))
quantity = int(input("Enter quantity: "))

match choice:
    case 1:
        price = 250
    case 2:
        price = 150
    case 3:
        price = 200
    case 4:
        price = 120
    case _:
        price = 0
        print("Invalid Choice")

if price != 0:
    total = price * quantity

    if total >= 500:
        discount = total * 10 / 100
    else:
        discount = 0

    final_amount = total - discount

    print("Total:", total)
    print("Discount:", discount)
    print("Final Amount:", final_amount)


# Q66
mark1 = int(input("Enter subject 1 marks: "))
mark2 = int(input("Enter subject 2 marks: "))
mark3 = int(input("Enter subject 3 marks: "))
attendance = int(input("Enter attendance: "))

average = (mark1 + mark2 + mark3) / 3

if attendance >= 75:
    if average >= 90:
        print("Outstanding")
    elif average >= 75:
        print("Very Good")
    elif average >= 60:
        print("Good")
    elif average >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")


# Q67
distance = int(input("Enter distance: "))
ride = input("Enter ride type: ")

match ride:
    case "normal":
        rate = 15
    case "premium":
        rate = 25
    case _:
        rate = 0
        print("Invalid Ride Type")

if rate != 0:
    fare = distance * rate

    if distance > 20:
        fare = fare + (fare * 10 / 100)

    print("Fare:", fare)


# Q68
score = int(input("Enter entrance score: "))
percentage = int(input("Enter 12th percentage: "))
category = input("Enter category: ")

match category:
    case "general":
        if score >= 80 and percentage >= 75:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")

    case "obc":
        if score >= 70 and percentage >= 70:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")

    case "sc":
        if score >= 60 and percentage >= 60:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")

    case _:
        print("Invalid Category")
      # Q69
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


# Q70
marks = int(input("Enter marks: "))

if marks >= 40:
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    else:
        print("Pass")
else:
    print("Fail")
