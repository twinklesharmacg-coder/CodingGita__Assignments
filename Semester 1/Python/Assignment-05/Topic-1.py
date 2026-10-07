## Q1. Predict the Loop Values

Without running the code, write the values printed:

```python
for i in range(2, 15, 3):
    print(i)
```

### Expected Output

Write the exact output.

---Answer:
2
5
8
11
14

## Q2. Reverse `range()` Prediction

Predict the output:

```python
for i in range(15, 2, -3):
    print(i)
```

---Answer:
15
12
9
6
3

## Q3. How Many Iterations?

Without running the program, determine how many times the loop executes and list the values of `i`.

```python
for i in range(4, 31, 5):
    print(i)
```

---Answer:
4
9
14
19
24
29

## Q4. Correct the Boundary

A student wants to print every third number from `3` through `18`:

```python
for i in range(3, 18, 3):
    print(i)
```

Correct the program so that `18` is also printed.

### Expected Output

```text
3
6
9
12
15
18
```

---Answer:
for i in range(3,19,3):
    print(i)

## Q5. Number and Distance from 20

Print each number from `5` to `10` along with its distance from `20`.

### Expected Output

```text
5 15
6 14
7 13
8 12
9 11
10 10
```

---Answer:
for i in range (5,11):
   distance=20-i
   print(i,distance)

## Q6. Number, Square and Cube

For every number from `1` to `6`, print the number, its square, and its cube on one line.

### Expected Output

```text
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
```

---Answer:
for i in range(1,7):
    square=i*i
    cube=i**3
    print(i,square,cube)
