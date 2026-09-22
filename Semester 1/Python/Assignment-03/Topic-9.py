## Q49. `sep`

Predict the output:

```python
print("2026", "09", "09", sep="-")
```

---Answer:
2026-09-09


## Q50. `end`

Predict the output:



```python
print("Hello", end=" ")
print("Python")
```

---Answer:
Hello Python


## Q51. `sep` and `end`
Write a program that produces exactly:

```text
10-20-30
40-50-60
```

Use `sep` and `end`.

---Answer:
print("10","20","30",sep="-")
print("40","50","60",sep="-")

## Q52. Student Introduction

Take:

- Name
- Age
- City
- Course

Display them using an f-string:

```text
Name: Rahul
Age: 20
City: Ahmedabad
Course: B.Tech
```

---Answer:
print(f"Name:Rahul \n Age:20 \n City:Ahemdabad \n Course: B.Tech")


## Q53. Formatted Price

Take a price as input and display it with exactly two decimal places.

### Test Cases

| Input | Expected Output |
|---|---|
| `45` | `45.00` |
| `99.5` | `99.50` |
| `120.678` | `120.68` |

Use an f-string.

---Answer:
price=input("Enter the text here:")
formatted_price = f"{price:.2f}"
print(formatted_price)
