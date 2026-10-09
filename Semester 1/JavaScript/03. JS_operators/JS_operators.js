// ## A] Arithmetic Operators

// ### 1. Addition `+`

// 1. A school collected ₹15,000 from one class and ₹12,500 from another class. Find the total collection. 
let amount1=15000;
let amount2=12500;
let total_amount=amount1+amount2;
console.log(total_amount)


// 2. A person reads 18 pages in the morning and 25 pages in the evening. Find the total pages read. 
let pagesRead_morning=18;
let pagesRead_evening=25;
let totalPages_read=pagesRead_evening+pagesRead_morning;
console.log(totalPages_read)


// 3. A shop sold 125 items on Monday and 178 items on Tuesday. Find the total items sold. 
let itemsSold_Monday=125;
let itemsSold_Tuesday=178;
let totalItems_Sold=itemsSold_Monday+itemsSold_Tuesday;
console.log(totalItems_Sold)


// 4. Predict the output:
//    ```js
//    let a = "10";
//    let b = 5;
//    let result = a + b;
//    console.log(result);

//Output:
//105


// 5. Predict the output:
//    ```js
//    let x = 5;
//    let y = "3";
//    let result = x + y;
//    console.log(result);
//    ```
//Output:
//53


// 6. What is the output of `15 + 27`? 
//Output:
//42


// 7. Calculate the total price if a book costs ₹350 and a pen costs ₹45.

let costOfBook=350;
let costOfPen=45;
let total_price=costOfBook+costOfPen;
console.log(total_price)


// 8. What is the result of `"25" + 10` and why?  
//Output:
//2510 
//Because whenever  + operator is used between string and a number concatanation happens not addition.



// 9. A person has ₹2000 in their wallet. They buy items worth ₹750 and ₹320. Write an expression using `+` to find the total spent, then calculate the remaining balance.  
let amount=2000;
let item1_cost=750;
let item2_cost=320;
let total_spent=item1_cost+item2_cost;
let balance=amount-total_spent;
console.log(balance)


// 10. Predict the outputs and explain:  
//     ```js
//     console.log(5 + "5" + 5);
//     console.log(5 + 5 + "5");
//     console.log("5" + 5 + 5);
//     ```
//Output :
555 //concatanation
105 //first addition then concatanation
555//concatanation


// ### 2. Subtraction `-`

// 1. A bus has 80 seats, and 53 seats are occupied. Find the number of empty seats.  
let seats=80;
let occupied=53;
let emptySeats=seats-occupied;
console.log(emptySeats)


// 2. A student has 500 marks and loses 35 marks due to incorrect answers. Find the final marks. 
let marks=500;
let loses=35;
let final_marks=marks-loses;
console.log(final_marks)


// 3. A warehouse has 2,500 boxes and sends 875 boxes to a store. Find the remaining boxes. 
let total_boxes=2500;
let box_sent=875;
let remaining_boxes=total_boxes-box_sent;
console.log(remaining_boxes)


// 4. Predict the output:
//    ```js
//    let a = "10";
//    let b = 3;
//    let result = a - b;
//    console.log(result);
//    ```
//Output:
//7

//
// 5. Predict the output:
//    ```js
//    let x = "20";
//    let y = "5";
//    let result = x - y;
//    console.log(result);
//    ```
//output:
//15


// 6. What is the output of `100 - 37`?  
//Output:
//63

// 7. A tank has 500 litres of water. After using 175 litres, how much water is left?  
let litresOfWater=500;
let waterUsed=175;
let waterLeft=litresOfWater-waterUsed;
console.log(waterLeft)




// 8. What is the result of `"50" - 20` and `"50" - "20"`? Explain any difference.  
//Bothgives same result i.e. is 30 for substraction strings act as numbers. 

// 9. A shopkeeper had 240 apples. He sold 95 in the morning and 67 in the evening. Write expressions to find how many apples are left.  
let apples=240;
let soldInmorning=95;
let solInevening=67;
let applesLeft=apples-soldInmorning-solInevening
console.log(applesLeft)

