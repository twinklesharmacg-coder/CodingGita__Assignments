## Q33. Basic `split()`

Predict the output:

```python
text = "Python is easy"

print(text.split())
```

Explain what separates the words.

---Answers:
the space betweeen the words seperate the words.

## Q34. Custom Separator

Predict the output:

```python
data = "apple,banana,mango"

print(data.split(","))
```

---Answwer:
apple
banana
mango

## Q35. Separator Not Present

Predict the output:

```python
text = "Python is easy"

print(text.split(","))
```

Why does it not split at the spaces?

---Answer:
Because here we have written the code to use the split function at commas but in our text commas are not there so split will not work.

## Q36. Split a Full Name

Take:

```text
Rahul Kumar Sharma
```

as input.

Use `.split()` and print each word on a separate line.

### Expected Output

```text
Rahul
Kumar
Sharma
```

---Answer:
text="Rahul kumar Sharma"
words = text.split()
print(words)


## Q37. Multiple Inputs Using `split()`

Take two values from the user in one line.

Example:

```text
Input:
Rahul Kumar
```

Store them in:

```text
first_name
last_name
```

Then display:

```text
First Name: Rahul
Last Name: Kumar
```

---  Amswer:
first_name,last_name=

## Q38. Three Numeric Inputs

Take three integers in one line using `.split()`.

Example:

```text
10 20 30
```

Convert them to integers and print their sum.

### Test Cases

| Input | Expected Output |
|---|---|
| `10 20 30` | `60` |
| `5 7 8` | `20` |
| `100 200 300` | `600` |

---

## Q39. Student Record

Input:

```text
Rahul,20,BTech,Ahmedabad
```

Use:

```python
.split(",")
```

to separate the information.

Display:

```text
Name: Rahul
Age: 20
Course: BTech
City: Ahmedabad
```

---
## Q40. Email Analyzer

Take an email address:

```text
rahul.kumar@gmail.com
```

Use `.split("@")` to separate:

- Username
- Domain

### Test Cases

| Input | Username | Domain |
|---|---|---|
| `rahul@gmail.com` | `rahul` | `gmail.com` |
| `student@yahoo.com` | `student` | `yahoo.com` |

---

## Q41. Sentence Analyzer

Take a sentence from the user.

Example:

```text
Python is very powerful
```

Use `.split()` to obtain the words.

Display:

```text
First word: Python
Last word: powerful
```

Also display the total number of words using the appropriate built-in operation.

---

