# Level 9 — Final Challenges

## Q68. Number Profile

Take a positive integer and, using exactly one `for` loop, find all of the following:

- number of digits
- sum of digits
- largest digit
- smallest digit
- number of even digits
- number of odd digits

Do not convert the number to a string. Do not use `max()` or `min()`.

### Test Case

```text
Input: 58321
```

### Expected Output

```text
Digits: 5
Sum: 19
Largest: 8
Smallest: 1
Even Digits: 2
Odd Digits: 3
```

---Answer:
import math
N = int(input())
length = int(math.log10(N)) + 1
count_even = count_odd = total = 0
largest_digit = smallest_digit = N%10
for i in range(length):
    digit=N%10
    total+=digit
    if digit%2==0:
        count_even+=1
    else:
        count_odd+=1
    if digit>largest_digit:
        largest_digit = digit
    elif digit<smallest_digit:
        smallest_digit = digit
    N//=10
print("Digits:", length)
print("Sum:", total)
print("Largest:", largest_digit)
print("Smallest:", smallest_digit)
print("Even Digits:", count_even)
print("Odd Digits:", count_odd)



## Q69. String Balance Challenge

Take a string containing letters. Using exactly one `for` loop, calculate:

- total characters
- vowels
- consonants
- uppercase characters
- lowercase characters
- characters at even indexes

Ignore spaces when counting vowels/consonants/uppercase/lowercase, but include them in total characters and index positions.

### Test Case

```text
Input: Hello World
```

### Expected Output

```text
Total Characters: 11
Vowels: 3
Consonants: 7
Uppercase: 2
Lowercase: 8
Even Index Characters: 6
```

---Answer:
total_chars = len(string)
count_vowels = count_consonants = count_upper = count_lower = count_even = 0
for i in range(total_chars):
    char = string[i]
    if char != " ":
        if char in "aeiouAEIOU":
            count_vowels += 1
        else:
            count_consonants += 1
        if char.isupper():
            count_upper+=1
        else:
            count_lower+=1
    if i%2==0:
        count_even+=1
print("Total Characters:", total_chars)
print("Vowels:", count_vowels)
print("Consonants:", count_consonants)
print("Uppercase:", count_upper)
print("Lowercase:", count_lower)
print("Even Index Characters:", count_even)
