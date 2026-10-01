## Part I : Variables (let, var, const)

### Part a — 4 Questions

**1. Personal Information**
Declare variables for `name`, `age`, and `city` using appropriate variable keywords. Assign values and print all three variables.

**2. Change the Score**
Create a variable `score` with the value `50`. Change its value to `80` and print the final value. Use the appropriate keyword for a value that can change.

**3. Constant Value**
Create a constant variable `PI` with the value `3.14`. Print its value. Do not try to change the value.

**4. Uninitialized Variables**
Declare one variable having name `num1` using `var` and one having name `num2` using `let` without assigning values. Print both variables. Then assign values to them and print the values again.

---Answer:
1.const name = "Alex";
let age = 25;
const city = "New York";

console.log(name);
console.log(age);
console.log(city);

2.let score = 50;
score = 80;
console.log(score);

3.const PI = 3.14;

console.log(PI);

4.var num1;
let num2;

console.log(num1); 
console.log(num2);

num1 = 10;
num2 = 20;

console.log(num1); 
console.log(num2);

### Part b — 4 Questions

**5. Choose the Correct Keyword**
Create the following variables using the most appropriate keyword:

* `studentName` — the value will not change
* `marks` — the value may change
* `schoolName` — the value will not change

Assign values to all three variables. Change `marks` and print all variables.

--Answer:

const studentName = "Sarah";
let marks = 85;
const schoolName = "Greenwood High";

// Changing marks
marks = 92;

console.log(studentName); // Output: Sarah
console.log(marks);       // Output: 92
console.log(schoolName);  // Output: Greenwood High

**6. Understand Scope**
Write a program where `var`, `let`, and `const` variables are declared inside an `if` block. Try to access all three variables outside the block. Observe and identify which variables can be accessed.
--Answer:
if (true) {
    var a = "I am var";
    let b = "I am let";
    const c = "I am const";
}

console.log(a);

**7. Test Re-declaration**
Declare a variable named `user` using `var` and declare it again with a different value. Then perform the same experiment using `let`. Observe what happens and identify which declaration allows re-declaration.
--Answer:
var user = "Alice";
var user = "Bob"; 
console.log(user);



**8. Test Re-assignment**
Create three variables using `var`, `let`, and `const`. Assign an initial value to each. Try to change the value of all three variables. Observe which variables allow re-assignment and which one produces an error.

---Answer:
var v = 10;
let l = 20;
const c = 30;

v = 15; // Allowed
l = 25; // Allowed
// c = 35; // TypeError: Assignment to constant variable.

console.log(v, l, c); // Output: 15 25 30

### Part c — 2 Questions

**9. Predict and Explain**
Without running the code, predict the output of each `console.log()` and identify which lines cause errors. Explain your answer using the rules of scope, re-assignment, and variable declaration.

```javascript
var x = 10;

if (true) {
    var x = 20;
    let y = 30;
    const z = 40;
}

console.log(x);
console.log(y);
console.log(z);
```
--Answer:
20
ReferenceError: y is not defined

**10. Fix the Program**
The following program contains multiple errors. Fix the code so that it runs correctly. Make sure your solution follows the rules for **initialization, re-declaration, re-assignment, and scope**.

```javascript
const name;

let age = 20;
let age = 25;

if (true) {
    var city = "Delhi";
    let country = "India";
}

console.log(country);

const score = 50;
score = 80;
```
--Answer:
// 1. const variables must be initialized immediately
const name = "Alex";

// 2. Cannot redeclare 'age' with let in the same scope. Changed to re-assignment.
let age = 20;
age = 25;

let country = "India"; // Moved or kept accessible depending on need

if (true) {
    var city = "Delhi";
    // country is available inside or outside block if declared correctly, 
    // but if we want to log it outside, it needs to be accessible.
}

// 3. country was block-scoped inside the if block earlier. 
// Declaring it outside or keeping it in scope fixes the reference error.
console.log(country);

// 4. Cannot re-assign a const variable. Changed const to let.
let score = 50;
score = 80;

#### Part d — 2 Question 

