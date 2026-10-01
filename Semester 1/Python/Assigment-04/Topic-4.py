# Topic-4 — Logical Conditions

## Q29. College Admission Eligibility

A student is eligible if:

- marks are at least `60`, **and**
- attendance is at least `75`.

Take both values and print:

```text
Eligible
```

or:

```text
Not Eligible
```

### Test Cases

`70 80 → Eligible`  
`70 70 → Not Eligible`  
`55 90 → Not Eligible`

---Answer:
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))

if marks >= 60 and attendance >= 75:
    print("Eligible")
else:
    print("Not Eligible")

## Q30. Scholarship Eligibility

A student gets a scholarship if marks are at least `85` **or** family income is below `300000`.

Take marks and income.

### Test Cases

`90 500000 → Scholarship Available`  
`70 250000 → Scholarship Available`  
`70 500000 → No Scholarship`

---Answer:
marks = int(input("Enter marks: "))
income = int(input("Enter income: "))

if marks >= 85 or income < 300000:
    print("Scholarship Available")
else:
    print("No Scholarship")

## Q31. Weekend Check

Take a day name.

If it is `Saturday` or `Sunday`, print:

```text
Weekend
```

Otherwise print:

```text
Weekday
```

### Test Cases

`Saturday → Weekend`  
`Sunday → Weekend`  
`Monday → Weekday`

---Answer:
day = input("Enter day: ")

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")  

## Q32. Online Exam Access

A student can access an exam if:

- username is `"student"`, and
- password is `"python123"`.

Print:

```text
Access Granted
```

or:

```text
Access Denied
```

### Test Cases

`student python123 → Access Granted`  
`student wrong123 → Access Denied`  
`admin python123 → Access Denied`

---Answer:
username = input("Enter username: ")
password = input("Enter password: ")

if username == "student" and password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

## Q33. Delivery Availability

A delivery is available if the city is `"Ahmedabad"` or `"Gandhinagar"`.

### Test Cases

`Ahmedabad → Delivery Available`  
`Gandhinagar → Delivery Available`  
`Surat → Delivery Unavailable`

---Answer:
city = input("Enter city: ")

if city == "Ahmedabad" or city == "Gandhinagar":
    print("Delivery Available")
else:
    print("Delivery Unavailable")

## Q34. Number Range Check

Take an integer.

Print `Inside Range` if the number is between `10` and `50`, inclusive. Otherwise print `Outside Range`.

### Test Cases

`10 → Inside Range`  
`35 → Inside Range`  
`50 → Inside Range`  
`55 → Outside Range`

---anaswer:
num = int(input("Enter number: "))

if num >= 10 and num <= 50:
    print("Inside Range")
else:
    print("Outside Range")

## Q35. Secure Transaction

A transaction is allowed only when:

- amount is at most `50000`, and
- OTP entered is `"1234"`.

### Test Cases

`25000 1234 → Transaction Approved`  
`60000 1234 → Transaction Declined`  
`25000 9999 → Transaction Declined`

---Answer:
amount = int(input("Enter amount: "))
otp = input("Enter OTP: ")

if amount <= 50000 and otp == "1234":
    print("Transaction Approved")
else:
    print("Transaction Declined")
