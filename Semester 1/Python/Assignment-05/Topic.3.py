# Level 3 — Factorial & Product Logic

## Q15. Factorial of a Number

Take an integer `N` and calculate `N!` using a `for` loop.

### Test Cases
5040

```text
Input: 5 | Output: 120
Input: 7 | Output: ```

---Answer:
N=int(input("Enter a number:"))
product=1
for i in range(1,N+1):
   product=product*i
print(product)
  


## Q16. Factorial from 1 to N

Take `N` and print the factorial of every number from `1` to `N`.

### Test Case

```text
Input: 5
```

### Expected Output

```text
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
```

---Answer:
N=int(input("Enter the number here:"))
factorial = 1
for i in range(1, N + 1):
    factorial *= i
    print(f"{i}! = {factorial}")


## Q17. Product of Even Numbers

Take `N` and find the product of all even numbers from `2` to `N`.

### Test Cases

```text
Input: 10 | Output: 3840
Input: 6 | Output: 48
```

---Answer:
N = int(input("Enter N: "))
product=1
for i in  range(2,N+1):
  if i%2==0:
    product*=i
print(product)
    
    
     
    

## Q18. Product of Odd Numbers

Take `N` and find the product of all odd numbers from `1` to `N`.

### Test Cases

```text
Input: 7 | Output: 105
Input: 9 | Output: 945
```

---Answer:

N = int(input("Enter N: "))

product = 1
for num in range(1, N + 1, 2):
    product *= num

print(product)




## Q19. Double Factorial — Even Numbers

Take an even number `N`. Calculate:

`N × (N-2) × (N-4) × ... × 2`

Use one `for` loop.

### Test Cases

```text
Input: 8 | Output: 384
Input: 10 | Output: 3840
```

---Answer:
 N=int(input("Enter the number here:"))
factorial = 1
for i in range(N.0.-2):
    factorial *= i
print(factorial)
       

## Q20. Sum of Squares

Take `N` and calculate:

`1² + 2² + 3² + ... + N²`

### Test Cases

```text
Input: 5 | Output: 55
Input: 10 | Output: 385
```

---Answeer:
N = int(input("Enter N: "))

total_sum = 0

for i in range(1, N + 1):
  square=i*i
  total_sum += square
  
print(total_sum)  



## Q21. Sum of Cubes

Take `N` and calculate:

`1³ + 2³ + 3³ + ... + N³`

### Test Cases

```text
Input: 4 | Output: 100
Input: 5 | Output: 225
```

---Answer:
N = int(input("Enter N: "))

total_sum = 0

for i in range(1, N + 1):
  cube=i**3
  total_sum += cube
  
print(total_sum)  

## Q22. Factorial-Based Sum

Take `N` and calculate:

`1! + 2! + 3! + ... + N!`

Use only one `for` loop.

### Test Cases

```text
Input: 4 | Output: 33
Input: 5 | Output: 153
```

---Answer:
N=int(input("Enter the number here:"))
factorial = 1
total_sum=0

for i in range(1, N + 1):
    factorial *= i
    total_sum+=factorial
print(total_sum)

