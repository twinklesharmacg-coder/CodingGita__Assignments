
// 1. Write a program that takes a month number (1–12) and prints the number of days in that month using `switch`  
//    (Hint: Consider 28/29 for February as 28 for simplicity).
// Answer:
let month = 10

switch (true){
    case month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12: 
        console.log("31 days");
        break;
    case  month == 4 || month == 6 || month == 9 || month == 11:
        console.log("30 days");
        break;
    case  month == 2:
        console.log("28 days");
        break;
    default:
        console.log("Invalid month number!");
}



// 2. Write a program that checks a character and prints whether it is a vowel or consonant using `switch`.
// Answer:
let character = "a"
switch (true){
    case character == "a" || character == "e" || character == "i" || character == "o" || character == "u" || character == "A" || character == "E" || character == "I" || character == "O" || character == "U":
        console.log("Vowel");
        break;
    default:
        console.log("Consonant");
}

// 3. Create a program that takes a number from 1 to 4 and prints the season using multiple cases together:  
//    1 or 2 → Winter  
//    3 or 4 → Summer
// Answer:
let number = 2;

switch (true){
    case number == 1 || number == 2:
        console.log("Winter");
        break;
    case number == 3 || number == 4:
        console.log("Summer");
        break;
    default:
        console.log("Invalid Number!");
}


// 4. Write a program using `switch (true)` to assign class based on marks:  
//    ≥ 75 → Distinction  
//    ≥ 60 → 1st class  
//    ≥ 50 → 2nd class  
//    ≥ 35 → 3rd class  
//    below 35 → Failed
// Answer:
let marks = 65
switch (true){
    case marks>=75:
        console.log("Distinction");
        break;
    case marks>=60:
        console.log("1st class");
        break;
    case marks>=50:
        console.log("2nd class");
        break;
    case marks>=35:
        console.log("3rd class");
        break;
    default:
        console.log("Failed");
}

// 5. Create a nested `switch` program:  
//    First take a role (“admin” or “user”).  
//    If role is “admin”, then take an action (“create”, “edit”, “delete”) and print the corresponding message.  
//    If role is “user”, print “Limited Access”.
// Answer:
let role = "admin"

switch (role){
    case "admin":
        let action = "create"
        switch (action) {
            case "create":
                console.log("Create");
                break;
            case "edit":
                console.log("Edit");
                break;
            case "delete":
                console.log("Delete");
                break;
        }
        break;
    case "user":
        console.log("Limited Access");
        break;
}


// 6. Predict and explain the output of the following code. Then correct it so that only one message is printed:
// ```js
// let fruit = "mango";

// switch (fruit) {
//   case "apple":
//     console.log("Apple is red");
//   case "mango":
//     console.log("Mango is yellow");
//   case "banana":
//     console.log("Banana is yellow");
//   default:
//     console.log("Unknown fruit");
// }
// ```

//Output:
// Mango is yellow
// Banana is yellow
// Unknown fruit
//Reason: as there is no break so execution will continue till end of the code.

// Correct code:
let fruit = "mango";

switch (fruit) {
  case "apple":
    console.log("Apple is red");
    break;
  case "mango":
    console.log("Mango is yellow");
    break;
  case "banana":
    console.log("Banana is yellow");
    break;
  default:
    console.log("Unknown fruit");
}

// Output:
// Mango is yellow



// 7. Write a program that takes a value which can be either a number or a string (`0`, `"0"`, `false`, `null`, `undefined`) and uses `switch` to correctly identify each one. Explain why some values may not match as expected.
// Answer:
let value = null
switch (value){
    case 0:
        console.log("Value is 0");
        break;
    case "0":
        console.log("Value is 0 as a string");
        break;
    case null:
        console.log("Value is null");
        break;
    case false:
        console.log("Value is false");
        break;
    case undefined:
        console.log("Value is undefined");
        break;
    default:
        console.log("Invalid Value");
}

// 8. Create a tricky calculator using `switch` that supports these operations:  
//    `+`, `-`, `*`, `/`, `%`, and also `**` (exponentiation).  
//    Handle division by zero properly inside the corresponding case.
// Answer:
let operator="/"
let a=4
let b=6
switch(operator){
    case "+":
        console.log(a+b);
        break;
    case"-":
        console.log(a-b);
        break;
    case"*":
        console.log(a*b);
        break;
    case "**":
         console.log(num1 ** num2);
         break; 
    case "/":
        switch(b){
            case 0:
                console.log("cannot be divided by zero")
                break;
            default:
                console.log(a/b);
                break;
        }
        break;
    default:
        console.log("Invalid operator")

    
}

