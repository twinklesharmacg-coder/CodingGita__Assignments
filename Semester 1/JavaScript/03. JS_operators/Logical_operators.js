// ## Part F]: Logical Operators

// ***

// ### 1. Logical AND `&&`

// Write a JavaScript program for each:

// 1. Stored username is `"admin"` and password is `1234`. Check if both are valid using `&&` and print the result.  
//Ans:
// let storedUsername="admin";
// let storedPassword=1234;
// let inputUsername="admin";
// let inputPassword=1234;
// let isValid=(inputPassword==storedUsername)&&(inputPassword==storedPassword);
// console.log("Are credentials Valid:",isValid);

// 2. A user is logged in (`isLoggedIn = true`) and has permission (`hasPermission = true`). Check if they can access a page using `&&`.  

//Ans:
// let isLoggedIn=true;
// let hasPermission=true;
// let canAccess = isLoggedIn && hasPermission
// console.log("Can the user access the page?", canAccess);


// 3. A product is in stock (`inStock = true`) and its price is less than ₹1000 (`price = 800`). Check if it can be bought using `&&`. 

//Ans:
// let inStock = true
// let price = 800
// let isWithinBudget = price <= 1000
// let canBuy = inStock && isWithinBudget
// console.log("Can it be bought?", canBuy);

// 4. A student has marks `75` and attendance `80`. Passing requires marks greater than `65` **and** attendance greater than `70`. Check using `&&`.  

//Ans:
// let marks = 75
// let attendance = 80
// let hasPassed = (marks > 65) && (attendance > 70)
// console.log("Has student passed?", hasPassed);


// 5. Two conditions: `isWeekend = true` and `isHoliday = false`. A party happens only if both are true. Check using `&&`.

//ANS:
// let isWeekend = true
// let isHoliday = false
// let willPartyHappen = isWeekend && isHoliday
// console.log("Will party happen?", willPartyHappen);



// ### Additional Questions (Logical AND `&&`)

// 6. Predict the output:
//    ```js
//    let a = 0;
//    let b = 10;
//    let result = a && b;
//    console.log(result);
//    ```

//output:0


// 7. Predict the output:
//    ```js
//    let x = 5;
//    let y = 10;
//    let result = (x > 3 && y) || 0;
//    console.log(result);
//    ```

//output:10

// 8. Predict the output:
//    ```js
//    let p = "Hello";
//    let q = "";
//    let r = "World";
//    let result = p && q && r;
//    console.log(result);
//    ```

//output:""

// 9. Predict the output:
//    ```js
//    let val = 5;
//    let condition = val && (val = 0);
//    console.log(condition);
//    console.log(val);
//    ```

//Output:0,0


// 10. Predict the output:
//     ```js
//     let x = 10;
//     let y = 20;
//     let result = (x && y) && (x > y);
//     console.log(result);
//     ```

//output:false

// ***




// ### 2. Logical OR `||`

// Write a JavaScript program for each:

// 1. A user can login with either a correct password (`passwordCorrect = true`) or a valid OTP (`otpValid = false`). Check if login is allowed using `||`. 

//ans:
// let passwordCorrect = true
// let otpValid = false
// let loginAllowed = passwordCorrect || otpValid
// console.log("Is login allowed?", loginAllowed);

// 2. A discount applies if the user is a member (`isMember = false`) or has a coupon (`hasCoupon = true`). Check using `||`.  

//ans:
// let isMember = false
// let hasCoupon = true
// let isDiscountApplied = isMember || hasCoupon
// console.log("Is the discount applied?", isDiscountApplied);


// 3. Entry is allowed if age is above `18` (`age = 16`) **or** height is above `150` cm (`height = 155`). Check using `||`.  

//ans:
// let age = 16
// let height = 155
// let entryAllowed = (age > 18) || (height > 150)
// console.log("Is entry allowed?", entryAllowed);


// 4. A form is valid if either email is given (`emailGiven = true`) or phone is given (`phoneGiven = false`). Check using `||`.  

//ans:
// let emailGiven = true
// let phoneGiven = false
// let isFormValid = emailGiven || phoneGiven
// console.log("Is form valid?", isFormValid);


// 5. A game level opens if score is above `1000` (`score = 900`) **or** time bonus is collected (`timeBonus = true`). Check using `||`.
//ans:
// let score = 900;
// let timeBonus = true;
// let gameLevelOpens = (score > 1000) || timeBonus;
// console.log("Is game level open?", gameLevelOpens);



// ### Additional Questions (Logical OR `||`)

// 6. Predict the output:
//    ```js
//    let a = 0;
//    let b = false;
//    let c = "";
//    let d = null;
//    let e = 42;
//    let result = a || b || c || d || e;
//    console.log(result);
//    ```
//output:42

// 7. Predict the output:
//    ```js
//    let x = "Hello" || 0;
//    let y = 0 || "Hi";
//    console.log(x, y);
//    ```
//output: Hello  Hi

// 8. Predict the output:
//    ```js
//    let a = 10;
//    let b = 20;
//    let result = (a < 5) || (b > 15);
//    console.log(result);
//    ```
//output:true

// 9. Predict the output:
//    ```js
//    let val = 5;
//    let condition = val || (val = 0);
//    console.log(condition);
//    console.log(val);
//    ```
//output:5,5

// 10. Predict the output:
//     ```js
//     let x = "" || 0 || false || null || undefined || "OK";
//     console.log(x);
//     ```

//output:OK

// ***

// ### 3. Logical NOT `!`

// Write a JavaScript program for each:

// 1. A user is not banned (`isBanned = false`). Check if they can login by negating `isBanned` using `!`.
//ans: 
// let isBanned = false
// let canLogin =!isBanned
// console.log("Can the user login?", canLogin);


// 2. A task is not completed (`isCompleted = false`). Check if it is still pending using `!`.  
//ans:
// let isCompleted = false
// let isPending = !isCompleted
// console.log("Is the task still pending?", isPending);


// 3. A light is on (`isOn = true`). Check if it is off using `!`.  
//ans:
// let isOn = true
// let isOff = !isOn
// console.log("Is the light off?", isOff);


// 4. A subscription is not active (`isActive = false`). Check if the user cannot access premium content using `!`. 
// let isActive = false
// let cannotAccess = !isActive
// console.log("Can the user not access premium content?", cannotAccess);



// 5. A file is not read‑only (`isReadOnly = false`). Check if it can be edited using `!`.
//ans:
// let isReadOnly = false
// let canEdit = !isReadOnly
// console.log("Can the file be edited?", canEdit);



// ### Additional Questions (Logical NOT `!`)

// 6. Predict the output:
//    ```js
//    let a = 0;
//    let b = 1;
//    console.log(!a, !b);
//    ```
//output:true false

// 7. Predict the output:
//    ```js
//    let x = "Hello";
//    let y = "";
//    console.log(!x, !y);
//    ```
//outpt:false true



// 8. Predict the output:
//    ```js
//    let val = 5;
//    let result = !val;
//    console.log(result);
//    ```

//output:false


// 9. Predict the output:
//    ```js
//    let a = 10;
//    let b = 20;
//    let result = !(a && b);
//    console.log(result);
//    ```
//output:false

// 10. Predict the output:
//     ```js
//     let x = 0;
//     let y = 1;
//     let result = !(x || y);
//     console.log(result);
//     ```
//output:false