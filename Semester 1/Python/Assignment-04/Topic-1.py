# Topic-1 — Basic `if` Statements

## Q1. Positive Number

Take an integer as input.

If the number is positive, print:

```text
Positive Number
```

Otherwise, print nothing.

### Test Cases

`8 → Positive Number`  
`-4 → No output`  
`0 → No output`

---
number=int(input("Enter your number here:"))
if number>0:
        print("positive")
else:
           print(" ")
          
           

## Q2. Voting Eligibility Check

Take a person's age as input.

If the age is `18` or more, print:

```text
Eligible to Vote
```

### Test Cases

`18 → Eligible to Vote`  
`25 → Eligible to Vote`  
`16 → No output`

---Answer:
age=int(input("Enter your age here:"))
if age>=18:
  print("Eligible to vote")
else:
  print("")

## Q3. Temperature Warning

Take the temperature in Celsius.

If the temperature is greater than `40`, print:

```text
High Temperature
```

### Test Cases

`42 → High Temperature`  
`40 → No output`  
`25 → No output`

---Answer:
temp=input("Enter the temperature in celsius here:")
if temp>40:
  print("High  temperature")
else:
  print("")
  

## Q4. Divisible by 5

Take an integer.

If it is divisible by `5`, print:

```text
Divisible by 5
```

### Test Cases

`25 → Divisible by 5`  
`42 → No output`  
`100 → Divisible by 5`

---Answer:
integer=int("enter the integer here:")
if integer%5==0:
  print("Divisible by 5")
else:
  print("")
            

## Q5. Free Delivery

An online store gives free delivery when the order amount is `1000` or more.

Take the order amount and print:

```text
Free Delivery
```

when the condition is satisfied.

### Test Cases

`1200 → Free Delivery`  
`1000 → Free Delivery`  
`799 → No output`

---Answer:
amount=int(input("Enter the order amount:))
if amount>=1000:
      print("Free delivery")
else:
      print("")
                 

## Q6. Character Check

Take one character as input.

If the character is `"A"`, print:

```text
You entered A
```

### Test Cases

`A → You entered A`  
`B → No output`

---Answer:
character=input("Enter")
if character=="A"
    print("You entered'A'")
else:
    print("")

## Q7. Password Length Check

Take a password as input.

If its length is at least `8`, print:

```text
Strong Length
```

### Test Cases

`python123 → Strong Length`  
`hello → No output`  
`college2026 → Strong Length`

---Answer:
pasword=input("Enter your password:")
if len(password)==8:
    print("Strong Password")
else:
    print("")

## Q8. Number of Digits

Take an integer.

If the number is between `100` and `999`, print:

```text
Three Digit Number
```

### Test Cases

`250 → Three Digit Number`  
`99 → No output`  
`1000 → No output`

---Answer:
integer=int(input("Enter the integer here:")
if 100=<integer=<999:
    print("Three Digit  Number")
else:
print("")