// 10. Predict and explain the outputs:  
//     ```js
//     console.log("100" - 50);    50 ,subtraction is taking place 
//     console.log("abc" - 10);     NaN, not able to subtract number from a string
//     console.log(10 - "5" - "2");   3,normal substraction taking place between strings andd numbers.
//     console.log("10" - "5" - "2");  3,all are strings but behaving as numbers in substraction.

// ### 3. Multiplication `*`

// 1. One notebook costs ₹45. Calculate the cost of buying 8 notebooks. 
let costOfNotebook=45;
let costOf_8_notebooks=8*costOfNotebook
console.log(costOf_8_notebooks) 

// 2. A machine produces 120 bottles per hour. Calculate its production in 6 hours.
let bottlesPer_hour=120;
let production_in_6_hours=6*bottlesPer_hour
console.log(production_in_6_hours)

// 3. A garden has 7 rows with 15 plants in each row. Find the total number of plants. 
let NoOfrows=7;
let NoOfplants=15;
let totalNoOfPlants=NoOfplants*NoOfrows
console.log(totalNoOfPlants)

// 4. Predict the output:
//    ```js
//    let a = "5";
//    let b = 4;
//    let result = a * b;
//    console.log(result);
//    ```
//output: 20
 
// 5. Predict the output:
//    ```js
//    let x = "10";
//    let y = "2";
//    let result = x * y;
//    console.log(result);
//    ```
//output: 20
// 6. What is the output of `12 * 8`? 
//output: 96



// 7. One pizza costs ₹299. What is the total cost of 4 pizzas?  
let costOfPizza=299;
let  total_cost=4*costOfPizza
console.log(total_cost)

// 8. What is the result of `"7" * 6` and `"7" * "6"`?  
//output: 42 both will give same result

// 9. A factory produces 45 units per hour. How many units does it produce in 8 hours? Write the expression and calculate.
let units=45;
let unitsTotal=8*units;  
console.log(unitsTotal)
// 10. Predict and explain the outputs:  
//     ```js
//     console.log("5" * 3 * "2");    30,normally multiplying strings and numbers
//     console.log("abc" * 4);         NaN as abc cannot be multiplied by 4
//     console.log(10 * "2.5");        25,normal multiplication taking place
//     console.log("10" * "2.5" * "0");  0,as strings are multiplying with other and resulting to give 0.
//     ```



// ### 4. Division `/`

// 1. A teacher distributes 144 pencils equally among 12 students. Find the number of pencils each student receives.  
let pencils=144;
let students=12;
let each_student_get=pencils/students
console.log(each_student_get)

// 2. A train travels 360 kilometres in 6 hours. Find its average distance travelled per hour.  
let distance=360;
let time=6;
let speed=distance/time
console.log(speed)
// 3. A company distributes ₹72,000 equally among 9 departments. Find the amount received by each department. 
let money=72000;
let department=9;
let each_department_recieves=money/department;
console.log(each_department_recieves)

// 4. Predict the output:
//    ```js
//    let a = "20";
//    let b = 4;
//    let result = a / b;
//    console.log(result);
//    ```
//output- 5


// 5. Predict the output:
//    ```js
//    let x = "100";
//    let y = "5";
//    let result = x / y;
//    console.log(result);

//   output- 20


// 6. What is the output of `144 / 12`?  
//output- 12


// 7. 360 students are to be divided equally into 9 classrooms. How many students per classroom?
let student=360;
let classrooms=9;
let student_per_classroom=student/classrooms;
console.log(student_per_classroom)


// 8. What is the result of `"100" / 4` and `"100" / "4"`? 
///output: 25 for both

// 9. A total bill of ₹2400 is to be shared equally among 6 friends. Write the expression and find each person’s share.  
let totalBill=24000;
let friends=6;
let each_share=totalBill/friends
console.log(each_share)


// 10. Predict and explain the outputs:  
//     ```js
//     console.log(10 / 0);     
//     console.log(-10 / 0);
//     console.log(0 / 0);
//     console.log("20" / "4" / 2);
//     console.log("abc" / 5);
//     ```

