
// 1. Write a ternary operator to check whether a given number is divisible by 7. If yes, return `"Divisible by 7"`, otherwise `"Not Divisible by 7"`.
// let num=9;
// let result= num%7==0 ? "Divisible by 7" : "Not divisible by 7"
// console.log(result)

// 2. Using ternary operator, check if the temperature is greater than or equal to 30. Return `"Hot Day"` or `"Pleasant Day"`.
// let  temperature=7;
// let  result = temperature>=30 ? "Hot Day" : "Pleasant Day"
// console.log(result)

// 3. Write a ternary expression that checks if a string is empty. Return `"Empty String"` if it is empty, otherwise `"String has content"`.
let x=""
x==""? console.log("Empty String") : console.log("String has content")

// 4. Using nested ternary, check a person’s age and return:  
//    - `"Child"` (age < 13)  
//    - `"Teenager"` (13–19)  
//    - `"Adult"` (20 and above)
let age=60
age<13 ? console.log("Child") : age<19 ? console.log("Teenager") : console.log("Adult")

// 5. Write a nested ternary to find the greater of three numbers (`a`, `b`, `c`) without using `Math.max`.
 let a=10
 let b=7
 let c=9
 a>b && a>c ? console.log(a): b>c && b>a ? console.log(b) : console.log(c)


// 6. Create a nested ternary that classifies a student’s marks as:  
//    - `"Distinction"` (≥ 75)  
//    - `"First Class"` (60–74)  
//    - `"Second Class"` (50–59)  
//    - `"Pass"` (35–49)  
//    - `"Fail"` (< 35)
let marks=50
marks>=75 ? console.log("Distinction") : marks >=60 ? console.log("First class") : marks>=50 ? console.log("second class") : marks>=35 ? console.log("Pass") : console.log("Fail")

// 7. Write a single nested ternary expression that returns one of the following based on a number:  
//    `"Positive Even"`, `"Positive Odd"`, `"Negative Even"`, `"Negative Odd"`, or `"Zero"`.
let num = 45
num % 2 == 0 && num > 0 ? console.log("Positive Even") : num % 2 == 0 && num < 0 ? console.log("Negative Even") : num % 2 != 0 && num > 0 ? console.log("Positive Odd") : num % 2 != 0 && num < 0 ? console.log("Negative Odd") : console.log("Zero")

// 8. Using only nested ternary operators, implement the full leap year logic  
//    (divisible by 4 **and** (not divisible by 100 **or** divisible by 400)) and return `"Leap Year"` or `"Not a Leap Year"`.
let year = 2089
year % 4 == 0 && (year % 100 != 0 || year % 400 == 0) ? console.log("Leap Year") : console.log("Not a Leap Year")


// 9. Convert the following decision tree into **one single nested ternary** expression:  
//    ```
//    if (role === "admin") {
//      if (action === "delete") → "Admin Delete"
//      else if (action === "edit") → "Admin Edit"
//      else → "Admin Other"
//    } else if (role === "user") {
//      if (action === "view") → "User View"
//      else → "User Restricted"
//    } else {
//      → "Invalid Role"
//    }
//
//```
let action = "edit"

role === "admin" ? (action === "delete" ? console.log("Admin Delete") : action === "edit" ? console.log("Admin Edit") : console.log("Admin Other")) : role === "user" ? (action === "view" ? console.log("User View") : console.log("User Restricted")) : console.log("Invalid Role")



// 10. Write a complex nested ternary that calculates discount and final amount based on these rules:  
//     - Cart total ≥ 5000 → 20% discount  
//     - Cart total ≥ 2000 → 10% discount  
//     - Cart total ≥ 1000 → 5% discount  
//     - Otherwise → 0% discount  
//     Return both the discount percentage and the final payable amount in a single expression (you may return an object or a formatted string)
let cartTotal = 6000

let result = cartTotal>= 5000 ? `Discount Percentage: 20 & Final Payable Amount: ${cartTotal - cartTotal * 0.2}`: cartTotal>=2000 ? `Discount Percentage: 10, Final Payable Amount: ${cartTotal - cartTotal * 0.1}` : cartTotal>= 1000 ? `Discount Percentage: 5, Final Payable Amount: ${cartTotal - cartTotal * 0.05}`: `Discount Percentage: 0, Final Payable Amount: ${cartTotal}`

console.log(result)