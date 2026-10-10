# Level 7 — Tricky Single-Loop Problems

## Q53. Second Largest Digit

Take a number and find the **second largest distinct digit** using one `for` loop.

Do not use `sort()`, `max()`, or convert the number to a string.

### Test Cases

```text
Input: 58321 | Output: 5
Input: 987654 | Output: 8
Input: 99852 | Output: 8
```

> Repeated digits should not count twice. For example, in `99852`, the largest digit is `9` and the second largest distinct digit is `8`.

---Answer:
import math
n = abs(int(input()))
largest_digit = second_largest_digit = 0
for _ in range(int(math.log10(n))+1):
    i = n%10
    if i > largest_digit:
        second_largest_digit = largest_digit
        largest_digit = i
        
    elif i > second_largest_digit and i<largest_digit:
        second_largest_digit = i
    n//=10
print(second_largest_digit)



## Q54. Longest Consecutive Equal Character Run

Take a string and find the length of the longest consecutive run of the same character.

### Test Cases

```text
Input: aaabbccccd | Output: 4
Input: programming | Output: 2
Input: abcde | Output: 1
```

> You must solve this with one `for` loop. Think about a **current count** and a **best count**.

---Answer:
string = input("Enter:")
curr_count = best_count = 1
for i in range(1,len(string)):
    pre_chr = string[i-1]
    curr_chr = string[i]
    if curr_chr == pre_chr:
        curr_count += 1
    else:
        curr_count = 1
    if curr_count>best_count:
        best_count=curr_count
print(best_count)


## Q55. Most Frequent Character — Controlled Approach

Take a string and a target character. Count how many times the target occurs and compare it with the number of characters in the string to determine its frequency percentage.

Use one `for` loop. Do not use dictionaries.

### Test Cases

```text
Input: banana, a | Output: Count = 3, Frequency = 50.0%
Input: programming, g | Output: Count = 2, Frequency = 18.18%
```

> The challenge is to maintain the count and calculate the final percentage correctly.

---Answer:
string , target = input("Enter:"), input("Enter:")
count = 0
for i in string:
    if i == target:
        count+=1
frequency = (count/len(string)) * 100
print(f"Count = {count}, Frequency = {frequency:.2f}%")


## Q56. Running Digit Sum Until the End

Take a positive integer. Process its digits from right to left and print the running sum after each digit is processed.

### Test Case

```text
Input: 58321
```

### Expected Output

```text
1
3
6
14
19
```

---Answer:
import math
N = int(input())
total = 0
for i in range(int(math.log10(N))+1):
    total+=N%10
    print(total)
    N//=10

## Q57. Number with Most Even Digits

Take a positive integer and determine whether it contains more even digits or more odd digits.

### Test Cases

```text
Input: 24681 | Output: More Even Digits
Input: 13579 | Output: More Odd Digits
Input: 1234 | Output: Equal
```

---Answer:
import math
N = int(input())
even_count = odd_count = 0
for i in range(int(math.log10(N))+1):
    if (N%10 )%2==0:
        even_count+=1
    else:
        odd_count+=1
    N//=10
if even_count>odd_count:
    print("More Even Digits")
elif even_count<odd_count:
    print("More Odd Digits")
else:
    print("Equal")

## Q58. Alternating Digit Sum

Take a positive integer. Starting from the **rightmost digit**, add the 1st digit, subtract the 2nd digit, add the 3rd digit, subtract the 4th digit, and continue this pattern.

Use exactly one `for` loop and `%` / `//`.

### Test Cases

```text
Input: 12345 | Output: 3
Input: 58321 | Output: -1
Input: 2468 | Output: 4
```

For `12345`:

`5 - 4 + 3 - 2 + 1 = 3`

> This question tests whether you can maintain changing logic from one iteration to the next.

---Answer:
import math
N = int(input())
total = 0
for i in range(int(math.log10(N))+1):
    digit = N%10
    if i%2==0:
        total+= digit
    else:
        total-= digit
    N//=10
print(total)

## Q59. Output Prediction — Accumulator Trap

Predict the output without running the code:

```python
total = 0
for i in range(1, 6):
    total = total + i * 2
    print(total)
```

### Expected Output

Write the exact five lines.

---Answer:
total = 0
for i in range(1, 6):
    total = total + i * 2
    print(total)

# Output:
# 2
# 6
# 12
# 20
# 30

## Q60. Output Prediction — Condition Inside Loop

Predict the output:

```python
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count = count + 1
print(count)
```

Explain why the final value is what it is.

---Answer:
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count = count + 1
print(count)       

# Output: 5


## Q61. Debug the Accumulator

The following program is intended to calculate `1 + 2 + 3 + 4 + 5`, but it is incorrect:

```python
sum = 0
for i in range(1, 6):
    sum = i
print(sum)
```

1. Identify the mistake.
2. Correct the program.
3. Explain what should happen to the accumulator in every iteration.

### Expected Output

```text
15
```

---Answer:
sum = 0
for i in range(1, 6):
    sum += i
print(sum)
# The accumulator should get added and reassigned in each iteration
