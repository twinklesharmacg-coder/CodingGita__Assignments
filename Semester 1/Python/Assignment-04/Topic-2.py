# Topic-2 — `if-else` Statements

## Q9. Even or Odd

Take an integer and print whether it is even or odd.

### Test Cases

`24 → Even`  
`17 → Odd`  
`0 → Even`

---Answer:
integer=int(input("Enter your number here:"))
if integer%2==0:
  print("Even")
else:
  print("Odd")
            

## Q10. Pass or Fail

Take marks as input.

If marks are `40` or more, print:

```text
Pass
```

Otherwise print:

```text
Fail
```

### Test Cases

`75 → Pass`  
`40 → Pass`  
`39 → Fail`

---Answer:
marks=int(input("Enter your marks here:"))
if marks >=40:
  print("Pass")
else:
  print("Fail")

## Q11. Adult or Minor

Take age as input.

Print:

```text
Adult
```

if age is `18` or more; otherwise print:

```text
Minor
```

### Test Cases

`21 → Adult`  
`18 → Adult`  
`12 → Minor`

---Answer:
age=int(input("Enter your age here:")
if age>=18:
        print("Adult")
else:
       prinnt("Minor")
        

## Q12. Number Sign

Take an integer and print:

```text
Positive
```

for positive numbers and:

```text
Non-Positive
```

otherwise.

### Test Cases

`15 → Positive`  
`0 → Non-Positive`  
`-7 → Non-Positive`

---Answer:
integer=int(input("Enter the integer here:"))
if n>=0:
  print("positive")
else:
  print("Non-positive")


## Q13. Divisible by 3

Take an integer.

Print:

```text
Divisible by 3
```

or:

```text
Not Divisible by 3
```

### Test Cases

`21 → Divisible by 3`  
`22 → Not Divisible by 3`  
`0 → Divisible by 3`

---Answer:
integer=int(input("Enter the integer :"))
if integer%3==0:
  print("Divisible by 3")
else:
  print("Not Divisible by 3")

## Q14. Login Password

Store the correct password as:

```python
correct_password = "python123"
```

Take a password from the user.

Print:

```text
Login Successful
```

if it matches; otherwise print:

```text
Invalid Password
```

### Test Cases

`python123 → Login Successful`  
`python321 → Invalid Password`

---Answer:
password=input("Enter your password here:")
if password=="python123"
    print("Login Successful")
else:
    print("Invalid Password")

## Q15. Username Check

The valid username is:

```text
admin
```

Take a username as input and print:

```text
Welcome Admin
```

or:

```text
Invalid Username
```

### Test Cases

`admin → Welcome Admin`  
`Admin → Invalid Username`  
`student → Invalid Username`

---Answer:
text=input("Enter the text here:)
if text=="admin"
   print("Welcome Admin")
else:
   print("Invalid Username")

## Q16. Greater Between Two Numbers

Take two integers and print the greater number.

If both numbers are equal, print:

```text
Both are Equal
```

### Test Cases

`15 20 → 20`  
`50 12 → 50`  
`25 25 → Both are Equal`

---Answer:
integer1=int(input("Enter number 1 here:"))
integer2=int(input("Enter number 2 here:"))
if integer1==integer2:
  print("Both are equal")
if integer1>integer2:
     print(integer1)
else:
    print(integer2)
             

## Q17. Hot or Comfortable

Take temperature in Celsius.

If temperature is greater than `30`, print:

```text
Hot
```

Otherwise print:

```text
Comfortable
```

### Test Cases

`35 → Hot`  
`30 → Comfortable`  
`18 → Comfortable`

---Answer:
temp=input("Enter  temp in celsius:")
if temp>30:
  print("Hot")
else:
  print("Comfortable")


## Q18. Shopping Discount Eligibility

A customer receives a discount if the shopping amount is at least `5000`.

Print:

```text
Discount Available
```

or:

```text
No Discount
```

### Test Cases

`7000 → Discount Available`  
`5000 → Discount Available`  
`4999 → No Discount`

---Answer:
amount=("Enter your shopping amount here:")
if amount>5000:
    print("Discount available")
else:
   print("No Discount")