// ---Output:
//  Infinity
// -Infinity
// NaN
// 2.5
// NaN

// ### 5. Modulus `%`

// 1. A teacher has 53 students and forms groups of 5. Find the number of students left over.  

let NoOfStudents=53;
let  groupSize=5;
let Student_left=NoOfStudents/groupSize;
console.log(Student_left)

// 2. A shop has 128 candies and packs 10 candies in each box. Find the number of candies left unpacked.  
let candies=128;
let candies_in_each_box=10;
let candies_left=candies%candies_in_each_box;
console.log(candies_left)

// 3. A factory produces 237 toys and packs them in boxes of 6. Find how many toys are left after packing full boxes. 
let toys= 237;
let boxes=6;
let toys_left=toys%boxes;
console.log(toys_left)

// 4. A bus can carry 40 passengers. If 185 people are waiting, find how many people will be left after filling as many full buses as possible.  
let passengers=40;
let peopleWaiting=185;
let peopleLeft=peopleWaiting%passengers
console.log(peopleLeft)


// 5. Predict the output:
//    ```js
//    let a = 10;
//    let b = 0;
//    let result = a % b;
//    console.log(result);
//    ```
//output: NaN

// 6. What is the output of `29 % 5`?  
//output: 4

// 7. There are 23 chocolates to be packed in boxes of 4. How many chocolates will be left over?  
let chocolates=23;
let box=4;
let chocolates_left=chocolates%box;
console.log(chocolates_left)

// 8. What is the result of `0 % 7` and `15 % 0`? Explain.  
// ouput: 0 and NaN

// 9. A number of pages (47) needs to be printed on sheets that hold 6 pages each. How many full sheets are needed and how many pages will be left over? Write expressions using `%` and `/`.  
let pages=47;
let sheets=6;
let full_sheets_needed=pages/sheets;
console.log(Math.floor(full_sheets_needed))
let pages_left=pages%sheets;
console.log(pages_left)



// 10. Predict and explain the outputs (especially the signs):  
//     ```js
//     console.log(17 % 5);
//     console.log(-17 % 5);
//     console.log(17 % -5);
//     console.log(-17 % -5);
//     console.log(10 % 0);
//     ```

// ---Output:
// 2
// -2
// 2
// -2
// NaN


// ### 6. Exponentiation `**`

// 1. Find the volume of a cube with a side length of 6 cm using `side ** 3`.  
let length=6;
let volume=length**3;
console.log(volume)


// 2. Calculate the total number of cells in a square arrangement with 9 cells on each side using `side ** 2`. 
let cells=9;
let total_cells=cells**2;
console.log(total_cells)


// 3. Find the value of \( 5^4 \) (5 raised to the power 4) using the exponentiation operator.
let base=5;
let power=4;
let exponential=base**power;
console.log(exponential)  

// 4. A digital image has 1,024 pixels on each side (square image). Find the total number of pixels using `pixels ** 2`.  
let pixels=1024;
let pixels_both_side=pixels**2;
console.log(pixels_both_side)

// 5. Predict the output:
//    ```js
//    let base = 2;
//    let power = -1;
//    let result = base ** power;
//    console.log(result);

//    Output:0.5

// 6. What is the output of `3 ** 4`?  
//output:81


// 7. Calculate the area of a square whose side is 9 units using the exponentiation operator.  
let side=9;
let area=side**2;
console.log(area)

// 8. What is the result of `2 ** 5` and `5 ** 2`? Are they the same? 
//output: 32 and 25 .no both are not same.

// 9. Predict and explain the outputs (and any errors):  
//    ```js
//    console.log(2 ** 3 ** 2);          // right-associative
//    console.log((2 ** 3) ** 2);
//    console.log(2 ** -3);
//    // console.log(-2 ** 2);           // Remember: Syntax error
//    console.log((-2) ** 2);
//    console.log(4 ** 0.5);
//    Output:
// 512
// 64
// 0.125
// 4
// 2


// 10. Predict the output:
//     ```js
//     let a = 10;
//     let b = 0;
//     let result = a ** b;
//     console.log(result);
//     ```

// ---Answer:1

