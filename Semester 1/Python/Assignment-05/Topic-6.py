
# Level 6 — Midpoint, Half & String Logic

## Q45. Find the Middle Character

Take a string and find its middle character using its length and indexing.

For this question, assume the string length is odd.

### Test Cases

```text
Input: Python | Output: h
Input: abcde | Output: c
```

---Answer:
string = input("Enter:")
for i in range(len(string)):
    if i==(len(string)//2):
        print(string[i])


## Q46. First Half and Second Half

Take a string with an even number of characters. Find and print its first half and second half.

### Test Cases

```text
Input: PythonCode
Output:
First Half: Pytho
Second Half: nCode

Input: ABCDEF
Output:
First Half: ABC
Second Half: DEF
```

---Answer:
string = input("Enter:")
first_half = second_half = ""
for i in range(len(string)):
    if i < (len(string)//2):
        first_half+=string[i]
    else:
        second_half+=string[i]
print("First Half:", first_half)
print("Second Half:", second_half)
  

## Q47. Split a String by Length — Odd vs Even

Take a string as input.

Use the string length and a **single `for` loop** to divide the string into halves.

- If the length is **odd**:
  - Print the first half.
  - Print the middle character.
  - Print the second half.
- If the length is **even**:
  - Print the first half.
  - Print the second half.
- Do not use slicing to directly obtain the final halves.
- Use one `for` loop for the character-processing logic.

### Test Cases

```text
Input: PROGRAM
Output:
First Half: PRO
Middle: G
Second Half: RAM

Input: PYTHON
Output:
First Half: PYT
Second Half: HON

Input: HELLO
Output:
First Half: HE
Middle: L
Second Half: LO
```
---Answer:
string = input("Enter:")
first_half = second_half = middle_char = ""
length = len(string)
for i in range(length):
    if length%2 == 0:
        if i < length//2:
            first_half+=string[i]
        else:
            second_half+=string[i]
    else:
        if i == length//2:
            middle_char = string[i]
        elif i < length//2:
            first_half+=string[i]
        else:
            second_half+=string[i]
print("First Half:", first_half)
if middle_char!="":
    print("Middle:", middle_char)
print("Second Half:", second_half)
         
         
## Q48. Compare Two Halves

Take a string of even length. Split it logically into two equal halves and check whether both halves are identical.

Use one `for` loop.

### Test Cases

```text
Input: ABCABC | Output: Equal Halves
Input: ABCABD | Output: Different Halves
Input: XYZXYZ | Output: Equal Halves
```

---Answer:
string = input("Enter:")
first_half = second_half = ""
length = len(string)
for i in range(length):
    if i < (length//2):
        first_half+=string[i]
    else:
        second_half+=string[i]
if first_half == second_half:
    print("Equal Halves")
else:
    print("Different Halves")


## Q49. Mirror the String

Take a string and determine whether its first and last characters match, second and second-last match, and so on.

Print `Symmetric` if all corresponding characters match; otherwise print `Not Symmetric`.

Use one `for` loop.

### Test Cases

```text
Input: ABCCBA | Output: Symmetric
Input: ABCD | Output: Not Symmetric
Input: MADAM | Output: Symmetric
```

---Answer:
string = input("Enter the :")
length = len(string)
is_symmetric=True
for i in range(length//2):
    if string[i] != string[(length-1) - i]:
        is_symmetric = False
if is_symmetric:
    print("Symmetric")
else:
    print("Not Symmetric")


## Q50. Alternate Character Extraction

Take a string and print characters at even indexes only.

### Test Cases

```text
Input: ABCDEFGH | Output: ACEG
Input: Python | Output: Pto
```

---Answer:
string = input("Enter:")
for i in range(len(string)):
if i%2==0:
print(string[i],end="")
       

## Q51. Count Characters at Even and Odd Indexes

Take a string and count how many characters occur at even indexes and how many occur at odd indexes.

### Test Cases

```text
Input: Python | Output: Even Index = 3, Odd Index = 3
Input: ABCDE | Output: Even Index = 3, Odd Index = 2
```

---Answer:
string = input("Enter:")
count_even = count_odd = 0
for i in range(len(string)):
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(f"Even Index = {count_even}, Odd Index = {count_odd}")                                
                                 


## Q52. Swap Adjacent Characters

Take a string with an even number of characters. Print the string after swapping every adjacent pair.

Example:

`ABCDEFGH → BADCFEHG`

Use one `for` loop.

### Test Cases

```text
Input: ABCD | Output: BADC
Input: ABCDEFGH | Output: BADCFEHG
```

---Answer:
string = input("Enter the :")
new_string = ""
for i in range(0, len(string), 2):
    new_string+= string[i+1]
    new_string+= string[i]
print(new_string)


