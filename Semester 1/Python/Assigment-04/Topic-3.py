# Topic-3 — `if-elif-else`

## Q19. Grade Calculator

Take marks and print:

```text
A
B
C
D
F
```

using these ranges:

- `90–100` → A
- `80–89` → B
- `70–79` → C
- `60–69` → D
- Below `60` → F

### Test Cases

`95 → A`  
`84 → B`  
`72 → C`  
`65 → D`  
`40 → F`

---Answer:
marks=int(input("Enter your marks here:"))
if marks>=90:
    print("A")
elif marks>=80 and marks<=89:
    print("B")
elif marks>=70 and marks<=79:
    print("C")
elif marks>=60 and marks<=69:
    print("D")
else:
    print("F")


## Q20. Temperature Category

Take temperature in Celsius.

Print:

```text
Very Hot
Hot
Warm
Cold
```

Rules:

- `40+` → Very Hot
- `30–39` → Hot
- `20–29` → Warm
- Below `20` → Cold

### Test Cases

`45 → Very Hot`  
`35 → Hot`  
`25 → Warm`  
`12 → Cold`

---Answer:
temp=input("Take tempurature in celsius:")
if temp>40:
    print("Very Hot")
elif 30<=temp<=40:
    print("Hot")
elif 29<=temp<=20:
    print("Warm")
else:
    print("Cold")

## Q21. Traffic Signal

Take a traffic signal color.

Print the appropriate instruction:

- `red` → Stop
- `yellow` → Wait
- `green` → Go
- anything else → Invalid Signal

### Test Cases

`red → Stop`  
`yellow → Wait`  
`green → Go`  
`blue → Invalid Signal`

---Answer:

color=("Enter the traffic color:")
if color=="red":
    print("Stop")
elif color=="yellow":
    print("Wait")
elif color=="green":
    print("Go")
elif color=="blue":
    print("Invalid Signal")


## Q22. Electricity Usage Category

Take electricity units.

Print:

- `0–100` → Low Usage
- `101–300` → Medium Usage
- `301–500` → High Usage
- Above `500` → Very High Usage

### Test Cases

`80 → Low Usage`  
`250 → Medium Usage`  
`450 → High Usage`  
`650 → Very High Usage`

---Answer:
units=input("Enter the electricity units here:")
if 0<=units<=100:
    print("Low usage")
elif 101<=units<=300:
    print("Medium usage")
elif 301<=units<=500:
    print("High usage")
else:
    print("Very high usage")


## Q23. Movie Ticket Category

Take age as input.

Print:

- Below `5` → Free Ticket
- `5–12` → Child Ticket
- `13–59` → Regular Ticket
- `60+` → Senior Ticket

### Test Cases

`3 → Free Ticket`  
`10 → Child Ticket`  
`25 → Regular Ticket`  
`65 → Senior Ticket`

---Answer:
age=int(input("Enter your age here:"))
if age<5:
    print("Free ticket")
elif 5<=age<=12:
    print("Child ticket")
elif 13<=age<=59:
    print("Regular Ticket")
else:
    print("Senior Ticket")

## Q24. BMI Category

Take BMI as input.

Print:

- Below `18.5` → Underweight
- `18.5–24.9` → Normal
- `25–29.9` → Overweight
- `30+` → Obese

### Test Cases

`17.8 → Underweight`  
`22.5 → Normal`  
`27.2 → Overweight`  
`31.4 → Obese`

---Answer:
bmi=input("Enter your bmi here:")
if bmi<18.5:
    print("Underweight")
elif 18.5<=bmi<=24.9:
    print("Normal")
elif 25<=bmi<=29.9:
    print("Overweight")
else:
    print("Obese")

## Q25. Month Days

Take a month number.

Print the number of days for:

- `1, 3, 5, 7, 8, 10, 12` → 31 Days
- `4, 6, 9, 11` → 30 Days
- `2` → 28 or 29 Days
- Anything else → Invalid Month

### Test Cases

`1 → 31 Days`  
`4 → 30 Days`  
`2 → 28 or 29 Days`  
`13 → Invalid Month`

---Answer:


## Q26. Simple Calculator

Take two numbers and an operator (`+`, `-`, `*`, `/`).

Perform the selected operation using `if-elif-else`.

### Test Cases

`10 5 + → 15`  
`10 5 - → 5`  
`10 5 * → 50`  
`10 5 / → 2.0`  
`10 5 % → Invalid Operator`

---

## Q27. Day Number

Take a number from `1` to `7`.

Print:

```text
1 → Monday
2 → Tuesday
3 → Wednesday
4 → Thursday
5 → Friday
6 → Saturday
7 → Sunday
```

For any other number, print:

```text
Invalid Day
```

### Test Cases

`1 → Monday`  
`5 → Friday`  
`7 → Sunday`  
`9 → Invalid Day`

---

## Q28. Performance Level

Take a score from `0` to `100`.

Print:

- `90+` → Excellent
- `75–89` → Very Good
- `60–74` → Good
- `40–59` → Average
- Below `40` → Needs Improvement

### Test Cases

`95 → Excellent`  
`82 → Very Good`  
`68 → Good`  
`50 → Average`  
`25 → Needs Improvement`

---