// 9. Write a program using `switch` that takes a date (day number of the month) and prints:  
//    “Beginning of the month” (1–10)  
//    “Middle of the month” (11–20)  
//    “End of the month” (21–31)  
//    Use `switch (true)` technique for range checking.
// Answer:

let date = 10

switch (true){
    case date>=1 && date<=10:
        console.log("Beginning of the month");
        break;
    case date>=11 && date<=20:
        console.log("Middle of the month");
        break;
    case date>=21 && date<=31:
        console.log("End of the month");
        break;
    default:
        console.log("Invalid Date!");
}



// 10. Create a multi-level nested `switch` program for an online food ordering system:  
//     First select Category: `"veg"` or `"nonveg"`.  
//     Then select Item based on category.  
//     Finally select Size: `"half"` or `"full"` and print the final order summary with price.

// ---
// Answer:
let category = "veg";
let item = "fried rice"
let size = "half"
let price;

switch (category){
    case "veg":
        switch (item){
            case "noodles":
                price=220

                switch (size){
                    case "half":
                        price *= 0.5
                        console.log("Category:", category);
                        console.log("Item:", item);
                        console.log("Size:", size);
                        console.log("Price:", price);
                        break;
                    case "full":
                        price *= 1
                        console.log("Category:", category);
                        console.log("Item:", item);
                        console.log("Size:", size);
                        console.log("Price:", price);
                        break;
                    default:
                        console.log("Invalid Size!");
                }
                break;

            case "fried rice":
                price = 200
               

                switch (size){
                    case "half":
                        price *= 0.5
                        console.log("Category:", category);
                        console.log("Item:", item);
                        console.log("Size:", size);
                        console.log("Price:", price);
                        break;
                    case "full":
                        price *= 1
                        console.log("Category:", category);
                        console.log("Item:", item);
                        console.log("Size:", size);
                        console.log("Price:", price);
                        break;
                    default:
                        console.log("Invalid Size!");
                }
                break;

            case "dal makhani":
                price = 180;
                

                switch (size){
                    case "half":
                        price *= 0.5
                        console.log("Category:", category);
                        console.log("Item:", item);
                        console.log("Size:", size);
                        console.log("Price:", price);
                        break;
                    case "full":
                        price *= 1
                        console.log("Category:", category);
                        console.log("Item:", item);
                        console.log("Size:", size);
                        console.log("Price:", price);
                        break;
                    default:
                        console.log("Invalid Size!");
                }
                break;
            default:
                console.log("Invalid Item!");
        }
        break;

    case "nonveg":
       
        switch (item){
            case "butter chicken":
                price = 370
              

                switch (size){
                    case "half":
                        price *= 0.5
                        console.log("Category:", category);
                        console.log("Item:", item);
                        console.log("Size:", size);
                        console.log("Price:", price);
                        break;
                    case "full":
                        price *= 1
                        console.log("Category:", category);
                        console.log("Item:", item);
                        console.log("Size:", size);
                        console.log("Price:", price);
                        break;
                    default:
                        console.log("Invalid Size!");
                }
                break;
            case "roasted chicken":
                price = 350
                

                switch (size){
                    case "half":
                        price *= 0.5
                        console.log("Category:", category);
                        console.log("Item:", item);
                        console.log("Size:", size);
                        console.log("Price:", price);
                        break;
                    case "full":
                        price *= 1
                        console.log("Category:", category);
                        console.log("Item:", item);
                        console.log("Size:", size);
                        console.log("Price:", price);
                        break;
                    default:
                        console.log("Invalid Size!");
                }
                break;
            case "chicken tandoori":
                price = 220
            

                switch (size){
                    case "half":
                        price *= 0.5
                        console.log("Category:", category);
                        console.log("Item:", item);
                        console.log("Size:", size);
                        console.log("Price:", price);
                        break;
                    case "full":
                        price *= 1
                        console.log("Category:", category);
                        console.log("Item:", item);
                        console.log("Size:", size);
                        console.log("Price:", price);
                        break;
                    default:
                        console.log("Invalid Size!");
                }
                break;
            default:
                console.log("Invalid Item!");
        }
        break;
    default:
        console.log("Invalid Category");
}