# Topic-4 — Logical Conditions

## Q29. College Admission Eligibility

A student is eligible if:

- marks are at least `60`, **and**
- attendance is at least `75`.

Take both values and print:

```text
Eligible
```

or:

```text
Not Eligible
```

### Test Cases

`70 80 → Eligible`  
`70 70 → Not Eligible`  
`55 90 → Not Eligible`

---

## Q30. Scholarship Eligibility

A student gets a scholarship if marks are at least `85` **or** family income is below `300000`.

Take marks and income.

### Test Cases

`90 500000 → Scholarship Available`  
`70 250000 → Scholarship Available`  
`70 500000 → No Scholarship`

---

## Q31. Weekend Check

Take a day name.

If it is `Saturday` or `Sunday`, print:

```text
Weekend
```

Otherwise print:

```text
Weekday
```

### Test Cases

`Saturday → Weekend`  
`Sunday → Weekend`  
`Monday → Weekday`

---

## Q32. Online Exam Access

A student can access an exam if:

- username is `"student"`, and
- password is `"python123"`.

Print:

```text
Access Granted
```

or:

```text
Access Denied
```

### Test Cases

`student python123 → Access Granted`  
`student wrong123 → Access Denied`  
`admin python123 → Access Denied`

---

## Q33. Delivery Availability

A delivery is available if the city is `"Ahmedabad"` or `"Gandhinagar"`.

### Test Cases

`Ahmedabad → Delivery Available`  
`Gandhinagar → Delivery Available`  
`Surat → Delivery Unavailable`

---

## Q34. Number Range Check

Take an integer.

Print `Inside Range` if the number is between `10` and `50`, inclusive. Otherwise print `Outside Range`.

### Test Cases

`10 → Inside Range`  
`35 → Inside Range`  
`50 → Inside Range`  
`55 → Outside Range`

---

## Q35. Secure Transaction

A transaction is allowed only when:

- amount is at most `50000`, and
- OTP entered is `"1234"`.

### Test Cases

`25000 1234 → Transaction Approved`  
`60000 1234 → Transaction Declined`  
`25000 9999 → Transaction Declined`

---