// ## B] Assignment Operators

// ### 1. Simple Assignment `=`

// 1. Store a student’s name as `"Priya"` and marks as `92` using the assignment operator.  
let Student_name="priya"
let Marks=92;

// 2. Create a variable `score` and assign it the value `0`.  
let score=0;

// 3. Assign the value `50` to three variables `a`, `b` and `c` using a single chained assignment.
let a,b,c=50;

// 4. Predict the output:
//    ```js
//    let x;
//    x = 100;
//    console.log(x);

//    ``Output:100

// 5. Predict the output:
//    ```js
   let p = 15;
   let q = p;
   q = 30;
   console.log(p, q);
//    ```

// ---Output:15 30


 

// ### 2. Add and Assign `+=`

// 1. A player’s score is `80`. He scores `25` more points. Update the score using `+=`.  
let scores=80;
scores+=25;
console.log(scores)


// 2. A wallet has ₹1500. Cashback of ₹120 is added. Update the balance using `+=`.  
let wallet_money=1500;
wallet_money+=120;
console.log(wallet_money)

// 3. Predict the output:
//    ```js
//    let count = 10;
//    count += 5;
//    console.log(count);
//    ```
//Output: 15

// 4. Predict the output:
//    ```js
//    let msg = "Good";
//    msg += " Morning";
//    console.log(msg);
//    ```
//  Output:Good Morning


// 5. What is the final value after `let n = 20; n += "5";`? Explain.

// ---Answer: 25 as n is already 20 and we are adding 5 to it.

// ### 3. Subtract and Assign `-=`
// 1. Health is `100`. Player takes `35` damage. Update health using `-=`.
let health=100;
health-=35;
console.log(health)  

// 2. Stock of 300 items is reduced by 45 after a sale. Update using `-=`. 
let stock=300;
stock-=45;
console.log(stock) 

// 3. Predict the output:
//    ```js
//    let lives = 5;
//    lives -= 2;
//    console.log(lives);
//    ```
//Output:3


// 4. Predict the output:
//    ```js
//    let num = "40";
//    num -= 15;
//    console.log(num);
//    ```
//Output:25


// 5. What is the result of `let x = "abc"; x -= 5;`? Explain.

// ---ANS: NaN as abc is string and 5 cannot be subtracted from it.




// ### 4. Multiply and Assign `*=`

// 1. Price of an item is ₹500. Apply 18% GST using `*= 1.18`.  
let price=500;
price*=0.18;
console.log(price)

// 2. A quantity of 8 is tripled. Update using `*=`.  
let quantity=4;
quantity*= 3;
console.log(quantity)


// 3. Predict the output:
//    ```js
//    let amount = 200;
//    amount *= 1.1;
//    console.log(amount);
//    ```
//Output:220

// 4. Predict the output:
//    ```js
//    let val = "7";
//    val *= 3;
//    console.log(val);
//    ```
//output:21


// 5. What is the result of `let y = "hello"; y *= 2;`? Explain.

// ---Ans:NaN, multipling a string by the numberr not possible as it is not a number.




// ### 5. Divide and Assign `/=`

// 1. Total of 180 chocolates is shared among 6 children. Update using `/=`.
// Ans:
let chocolate=180;
let children=6;
chocolate/=children;
console.log(chocolate)

// 2. Distance of 300 km is covered in 5 hours. Find average speed using `/=`.  
let Distance=300;
let hours=5;
Distance/=hours;
console.log(Distance)


// 3. Predict the output:
//    ```js
//    let total = 400;
//    total /= 8;
//    console.log(total);
//    ```
//Output:50


// 4. Predict the output:
//    ```js
//    let num = "100";
//    num /= 4;
//    console.log(num);
//    ```
//Output: 25


// 5. What is the result of `let z = 50; z /= 0;`? Explain.
// ---Answer:Infinity




// ### 6. Modulus and Assign `%=`
// 1. Number 47 is divided by 6. Store only the remainder using `%=`. 
let number=47;
number%=6;
console.log(number) 

