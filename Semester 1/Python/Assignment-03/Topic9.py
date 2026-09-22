Topic-10 — Debugging

Q54. String and Integer
Find and correct the error:

age = input("Enter age: ")
print("Age after 5 years:", age + 5)

--Answer:
age=int(input("Enter age:")
  print("Age after 5 years:", age + 5)

Q55. Incorrect Quotes
Find and correct the error:

print('It's Python')
Q56. Incorrect Slicing Syntax
Find and correct the error:

text = "Python"
print(text[1,4])

--Answer:
text = "Python"
print(text[1:4])

Q57. Incorrect split() Separator
The program is:

a, b = input().split(",")
The user enters:

10 20
Why does the program fail?

Rewrite it correctly for the given input.

---Answer:
because we have mentioned incode to split at comma.

a, b = input().split()

Q58. String Addition vs Numeric Addition
What will this program print?

a, b = input().split()

print(a + b)
Input:
10 20
Then modify the program so that it performs numeric addition.

--Answer:
1020

a, b = input().split()
a1=int(a)
b1=int(b)
print(a1 + b1)



Q59. Escape Sequence Debugging
Find and correct the problem:

print("C:\new\test")
The programmer wants to display:

C:\new\test
What special-character problem can occur here?

--Answer:
Instead of printing C:\new\test on a single line, Python will break the string onto a new line at \n and insert a tab space before test.