**11. Predict the Hoisting Behavior**  
Without running the code, predict the output of each `console.log()` and identify which lines cause errors. Explain your answer using the rules of hoisting for `var`, `let`, and `const`.

```javascript
console.log(a);
console.log(b);
console.log(c);

var a = 10;
let b = 20;
const c = 30;
```
--Answer:
undefined
ReferenceError: Cannot access 'b' before initialization
**12. Fix the Hoisting Errors**  
The following program contains errors related to hoisting. Fix the code so that it runs correctly without any errors. Make sure your solution follows the rules of hoisting for `var`, `let`, and `const` (you may reorder declarations/assignments or change keywords only where necessary to make it work properly).

```javascript
console.log(x);
console.log(y);
console.log(z);

var x = "Hello";
let y = "World";
const z = "!";

console.log(x + " " + y + z);
```
--Answer:
var x = "Hello";
let y = "World";
const z = "!";

// Now all variables are hoisted / initialized before being logged
console.log(x);
console.log(y);
console.log(z);

console.log(x + " " + y + z); // Output: Hello World!


**Questions on Primitive vs Non-Primitive Data Types**

---

### Part e — Basic Identification (4 Questions)

**1. Classify the Types**  
Declare one variable of each of the following types and print both the value and its type using `typeof`:
- A whole number  
- A decimal number  
- A piece of text  
- A true/false value
- 
---Answer:
  let wholeNumber = 42;
let decimalNumber = 3.14;
let text = "Hello, JavaScript!";
let isTrue = true;

console.log(wholeNumber, typeof wholeNumber);       // 42 'number'
console.log(decimalNumber, typeof decimalNumber);   // 3.14 'number'
console.log(text, typeof text);                     // Hello, JavaScript! 'string'
console.log(isTrue, typeof isTrue);                 // true 'boolean'

**2. Undefined vs Null**  
Declare two variables:
- `a` using `let` without assigning any value  
- `b` and intentionally assign `null` to it  

Print both variables and their `typeof` results. Explain the difference between `undefined` and `null`.
--Answer:
let a;
let b = null;

console.log(a, typeof a); // undefined 'undefined'
console.log(b, typeof b); // null 'object'

**3. Number Special Values**  
Create variables for the following and print each value along with its type:
- Positive Infinity  
- Negative Infinity  
- Not-a-Number (`NaN`)  
- A large number written with scientific notation (e.g., `2.5e3`)  
- A number written with underscores for readability (e.g., `1_000_000`)
- 
 --Answer:
let posInfinity = Infinity;
let negInfinity = -Infinity;
let notANumber = NaN;
let scientificNum = 2.5e3;      // Evaluates to 2500
let numericSeparator = 1_000_000; // Evaluates to 1000000

console.log(posInfinity, typeof posInfinity);       // Infinity 'number'
console.log(negInfinity, typeof negInfinity);       // -Infinity 'number'
console.log(notANumber, typeof notANumber);         // NaN 'number'
console.log(scientificNum, typeof scientificNum);   // 2500 'number'
console.log(numericSeparator, typeof numericSeparator); // 1000000 'number'

**4. String Styles**  
Create three string variables using:
- Single quotes  
- Double quotes  
- Template literals (backticks) that include another variable  

Print all three strings.

---Answers:
let singleQuoteStr = 'Hello using single quotes';
let doubleQuoteStr = "Hello using double quotes";

let name = "Alex";
let templateLiteralStr = `Hello ${name}, this is a template literal!`;
console.log(singleQuoteStr);
console.log(doubleQuoteStr);
console.log(templateLiteralStr);

### Part f — Advanced Primitive Types (3 Questions)

**5. Symbol Uniqueness**  
Create two Symbols with the same description (`'id'`).  
Compare them using `===` and print the result.  
Then use both Symbols as keys in an object and retrieve the values.  
Explain why the comparison returns `false`.

---Answer:
let sym1 = Symbol('id');
let sym2 = Symbol('id');

console.log(sym1 === sym2); // Output: false

let obj = {
    [sym1]: "Value for sym1",
    [sym2]: "Value for sym2"
};

