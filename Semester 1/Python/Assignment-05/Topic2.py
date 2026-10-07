# Level 2 — Counting & Accumulation

## Q7. Sum of Numbers in a Range

Take `start` and `end`. Find the sum of all integers from `start` to `end` using one `for` loop.

### Test Cases

```text
Input: 5 10 | Output: 45
Input: 12 15 | Output: 54
```

---Answer:
start=int(input("Enter the integer here:))
end=int(input("Enter the integer here:))
total_sum=0
for num in range(start,end+1):
     total_sum = total_sum + num
print(total_sum)


## Q8. Count Multiples of 3

Take `N` and count how many numbers from `1` to `N` are divisible by `3`.

### Test Cases

```text
Input: 10 | Output: 3
Input: 20 | Output: 6
```

---Answer:

N=int(input("Enter N: "))
count=0
for num in range(1,N+1):
    if num%3==0:
      count+=1
print(count)

## Q9. Sum of Multiples of 4

Take `N` and calculate the sum of all numbers from `1` to `N` divisible by `4`.

### Test Cases

```text
Input: 20 | Output: 60
Input: 30 | Output: 112
```

---Answer:
N = int(input("Enter N: "))
total_sum=0
for num in range(1,N+1):
   if num%4==0:
      total_sum = total_sum + num
print(total_sum)

## Q10. Count Numbers with Two Conditions

Take `N` and count numbers from `1` to `N` that are divisible by **both 3 and 5**.

### Test Cases

```text
Input: 50 | Output: 3
Input: 100 | Output: 6
```

---Answer:
N = int(input("Enter N: "))
count=0
for i in range(1,N+1):
   if i%3==0 and i%5==0:
        count=count+1
print(count)
     








## Q11. Sum Numbers Except Multiples of 3

Take `N` and find the sum of numbers from `1` to `N` that are **not divisible by 3**.

### Test Cases

```text
Input: 10 | Output: 37
Input: 15 | Output: 80
```

---Answer:
N=int(input("Enter the number here:"))
count=0
for i in range(1,N+1):
    if i%3!=0:
       count=count+1
print(count)
       





## Q12. Count Even and Odd Together

Take `N`. Using one loop, count how many numbers from `1` to `N` are even and how many are odd.

### Test Cases

```text
Input: 10 | Output: Even = 5, Odd = 5
Input: 7 | Output: Even = 3, Odd = 4
```

---Answer:
N=int(input("Enter the number here:")
even_count=0
odd_count=0
for num in range(1, N + 1):
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even = {even_count}, Odd = {odd_count}")



## Q13. Running Sum

Take `N`. Print the running sum after every number from `1` to `N`.

### Test Case

```text
Input: 5
```

### Expected Output

```text
1
3
6
10
15
```

---Answer:
N=int(input("Enter a number here:"))
sum=0
for i in range(1,N+1):
   sum=sum+i
   print(sum)



## Q14. Running Product

Take `N`. Starting with `1`, multiply by every number from `1` to `N` and print the product after each iteration.

### Test Case

```text
Input: 5
```

### Expected Output

```text
1
2
6
24
120
```

---Answer:
N=int(input("Enter N:))
product=1
for i in range(1,N+1):
  product=product*i
  print(product)


