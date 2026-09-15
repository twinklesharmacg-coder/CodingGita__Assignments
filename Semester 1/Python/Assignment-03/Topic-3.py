# Q7. Basic Membership

#Predict the output:


#text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Python" not in text)

# Q8. Character Membership

Given:

```python
word = "computer"
```

Write expressions to check:

1. Whether `"p"` is present.
2. Whether `"x"` is present.
3. Whether `"c"` is not present.

---Ans
print(p in word)
print(x in word)
print(c not in word)

# Q9. Case Sensitivity in Membership

#Predict the output:

```python
text = "Python"

print("P" in text)
print("p" in text)
print("Python" in text)
print("python" in text)
```

Explain why some results are different.

---Ans
print("P" in text)   false because python  being case sensitive considers lowercase p as different
print("Python" in text)  true 
print("python" in text)  false because of case sensitivity


# Q10. Membership with User Input

Take a word or sentence as input and check whether the character `"a"` occurs in it.

### Test Cases

| Input | Expected Output |
|---|---|
| `apple` | `True` |
| `Python` | `False` |
| `banana` | `True` |

---

