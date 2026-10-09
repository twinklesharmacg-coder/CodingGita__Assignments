# Level 4 — Number & Digit Logic

## Q23. Count Digits Using a Loop

Take a positive integer and count its digits using a `for` loop. Do not convert the number to a string.

### Test Cases

```text
Input: 58321 | Output: 5
Input: 904 | Output: 3
```

---Answer:
import math
N = int(input())
count = 0
for i in range(int(math.log10(N))+1):
    count+=1
print(count)



## Q24. Sum of Digits

Take an integer and find the sum of its digits using one `for` loop.

### Test Cases

```text
Input: 58321 | Output: 19
Input: 907 | Output: 16
```

---Answer:
import math
N = int(input("Enter the N:"))
total = 0
for i in range(int(math.log10(N))+1):
    total += N%10
    N//=10
print(total)


## Q25. Product of Digits

Take an integer and find the product of its digits.

### Test Cases

```text
Input: 234 | Output: 24
Input: 105 | Output: 0
```

---Answer:
import math
N = int(input("Enter the N:"))
product = 1
for i in range(int(math.log10(N))+1):
    product *= N%10
    N//=10
print(product)

## Q26. Count Even Digits

Count how many digits of a given integer are even.

### Test Cases

```text
Input: 58321 | Output: 2
Input: 24680 | Output: 5
```

---Answer:
import math
N = int(input("Enter N:"))
count = 0
for i in range(int(math.log10(N))+1):
    if (N%10)%2 == 0:
        count += 1
    N//=10
print(count)



## Q27. Sum of Even Digits

Find the sum of only the even digits of a number.

### Test Cases

```text
Input: 58321 | Output: 10
Input: 24681 | Output: 20
```

---Answer:
import math
N = int(input("Enter N: "))
total = 0
for i in range(int(math.log10(N))+1):
    if (N%10)%2 == 0:
        total += N%10
    N//=10
print(total)


## Q28. Largest Digit Without `max()`

Find the largest digit of a number using one `for` loop. Do not use `max()` and do not convert the number to a string.

### Test Cases

```text
Input: 58321 | Output: 8
Input: 40796 | Output: 9
```

---Answer:
import math
N = int(input("Enter the N:"))
max_digit = N%10
for i in range(int(math.log10(N))+1):
    N//=10
    if (N%10)>max_digit:
        max_digit = N%10
print(max_digit)



## Q29. Smallest Digit Without `min()`

Find the smallest digit of a number using one `for` loop. Do not use `min()`.

### Test Cases

```text
Input: 58321 | Output: 1
Input: 40796 | Output: 0
```

---Answer:


## Q30. Reverse a Number

Reverse the digits of a positive integer using one `for` loop and `%` / `//`.

### Test Cases

```text
Input: 58321 | Output: 12385
Input: 12040 | Output: 4021
```

---Answer:
import math
N = int(input("Enter the N:"))
min_digit = N%10
for i in range(int(math.log10(N))+1):
    if (N%10)<min_digit:
        min_digit = N%10
    N//=10
print(min_digit)


## Q31. Palindrome Number

Check whether a number reads the same from left to right and right to left. Use one `for` loop.

### Test Cases

```text
Input: 1221 | Output: Palindrome
Input: 1234 | Output: Not Palindrome
```

---Answer:
import math
N = int(input("Enter:"))
N_copy = N
N_reversed = 0
for i in range(int(math.log10(N))+1):
    N_reversed = N_reversed*10 + N%10
    N//=10
if N_copy == N_reversed:
    print("Palindrome")
else:
    print("Not Palindrome")


## Q32. Count a Specific Digit

Take an integer and a target digit. Count how many times that digit occurs.

### Test Cases

```text
Input: 1223342, 2 | Output: 3
Input: 505550, 5 | Output: 4
```

---Answer:
import math
N = int(input("Enter the N:"))
target_digit = int(input())
count = 0
for i in range(int(math.log10(N))+1):
    if N%10 == target_digit:
        count+=1
    N//=10
print(count)


## Q33. First Digit Using Repeated Division

Find the first/leftmost digit of a positive integer using a `for` loop and repeated integer division. Do not convert the number to a string.

### Test Cases

```text
Input: 58321 | Output: 5
Input: 9047 | Output: 9
```

---Answer:
import math
N = int(input("Enter the N:"))
for i in range(int(math.log10(N))):
    N//=10
print(N)


## Q34. Difference Between Largest and Smallest Digit

Find the largest digit and smallest digit of a number, then print their difference. Do not use `max()` or `min()`.

### Test Cases

```text
Input: 58321 | Output: 7
Input: 40796 | Output: 9
```

---Answer:
import math
N = int(input("Enter the N:"))
large_digit = 0
small_digit = 9
for i in range(int(math.log10(N))+1):
    i = N%10
    if i>large_digit:
        large_digit = i
    if i<small_digit:
        small_digit = i
    N//=10
print(large_digit - small_digit)


## Q35. Digit Position Value

Take a positive integer and print each digit with its position from the right, starting from position `1`.

### Test Case

```text
Input: 58321
```

### Expected Output

```text
1 1
2 2
3 3
8 4
5 5
```

The first value is the digit and the second value is its position from the right.

--- Answer:
import math
N = int(input())
for i in range(1,int(math.log10(N))+2):
    print(f"{N%10} {i}")
    N//=10



## Q36. Armstrong Number — 3 Digit

Take a 3-digit number and check whether it is an Armstrong number.

For example:

`153 = 1³ + 5³ + 3³`

### Test Cases

```text
Input: 153 | Output: Armstrong Number
Input: 123 | Output: Not Armstrong Number
```

# ---Answer:
import math
N = int(input("Enter the N:"))
N_copy = N
length = int(math.log10(N))+1
total = 0
for i in range(length):
    i = N%10
    total+= i**length
    N//=10
if total == N_copy:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")






---
