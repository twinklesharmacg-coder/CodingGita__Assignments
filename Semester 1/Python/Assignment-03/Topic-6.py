## Q24. Basic Slicing

Given:

```python
text = "PYTHON"
```

Predict:

```python
print(text[0:3])
print(text[2:5])
print(text[1:6])
```

---Answers:
PYT
THO
YTHON


## Q25. Start and Stop

Given:

```python
text = "PROGRAMMING"
```

Predict:

```python
print(text[:4])
print(text[4:])
print(text[:])
```

---Answers:
PROG
RAMMING
PROGRAMMING

## Q26. Negative Slicing

Given:

```python
text = "COMPUTER"
```

Predict:

```python
print(text[-5:])
print(text[:-3])
print(text[-6:-2])
```

---Answers:
PUTER
COMPU
MPUT


## Q27. Step in Slicing

Given:

```python
text = "PYTHON"
```

Predict:

```python
print(text[::2])
print(text[1::2])
print(text[::-1])
```

---Answers:
PTO
YHN
NOHTYP


## Q28. Reverse a String

Take a string as input and reverse it using slicing.

### Test Cases

| Input | Expected Output |
|---|---|
| `Python` | `nohtyP` |
| `Hello` | `olleH` |
| `12345` | `54321` |

  
  ---Answers:
    string=input("Enter the text here")
   print(string[::-1]
         
## Q29. Alternate Characters

Take a string as input and print every second character starting from index `0`.

### Test Cases

| Input | Expected Output |
|---|---|
| `ABCDEFGH` | `ACEG` |
| `Python` | `Pto` |
| `12345678` | `1357` |

---Answers:
str=input("Enter your text here")
print(str[::2])


## Q30. Extract First and Last Three Characters

Take a string as input and print:

- First three characters
- Last three characters

### Test Cases

| Input | First Three | Last Three |
|---|---|---|
| `Programming` | `Pro` | `ing` |
| `Computer` | `Com` | `ter` |
| `Python` | `Pyt` | `hon` |

Use slicing.

---
user_input=input("Enter here:")
first_three=user_input[:3]
last_three=user_input[-3:]
print("first three:",first_three)
print("last three:"'last_three)

## Q31. Slicing Challenge

Given:

```python
text = "ABCDEFGHIJ"
```

Predict the output:

```python
print(text[2:8:2])
print(text[8:2:-2])
print(text[::-2])
```

For each expression, identify:

```text
start
stop
step
```

---Answers:
1.start-2 stop-8 step-2
2. start-8 stop-2 step-(-2)
3.start-0 stop-11 step:-2

## Q32. Slice Without Counting from the Beginning

Take the string:

```python
text = "BTECH-CSE-2026"
```

Use slicing to extract:

```text
BTECH
CSE
2026
```

Do not manually write the extracted strings.

---Answers:
text="BTECH-CSE-2026"
print(text[:-9])
print(text[-8:-5])
print(text[-4:]
