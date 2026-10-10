# Level 8 — Real-Life Single-Loop Problems

## Q62. Daily Expense Analyzer

Take the number of days and then enter the expense for each day. Using one `for` loop, calculate:

- total expense
- highest expense
- lowest expense

### Test Case

```text
Input: 5
Expenses: 250 180 400 120 300
```

### Expected Output

```text
Total: 1250
Highest: 400
Lowest: 120
```

---Answer:

days = int(input("Enter no of days:"))
total = 0
highest_expense = lowest_expense = None
for i in range(days):
    expense = int(input())
    if i == 0:
        highest_expense = lowest_expense = expense
    if expense>highest_expense:
        highest_expense = expense
    elif expense<lowest_expense:
        lowest_expense=expense
    total+=expense
print(f"Total: {total}")
print(f"Highest: {highest_expense}")
print(f"Lowest: {lowest_expense}")                                                                          

## Q63. Student Marks Analyzer

Take the number of subjects and enter marks one by one. Using one `for` loop, calculate:

- total marks
- average marks
- highest marks
- lowest marks

### Test Case

```text
Input: 5
Marks: 78 65 92 81 74
```

### Expected Output

```text
Total: 390
Average: 78.0
Highest: 92
Lowest: 65
```

---Answer:
 num_subjects = int(input())
total_marks = average_marks = highest_marks = 0
lowest_marks = 999
for i in range(num_subjects):
    marks = int(input())
    total_marks+= marks
    if marks>highest_marks:
        highest_marks = marks
    elif marks<lowest_marks:
        lowest_marks= marks
average_marks = total_marks / num_subjects
print(f"Total: {total_marks}")
print(f"Average: {average_marks}")
print(f"Highest: {highest_marks}")
print(f"Lowest: {lowest_marks}")                                                                

## Q64. Attendance Analyzer

Take the number of working days. For each day, input `P` for Present or `A` for Absent. Count present days, absent days, and calculate attendance percentage.

### Test Case

```text
Input: 6
Status: P P A P A P
```

### Expected Output

```text
Present: 4
Absent: 2
Attendance: 66.67%
```

---Answer:
working_days = int(input("Enter no of days:"))
count_present = count_absent = 0
for i in range(working_days):
    attendance = input()
    if attendance == "P":
        count_present+=1
    elif attendance == "A":
        count_absent+=1
attendance__percentage = (count_present / working_days) * 100
print(f"Present: {count_present}")
print(f"Absent: {count_absent}")
print(f"Attendance: {attendance__percentage:.2f}%")

## Q65. Electricity Usage Analyzer

Take the number of days and the electricity units used each day. Calculate total units and the number of days where usage was above `10` units.

### Test Case

```text
Input: 5
Units: 8 12 15 7 13
```

### Expected Output

```text
Total Units: 55
Days Above 10: 3
```

---Answer:
number_of_days = int(input("Enter the no of days:"))
total_units = number_of_high_usage_days = 0
for i in range(number_of_days):
    units = int(input())
    total_units+=units
    if units > 10:
        number_of_high_usage_days+=1
print("Total Units:", total_units)
print("Days Above 10:", number_of_high_usage_days)

## Q66. Shopping Bill Analyzer

Take the number of products and their prices. Using one `for` loop, calculate the total bill and count how many products cost more than `1000`.

### Test Case

```text
Input: 5
Prices: 450 1200 800 2500 600
```

### Expected Output

```text
Total Bill: 5550
Products Above 1000: 2
```

---Answer:
number_of_products = int(input("Enter no of products:"))
total_bill = number_of_expensive_products = 0
for i in range(number_of_products):
    price = int(input())
    total_bill+=price
    if price > 1000:
        number_of_expensive_products+=1
print("Total Bill:", total_bill)
print("Products Above 1000:", number_of_expensive_products)


        
## Q67. Login Attempt Analyzer

Take `N` login attempts. For each attempt, input `success` or `failed`. Count successful and failed attempts and calculate the success percentage.

### Test Case

```text
Input: 5
Attempts: success failed success failed success
```

### Expected Output

```text
Successful: 3
Failed: 2
Success Rate: 60.0%
```

---Answer:
N = int(input("Enter the N here:"))
attempt = input("Enter here:")
count_success = count_failed = 0
for i in range(N):
    if attempt == "success":
        count_success+=1
    elif attempt == "failed":
        count_failed+=1
success_percentage = (count_success / N) * 100
print(f"Successful: {count_success}")
print(f"Failed: {count_failed}")
print(f"Success Rate: {success_percentage:.1f}%")
