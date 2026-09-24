Q60. Student Result Information
Take:

Student name
Three subject marks
Calculate:

Total
Average
Display the student's information using an f-string.

Test Case
Input:
Rahul
70 80 90
Expected:

Name: Rahul
Total: 240
Average: 80.00
Use:

input()
.split()
Type casting
Arithmetic operators
f-strings


---Answers:

name=input("Enter your name:")
marks1,marks2,marks3=input("Enter your 3 subjects marks:").split()

marks11=int(marks1)
marks22=int(marks2)
marks33=int(marks3)
Total=marks11+marks22+marks33
average=total/3
print(f"Name: {name} \n Total: {Total} \n Average:{average}")


Q61. Student ID Analyzer
A student enters:

BTECH-24-CSE-105
Write a program that:

Takes the ID as input.
Uses .split("-") to separate the parts.
Displays:
Degree
Batch
Branch
Roll Number
Uses string slicing to extract the last three characters from the original ID.
Converts the roll number into an integer.
Prints the roll number.
Test Case
Input:
BTECH-24-CSE-105
Expected:

Degree: BTECH
Batch: 24
Branch: CSE
Roll Number: 105

--Answers:
id=input("Enter your id here:")
degree,batch,branch,roll_number=id.spilt(-)
  print("Degree: {degree}  Batch: {batch} Branch: {branch}  Roll number: {roll_number})

Q62.Take a three-word full name:

Rahul Kumar Sharma
Use .split() and string indexing/slicing to create:

rahul.sharma
Think carefully about:

.split()
Indexing
Slicing
String concatenation
Do not use any conditional statement.

---Answers:
full_name = "Rahul Kumar Sharma"
words = full_name.split()


first_name = words[0]
last_name = words[2]
username = first_name.lower() + "." + last_name.lower()

print(username)

# Output: rahul.sharma

Q63. Sentence Information
Take:

Python is very powerful
as input.

Use .split() and string indexing to display:

First word: Python
Last word: powerful
Also display the number of words.

--Answer:
text=input("Enter your text here:")
words=text.split()
print("First word: " ,words[0])
print("Last word: " ,words[-1])

Q64. Email Analyzer + Membership
Take an email address as input.

Use:

Membership operator to check for "@"
.split("@")
String operations
For the input:

rahul@gmail.com
display:

@ Present: True
Username: rahul
Domain: gmail.com

---Answer:

email = input("Enter the email address: ")
has_at_symbol = "@" in email

# Display the required output
print(f"@ Present: {has_at_symbol}")

if has_at_symbol:
    username, domain = email.split("@", 1)
    
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Invalid email format: Missing '@' symbol.")

Q65. Character Analyzer
Take one character from the user.

Display:

Character
Unicode code point
Previous character
Next character
Use ord() and chr().

Test Case
Input:
B
Expected:

Character: B
Code: 66
Previous: A
Next: C

--Answer:
char=input("enter the character here :")
print("Character:",char)
code=ord(char)
print("Code:",code)
previous=code-1
previous_letter=chr(previous)
print("Previous: ",previous_letter)
next=code+1
next_letter=chr(next)
print("Next:",next_letter)


Q66. Product Bill
Take:

Product name
Price
Quantity
Discount percentage
Calculate:

Subtotal = price × quantity
Discount = subtotal × discount_percentage / 100
Final Total = subtotal - discount
Display the values using an f-string with two decimal places.

Test Case
Product: Pen
Price: 20
Quantity: 5
Discount: 10
Expected:

Product: Pen
Price: 20.00
Quantity: 5
Subtotal: 100.00
Discount: 10.00
Final Total: 90.00

---Answer:

product_name=input("Enter your product name:")
price=input("Enter the price here :")
quantity=input("Enter the quantity here :")
discount_percentage=("Enter discount percentage :")
subtotal=price*quantity
discount=subtotal*discount_percentage/100
final_total=subtotal-discount

print("Product:",product_name)
print("Price:",price)
print("quantity:",quantity)
print("Discount:",discount_quantity)
print("Subtotal:",subtotal)
print("Final Total :",final_total)


Q67. Date Analyzer
Take a date in this format:

09-09-2026
Use .split("-") to separate:

Day
Month
Year
Display:

Day: 09
Month: 09
Year: 2026
Then use string slicing on the original input to extract:

2026


--Answer:
date=input("Enter your date here:").split("-")
day=date[0]
month=date[1]
year=date[2]
print("Day:",day)
print("Month:",month)
print("Year:",year)



Q68. String Transformation Challenge
Take:

Python Programming
as input.

Use .split() and slicing to display:

First Word: Python
Second Word: Programming
First Word Reversed: nohtyP
Second Word Reversed: gnimmargorP


--Answer:
text=input("Enter your text here:")
words=text.split()
word1=words[0]
word2=words[1]

print("First Word :",word1)
print("Second word:",word2)
print ("First Word Reversed: ",word1[::-1])
print("Second word Reversed: "'word2[::-1])

Q69. Final Challenge — Student Code Formatter
A student enters:

BTECH-2026-CSE-105
Create a formatted output:

Degree: BTECH
Batch: 2026
Branch: CSE
Roll: 105
Code: BTECH/CSE/105
Requirements:

Use .split("-").
Use string indexing to access the required parts.
Use string slicing where appropriate.
Use string concatenation or an f-string for the final Code.
Do not manually write the extracted values.
Test Case
Input:
BTECH-2026-CSE-105
Expected:

Degree: BTECH
Batch: 2026
Branch: CSE
Roll: 105
Code: BTECH/CSE/105


--Answer:
text=input("Enter your id here:")
texte=text.spilt("-")
degree=texte[0]
batch=texte[1]
branch=texte[2]
roll=texte[3]
print("Degree:",degree)
print("Batch:",batch)
print("Roll:",branch)
print(f"Code: {degree}/{branch}/{roll}")

   
Q70. Final String + Input/Output Challenge
Take a full name from the user in this format:

Rahul Kumar Sharma
Create the following output:

Original: Rahul Kumar Sharma
First Name: Rahul
Last Name: Sharma
First Name (Upper Part): RAH
Last Name (Lower Part): har
Full Name Reversed: amrahS ramuK luhaR
Requirements:

Use input().
Use .split() to separate the words.
Use indexing to access the first and last name.
Use slicing to create the required parts.
Use [::-1] to reverse the complete original string.
Use an f-string for the final output.
Do not manually write the extracted values.
Test Case
Input:
Rahul Kumar Sharma
Expected:

Original: Rahul Kumar Sharma
First Name: Rahul
Last Name: Sharma
First Name (Upper Part): RAH
Last Name (Lower Part): har
Full Name Reversed: amrahS ramuK luhaR

---Answer:
name=input("Enter your name here:")
words=name.split()
first_name=name[0]
Last_name=name[-1]
first_name_part=first_name[0:3]
first_name_upper_part=first_name_part.upper()
last_name_part=last_name[1:4]
last_name_lower_part=last_name_part.lower()
full_name_reversed=name[::-1]
print("Original:",name)
print("First Name:",first_name)
print("Last Name:",last_name)
print("First name (upper part):",first_name_upper_part)
print("Last name (lower part):",last_name_lower_part)
print("Full name Reversed:",full_name_reversed)