// 2. Counter is at 23. Keep only the remainder when divided by 12 using `%=`.  
let counter=23;
counter%=12;
console.log(counter)

// 3. Predict the output:
//    ```js
//    let num = 29;
//    num %= 5;
//    console.log(num);
//    ```
// Output: 4


// 4. Predict the output:
//    ```js
//    let x = "17";
//    x %= 3;
//    console.log(x);
//    ```
//output: 2


// 5. What is the result of `let m = 15; m %= 0;`? Explain.

// ---Answer:NaN as whedn we divide 15 by 0 we get infinity.


// ### 7. Exponentiation and Assign `**=`
// 1. Side of a cube is 5. Update it to get the volume using `**= 3`.  

let Side=5;
side**=3;
console.log(side)


// 2. Number 4 needs to be squared. Use `**= 2`.  
let num=4;
num**=2;
console.log(num)


// 3. Predict the output:
//    ```js
//    let base = 2;
//    base **= 5;
//    console.log(base);
//    ```
//Output: 32


// 4. Predict the output:
//    ```js
//    let n = 4;
//    n **= 0.5;
//    console.log(n);
//    ```
//Output:2


// 5. What is the result of `let p = 2; p **= -1;`? Explain.

// ---Ans:
// 0.5  as 2 raised to power -1 is 1/2.




// ## C] Comparison Operators

// ### 1. Loose Equality `==`
// 1. Check whether the string `"25"` is loosely equal to the number `25`. 
console.log("25"==25);  //true
 
// 2. Check if `0 == false` returns true or false. 
console.log(0==false) ;  //true


// 3. Predict the output:
//    ```js
//    console.log(10 == "10");
//    console.log(null == undefined);
//    ```
//Output: true  and true


        
// 4. Predict the output:
//    ```js
//    console.log("" == 0);       //Answer:true
//    console.log([] == false);    //Answer:true
//    ```


// 5. Why does `NaN == NaN` return `false`?
// ---ANSWER: As NaN  refers to not a number so NaN could be any value 



// ### 2. Loose Inequality `!=`


// 1. Check whether `"18" != 18` returns true or false.  
console.log("18"!=18);
// output: false


// 2. A password is stored as `"1234"`. User enters `1234` (number). Will `!=` return true? 

let stored="1234" ;
let entered=1234;
console.log(stored==entered)

//output: true


// 3. Predict the output:
//    ```js
//    console.log(5 != "5");         Answer:false
//    console.log(0 != false);       Answer:false
//    ```



// 4. Predict the output:
//    ```js
//    console.log(null != undefined);        
//    console.log("" != 0);
//    ```
//Answer: false and false



// 5. What does `NaN != NaN` return? Explain.

// ---Answer: true as it is not known which number is it so it considered as they both are not equal.




// ### 3. Strict Equality `===`
// 1. Check whether `"25" === 25` returns true or false. Explain why.  
console.log("25"===25)  //output:false as it checks both value and datatype.

// 2. Check if `0 === false` and `null === undefined`.  
//Output: false and  false 



// 3. Predict the output:
//    ```js
//    console.log(10 === "10");   //false
//    console.log(true === 1);    //false
//    ```



// 4. Predict the output:
//    ```js
//    console.log("" === 0);            //false
//    console.log([] === false);        //false



//    ```
// 5. Why is `===` preferred over `==` in most real-world code?

// ---Answer:Because strict equality checks both datatype and value while loose equality is only checking values .





// ### 4. Strict Inequality `!==`
// 1. Check whether `"18" !== 18` returns true or false. 
console.log("18!==18")   //true


// 2. Check if `0 !== false` and `null !== undefined`.  
console.log(0!==false)   //true
console.log(null!==undefined)     //true

// 3. Predict the output:
//    ```js
//    console.log(5 !=="5");     //true
//    console.log(true !== 1);     //true
//    ```
//
// 4. Predict the output:
//    ```js
//    console.log("" !== 0);       //true
//    console.log(NaN !== NaN);    //true
//    ```
// 5. Write a condition that checks if a variable `input` is strictly not equal to the string `"0"`.
let variable=10
console.log (variable!=="0")