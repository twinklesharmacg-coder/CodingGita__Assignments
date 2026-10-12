// D] Relational Operator

// 1. Greater Than

// Question 1
let studentMarks = 78;
let passingMarks = 40;
let result = studentMarks>passingMarks
console.log("Student has scored more?", result);

// Question 2
let tempToday = 35;
let tempYesterday = 28;
let isHotter = tempToday>tempYesterday
console.log("Is today hotter?", isHotter);

// Question 3
console.log(15 > 10); // true
console.log(10 > 15); // false
console.log(10 > 10); // false

// Question 4
console.log("20" > 15); // true
console.log("5" > "10"); // true
console.log("abc" > 10); // false

// Question 5
console.log(null > 0); // false because null gets converted to 0 and 0 > 0 results in false
console.log(undefined > 0); // false because undefined gets converted to NaN and NaN > 0 results in false 

// Question 6
let itemsStock = 120
let itemsRequired = 85
let isSufficient = itemsStock > itemsRequired
console.log("Is stock sufficient?", isSufficient);

// Question 7
console.log(true > false); // true because true gets converted to 1 and false gets converted to 0 and then 1>0 results in true
console.log("10" > "2"); // false because the each character of first string gets compared to the corresponding character of the second string
console.log(NaN > 5); // false because any comparison with NaN results is false


// 2. Less Than

// Question 1
let maxWeight = 50
let currentWeight = 42
let canAddItems = currentWeight < maxWeight
console.log("Can more items still be added?", canAddItems);

// Question 2
let minAge = 18
let personAge = 16
let isUnderage = personAge < minAge
console.log("Is the person underage?", isUnderage);

// Question 3
console.log(8 < 12); // true
console.log(20 < 10); // false
console.log(7 < 7); // false

// Question 4
console.log("8" < 10); // true
console.log("20" < "3"); // true
console.log("hello" < 5); // false

// Question 5
// The result of null < 0 is false because null gets converted to 0 and 0 < 0 results in false and undefined < 0 is false because undefined gets converted to NaN and NaN < 0 results in false
// console.log(null < 0);
// console.log(undefined < 0);

// Question 6
let tankCapacity = 500
let waterLevel = 375
let isNotFull = waterLevel < tankCapacity
console.log("Is the tank not full?", isNotFull);

// Question 7
console.log(false < true); // true because false gets converted to 0 and true gets converted to 1 and then 0 < 1 results in true
console.log("5" < "15"); // false false because the each character of first string gets compared to the corresponding character of the second string
console.log(NaN < 10); // false because any comparison with NaN results in false


// 3. Greater Than or Equal To

// Question 1
let marksRequired = 75
let marksScored = 75
let getsDistinction = marksScored >= marksRequired
console.log("Student gets distiction?", getsDistinction);

// Question 2
let ticketPrice = 300
let personBal = 300
let canBuyTicket = personBal >= ticketPrice
console.log("Can they buy the ticket?", canBuyTicket);

// Question 3
console.log(25 >= 25); // true
console.log(30 >= 25); // true
console.log(20 >= 25); // false

// Question 4
console.log("25" >= 25); // true
console.log("10" >= "2"); // false
console.log(null >= 0); // true

// Question 5
// The result of undefined >= 0 is false because undefined gets converted to NaN and any comparison with NaN results in false
// console.log(undefined >= 0);

// Question 6
// A lift can carry maximum 8 people. Currently 8 people are inside. Write a condition using >= to check if the lift is full or overloaded.
// let liftCapacity = 8
// let peopleInside = 8
// let isFull = peopleInside >= liftCapacity
// console.log("Is lift full?", isFull);

// Question 7
console.log(true >= 1); // true because true gets converted to 1 and then 1>=1 results in true
console.log("" >= 0); // true because "" gets converted to 0 and then 0 >= 0 results in true
console.log(NaN >= NaN); // false because any comparison with NaN results in false


// 4. Less Than or Equal To

// Question 1
let maxSpeedLimit = 60
let vehicleSpeed = 60
let isWithinLimit = vehicleSpeed <= maxSpeedLimit
console.log("Is vehicle within speed limit?", isWithinLimit);

// Question 2
let marksPassing = 40
let marksStudent = 39
let isFailed = marksStudent <= (marksPassing-1)
console.log("Has student failed?", isFailed);

// Question 3
console.log(15 <= 20); // true
console.log(20 <= 15); // false
console.log(15 <= 15); // true

// Question 4
console.log("15" <= 20); // true
console.log("30" <= "5"); // true
console.log(null <= 0); // true

// Question 5
// The result of undefined <= 0 is false because undefined gets converted to NaN and any comparison with NaN results in false
// console.log(undefined <= 0);

// Question 6
let bagCapacity = 10
let booksCurrentlyInBag = 10
let canAddBooks = booksCurrentlyInBag <= (bagCapacity-1)
console.log("Can more books be added?", canAddBooks);

// Question 7
console.log(false <= 0); // true because false get converted to 0 and then 0 <= 0 results in true
console.log("" <= 0); // true because "" get converted to 0 and then 0 <= 0 results in true
console.log(NaN <= 5); // false because any comparison with NaN results in false


// Mixed Practice

// Question 1

// Whether age 18 is greater than or equal to voting age 18.
// let votingAge = 18
// let age = 18
// let result = age >= votingAge
// console.log(result);

// Whether temperature 32 is less than 35.
// let temperature1 = 35
// let temperature2 = 32
// let result = temperature2 < temperature1
// console.log(result);

// Whether score 90 is greater than 85.
// let score1 = 85
// let score2 = 90
// let result = score2 > score1
// console.log(result);

// Question 2
console.log(10 > 5 && 5 < 10); // true
console.log("10" >= 10); // true
console.log(null <= undefined); // false
console.log("5" < "10" && 5 > 2); // false

// Question 3
let productCost = 499
let customerBal = 500
let canBuy = customerBal >= productCost  
let isChangeLeft = productCost < customerBal
console.log("Can customer buy the product?", canBuy);
console.log("Will any change be left?", isChangeLeft);

// Question 4
// "10" > "2" is false but 10 > 2 is true because when two strings are compared then each character of the first string is compared to the corresponding character of the second string and when both the operands are numbers then they are compared on their numerical value