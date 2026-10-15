// ### Part a: 

// 1. Declare a variable `name = "Rahul"` and print its type using `typeof`. 
//Answer:
let name = "Rahul"
console.log(typeof name);

// 2. Declare a variable `age = 25` and print its type.  
//Answer:
let age = 25
console.log(typeof age);


// 3. Declare a variable `isStudent = true` and print its type.  
//Answer:
let isStudent = true
console.log(typeof isStudent);

// 4. Declare a variable `city` (without assigning a value) and print its type.  
//Answer:
let city;
console.log(typeof city)


// 5. Print the type of the value `null`.
//Answer:
console.log(typeof null)


// ### Part b:

// 6. Predict the output:
//    ```js
//    console.log(typeof 42);
//    console.log(typeof "Hello");
//    console.log(typeof true);
//    console.log(typeof undefined);
//    ```
//output: number , string,boolean ,undefined


// 7. Predict the output:
//    ```js
//    console.log(typeof null);
//    console.log(typeof {});
//    console.log(typeof []);
//    ```
//output: object,object,object

// 8. Predict the output:
//    ```js
//    console.log(typeof NaN);
//    console.log(typeof Infinity);
//    console.log(typeof function(){});
//    ```
//output: number,number,function

// 9. Create three variables:
//    - `price = 99.99`
//    - `message = "Welcome"`
//    - `isActive = false`  
//    Print the type of each variable with a clear message.

let price = 99.99
let message = "Welcome"
let isActive = false
console.log("The type of", price, "is", typeof price);
console.log("The type of", message, "is", typeof message);
console.log("The type of", isActive, "is", typeof isActive);



// 10. Predict the output:
//     ```js
//     let value = null;
//     console.log(typeof value); //object
//     console.log(typeof value === "object");   //true
//     ```

// ### Part c:

// 11. Predict the output:
//     ```js
//     console.log(typeof typeof 100);   //string
//     console.log(typeof typeof "Hi");   //string
//     console.log(typeof typeof true);   //string
//     ```

// 12. Predict the output:
//     ```js
//     let a = 10;
//     let b = "10";
//     console.log(typeof a === typeof b);   //false
//     console.log(typeof a == typeof b);    //false
//     ```

// 13. Predict the output:
//     ```js 
//     console.log(typeof null === "object");   //true
//     console.log(typeof [] === "object");     //true
//     console.log(typeof {} === "object");      //true
//     ```

// 14. Predict the output:
//     ```js
//     let x;
//     console.log(typeof x);   //undefined
//     x = null;
//     console.log(typeof x);   //object
//     x = 0;
//     console.log(typeof x);    //number
//     ```

// 15. Predict the output:
//     ```js
//     console.log(typeof NaN === "number");          //true
//     console.log(typeof Infinity === "number");      //true
//     console.log(typeof (1 / 0));                   //number
//     ```
// ---