console.log(obj[sym1]); // Output: Value for sym1
console.log(obj[sym2]);// Output: Value for sym2

**6. BigInt Precision**  
Create a regular `number` with the value `9007199254740991` (Number.MAX_SAFE_INTEGER).  
Add `1`, `2`, and `3` to it and print the results.  
Now create the same value as a `BigInt` and perform the same additions.  
Print the results and explain the difference.

---Answer:
let maxSafe = Number.MAX_SAFE_INTEGER; // 9007199254740991
console.log(maxSafe + 1); // 9007199254740992
console.log(maxSafe + 2); // 9007199254740993 
console.log(maxSafe + 3); // 9007199254740994 

// BigInt Precision Preservation
let bigMaxSafe = 9007199254740991n;
console.log(bigMaxSafe + 1n); // 9007199254740992n
console.log(bigMaxSafe + 2n); // 9007199254740993n
console.log(bigMaxSafe + 3n); // 9007199254740994n


**7. Choose the Correct Type**  
For each description below, write the most appropriate primitive data type and give an example declaration:
- A unique identifier that is never equal to another value with the same description  
- A very large integer that must keep exact precision  
- A variable that has been declared but not yet given a value  
- An intentional empty value

- --Answers:
- 
A unique identifier that is never equal to another value with the same description: Symbol

Example: const id = Symbol('userId');

A very large integer that must keep exact precision: BigInt

Example: const hugeNum = 9007199254740993245n;

A variable that has been declared but not yet given a value: undefined

Example: let status;

An intentional empty value: null

Example: let selectedUser = null;



### Part g — Prediction & Fixing (3 Questions)

**8. Predict the Output**  
Without running the code, predict what each `console.log` will print (value + type). Explain your reasoning.

```javascript
let a;
let b = null;
let c = 42;
let d = "Hello";
let e = true;
let f = Symbol("key");
let g = 123n;

console.log(typeof a, a);
console.log(typeof b, b);
console.log(typeof c, c);
console.log(typeof d, d);
console.log(typeof e, e);
console.log(typeof f, f);
console.log(typeof g, g);


```
---Answers:
  // console.log outputs:
undefined undefined
object null
number 42
string Hello
boolean true
symbol Symbol(key)
bigint 123n

**9. Fix the Code**  
The following program has mistakes related to primitive types. Fix it so that it runs correctly and prints meaningful values.

```javascript
let num = 10;
let text = Hello;
let flag = True;
let empty;
let nothing = Null;
let unique = symbol("id");
let big = 9007199254740991;

console.log(num, text, flag, empty, nothing, unique, big);
```
--Answer:
let num = 10;
let text = "Hello";        // Added quotes
let flag = true;           // Lowercase 'true'
let empty;                 // Undefined variable declaration
let nothing = null;        // Lowercase 'null'
let unique = Symbol("id"); // Capital 'S' for Symbol constructor
let big = 9007199254740991n; // Added 'n' for BigInt or use BigInt()

console.log(num, text, flag, empty, nothing, unique, big);

**10. Primitive vs Non-Primitive**  
Answer the following questions in your own words and give one example for each:

a) What is the main difference between Primitive and Non-Primitive data types?  
b) Why are Numbers, Strings, Booleans, Undefined, Null, Symbol, and BigInt called Primitive?  
c) Give one example of a Non-Primitive data type and explain why it is considered Non-Primitive.


---Answer:
a) 

Primitives hold a single, immutable value directly in memory (and are compared by value). Non-Primitives (like Objects and Arrays) can hold collections of values or complex entities, are mutable, and are stored and compared by reference in memory.

Example: let str = "hello"; (Primitive) vs let obj = {name: "Alex"}; (Non-Primitive).

b)

They are considered the building blocks of data in JavaScript because they contain no properties, methods, or sub-values—they represent single, unchangeable atomic values.

c)

Array (or Object). It is considered non-primitive because it can store multiple values (of any data type) simultaneously, has built-in methods (like .push() or .map()), and is mutable (its contents can be changed without reassigning the variable reference).
