// ## Part H]: Type Coercion

// ### Part a:

// 1. Convert the string `"25"` into a number using `Number()` and add `10` to it. Print the result.
//Answer:
let string = "25"
string = Number(string)
string += 10
console.log(string);


// 2. Convert the number `100` into a string using `String()` and join it with `" rupees"`. Print the result.
//Answer:  
let number = 100
number = number(number)
number += " rupees"
console.log(number);


// 3. Convert the value `0` into a boolean using `Boolean()` and print it.  
//Answer:
let value = 0
value = Boolean(value)
console.log(value);

// 4. Convert the value `"Hello"` into a boolean and print it. 
//Answer:
let val = "Hello"
val = Boolean(val)
console.log(val);


// 5. Use the unary `+` operator to convert `"50"` into a number and multiply it by `2`.
//Answer:
let str = "50"
str = +str
str *= 2
console.log(str);

// ### Part b:

// 6. Predict the output:
//    ```js
//    console.log("10" - 5);   //5
//    console.log("10" + 5);   //105
//    console.log("10" * 2);   //20
//    console.log("10" / 2);   //5
//    ```
//Answer:

// 7. Predict the output:
//    ```js
//    console.log("5" - "2");   //3
//    console.log("5" + "2");   //52
//    console.log("5" * "2");   //10
//    console.log("5" / "2");   //2.5
//    ```

// 8. Predict the output:
//    ```js
//    console.log(Number("123"));    //123
//    console.log(Number("123abc"));  //NaN
//    console.log(Number(true));      //1
//    console.log(Number(false));     //0
//    console.log(Number(null));      //0
//    console.log(Number(undefined)); //NaN
//    ```

// 9. Predict the output:
//    ```js
//    console.log(Boolean(0));      //false
//    console.log(Boolean(""));     //false
//    console.log(Boolean("0"));     //true
//    console.log(Boolean([]));      //true
//    console.log(Boolean({}));      //true
//    console.log(Boolean(null));    //false
//    ```

// 10. Predict the output:
//     ```js
//     console.log(String(100));     //"100"
//     console.log(String(true));    //"true"
//     console.log(String(null));    //"null"
//     console.log(String(undefined));    //"undefined"
//     console.log(100 + "");             //"100"
//     ```

// ### Part c:

// 11. Predict the output:
//     ```js
//     console.log("5" + 3 + 2);         //"532"
//     console.log(5 + 3 + "2");         //"532"
//     console.log("5" - 3 + 2);         //4
//     console.log(5 - "3" + "2");       //22
//     ```

// 12. Predict the output:
//     ```js
//     console.log(true + true);        //2 
//     console.log(true + false);       //1
//     console.log(true + "false");     //truefalse
//     console.log(false + "true");     //falsetrue
//     ```

// 13. Predict the output:
//     ```js
//     console.log(null + 5);          //5
//     console.log(undefined + 5);     //NaN
//     console.log(null + "5");        //"null5"
//     console.log(undefined + "5");   //"undefined5"
//     ```

// 14. Predict the output:
//     ```js
//     console.log([] + []);             
//     console.log([] + {});
//     console.log({} + []);
//     console.log({} + {});
//     ```

// 15. Predict the output:
//     ```js
//     let a = "10";
//     let b = 5;
//     let c = a + b;
//     let d = a - b;
//     let e = +a + b;
//     console.log(c, typeof c);     //105, string
//     console.log(d, typeof d);      //5,number
//     console.log(e, typeof e);       //15 ,  number
//     ```

// 16. Predict the output:
//     ```js
//     console.log(!!"Hello");    //true
//     console.log(!!"");         //false
//     console.log(!!0);          //false
//     console.log(!!1);          //true
//     console.log(!!null);       //false
//     console.log(!!undefined);   //false
//     ```

// 17. Predict the output:
//     ```js
//     console.log(Number(""));   //0
//     console.log(Number(" "));   //0
//     console.log(Number("0"));    //0
//     console.log(Number("  25  "));  //25
//     console.log(Number("25px"));    //NaN
//     ```

// 18. Predict the output:
//     ```js
//     let val1 = "5";
//     let val2 = 2;
//     console.log(val1 + val2);    //52
//     console.log(+val1 + val2);   //7
//     console.log(val1 - val2);    //3
//     console.log(val1 * val2);   //10
//     console.log(val1 / val2);    //2.5
//     ``` 

// ---

// # Bonus Mixed Practice Questions:

// 19. Predict the output:
//     ```js
//     let count = 5;         
//     console.log(typeof count++); //number
//     console.log(count);    //6
//     console.log(typeof ++count);  //number
//     console.log(count);   //7
//     ```

// 20. Predict the output:
//     ```js
//     let x = "10";
//     let y = ++x;
//     console.log(x, y, typeof x, typeof y);    //11  11 number number
//     ```

// 21. Predict the output:
//     ```js
//     let a = "5";      
//     let b = a++;
//     console.log(a, b, typeof a, typeof b);      6 5 number number
//     ```

// 22. Predict the output:
//     ```js
//     console.log(typeof (1 + "2"));  //string
//     console.log(typeof (1 - "2"));  //number
//     console.log(typeof (1 * "2"));  //number
//     console.log(typeof (1 / "2"));   //number
//     ```

// 23. Predict the output:
//     ```js
//     let val = null;         
//     console.log(typeof val);  //object
//     console.log(val + 1);     //1
//     console.log(val - 1);     //-1
//     console.log(val * 1);      //0
//     console.log(Boolean(val));  //false
//     ```
