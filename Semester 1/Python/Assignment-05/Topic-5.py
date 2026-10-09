# Level 5 — String & Character Logic

## Q37. Print Characters with Index

Take a string and print every character along with its index.

### Test Case

```text
Input: Python
```

### Expected Output

```text
0 P
1 y
2 t
3 h
4 o
5 n
```

---Answer:
string = input("enter the string here:")
for i in range(len(string)):
    print(f"{i} {string[i]}")


## Q38. Count Characters Without `len()`

Take a string and find its length without using `len()`. Use a `for` loop to count the characters.

### Test Cases

```text
Input: Python | Output: 6
Input: Hello World | Output: 11
```

---Answer:
string = input("enter the string here:")
count = 0
for i in string:
    count+=1
print(count)


## Q39. Count Vowels and Consonants

Take a string containing English letters and spaces. Count vowels and consonants using one `for` loop. Ignore spaces.

### Test Cases

```text
Input: Python | Output: Vowels = 1, Consonants = 5
Input: Hello World | Output: Vowels = 3, Consonants = 7
```

---Answer:
string = input("Enter:").lower()
vowel_count =consonant_count = 0
for i in string:
    if i!=" ":
        if i in "aeiou":
            vowel_count+=1
        else:
            consonant_count+=1
print(f"Vowels = {vowel_count}, Consonants = {consonant_count}")


## Q40. Character Frequency

Take a string and a target character. Count how many times the target appears.

### Test Cases

```text
Input: programming, g | Output: 2
Input: banana, a | Output: 3
```

---Answer:
string = input()
target = input()
count = 0
for i in string:
    if target == i:
        count+=1
print(count)


## Q41. First Occurrence Position

Take a string and a target character. Find the index of the **first occurrence** of that character.

If it does not occur, print `Not Found`.

### Test Cases

```text
Input: programming, g | Output: 3
Input: banana, n | Output: 2
Input: Python, z | Output: Not Found
```

> **Hint:** Think carefully about how a variable can remember the first position found.

---Answer:
string = input("Enter the string :")
target = input("Enter the string here :")
index = 0
count = 0
for i in range(len(string)):
    if target == string[i] and count == 0:
        count+=1
        index = i
if count != 0:
    print(index)
else:
    print("Not Found")


## Q42. Count Uppercase and Lowercase

Take a string containing English letters. Count uppercase and lowercase characters using one `for` loop.

### Test Cases

```text
Input: PyThOn | Output: Uppercase = 3, Lowercase = 3
Input: HelloWORLD | Output: Uppercase = 6, Lowercase = 4
```

---Answer:
string = input("Enter the :")
upper_count = lower_count = 0
for i in string:
    if i.isupper():
        upper_count+=1
    elif i.islower():
        lower_count+=1
print(f"Uppercase = {upper_count}, Lowercase = {lower_count}")


## Q43. Character Code Analyzer

Take a string and print every character along with its Unicode value using `ord()`.

### Test Case

```text
Input: ABC
```

### Expected Output

```text
A 65
B 66
C 67
```

---Answer:
string = input("Enter the here:")
for i in string:
    print(f"{i} {ord(i)}")






## Q44. String Without Vowels

Take a string and print all characters except vowels. Preserve the original order.

### Test Cases

```text
Input: education | Output: dctn
Input: Python | Output: Pythn
```

---Answer:
string = input("enter the input here:")
for i in string:
    if i.lower() not in "aeiou":
        print(i,end="")


