
## Section A: Short Answer Questions (1 Mark each)

**Q1.** What is JavaScript?

**Q2.** Who created JavaScript and in which year?

**Q3.** What was the original name of JavaScript?

**Q4.** Is JavaScript the same as Java? Give one major difference.

**Q5.** What does it mean when we say JavaScript is a **high-level** programming language?

**Q6.** Is JavaScript a compiled language or an interpreted language? Explain briefly.

**Q7.** Name the JavaScript engines used by the following browsers:
- Google Chrome
- Mozilla Firefox
- Apple Safari

**Q8.** What is **Dynamic Typing** in JavaScript?

**Q9.** What is the main difference between a **static** website and a **dynamic** website?

**Q10.** Name the three pillars of Front-end Web Development and write one line about each.

**Q11.** What is the difference between Frontend and Backend?

**Q12.** What is Node.js?

**Q13.** Explain **ECMAScript**. What is its relation with JavaScript?

---Answer:
<img width="854" height="1279" alt="image" src="https://github.com/user-attachments/assets/9bd085bb-5455-4c18-a01a-5fde13a03bfd" />
<img width="1124" height="1279" alt="image" src="https://github.com/user-attachments/assets/64e2298f-a16c-46af-aa12-e177ac440126" />
<img width="874" height="1279" alt="image" src="https://github.com/user-attachments/assets/674a5a3f-2383-48f9-85d6-34743356b72c" />




## Section B: True or False  
(Write True or False. If False, correct the statement)

1. JavaScript is a statically typed language.
2. JavaScript can only run inside the browser.
3. HTML is responsible for the behaviour of a webpage.
4. Node.js allows JavaScript to run outside the browser.
5. JavaScript is case-insensitive.
6. `let name` and `let Name` are the same variable.
7. ECMAScript is a programming language.
8. React, Angular, and Vue.js are used for Backend development.

---Answer:
<img width="742" height="1279" alt="image" src="https://github.com/user-attachments/assets/44502dc0-8fef-474a-9bfa-cd4d361395f8" />


## Section C: Fill in the Blanks

1. JavaScript was created by ______________ in the year ______________.
2. The three technologies used in Front-end development are __________, __________, and __________.
3. JavaScript engines: Chrome uses __________, Firefox uses __________.
4. In the restaurant analogy: Customer = __________, Waiter = __________, Chef = __________.
5. JavaScript file extension is __________.

---Answer:
<img width="514" height="1281" alt="image" src="https://github.com/user-attachments/assets/73e84f48-5f69-4ced-8549-4897b2a674ea" />


## Section D: Conceptual Questions (2 Marks each)

**Q14.** Differentiate between a **static website** and a **dynamic website**. Give one real-world example of each.

**Q15.** Explain any two features of JavaScript that make it suitable for creating interactive web pages.

**Q16.** List any four areas (apart from web browsers) where JavaScript is used today. Mention one popular framework/library for each (if applicable).

**Q17.** What is the difference between writing JavaScript code:
- Inside an HTML file using `<script>` tag, and
- In an external `.js` file?  
Mention two advantages of using an external JavaScript file.

**Q18.** Explain the difference between Frontend and Backend using the **restaurant analogy** in your own words.

**Q19.** Why should a beginner learn JavaScript? Write at least 4 points.

---Answer:
<img width="1228" height="1279" alt="image" src="https://github.com/user-attachments/assets/e617c687-66de-4d6c-b76b-90514cbd61e2" />
<img width="910" height="1281" alt="image" src="https://github.com/user-attachments/assets/efb42901-0ab1-4f4c-a22e-da0617e4ba46" />
<img width="862" height="1280" alt="image" src="https://github.com/user-attachments/assets/71e05839-7fd8-4e97-b4cb-3681a828e649" />



## Section E: Code-Based Questions (3 Marks each)

**Q20.** Predict the output of the following code and explain why:

```javascript
let value = 25;
console.log(typeof value);
value = "JavaScript";
console.log(typeof value);
value = false;
console.log(typeof value);
```
--Answer:
Output:
number
string
boolean

**Q21.** Write a simple HTML + JavaScript program that displays an alert box with the message **"Welcome to JavaScript!"** when a button is clicked.
--Answer:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome Alert</title>
</head>
<body>

    <!-- Button that triggers the JavaScript function when clicked -->
    <button onclick="showAlert()">Click Me</button>

    <script>
        // JavaScript function to display the alert box
        function showAlert() {
            alert("Welcome to JavaScript!");
        }
    </script>

</body>
</html>

**Q22.** Write JavaScript code to demonstrate **event-driven programming**.  
When a user clicks a button with id `"myBtn"`, the text of a paragraph with id `"demo"` should change to `"Button was clicked!"`.

---Answer:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event-Driven Programming Example</title>
</head>
<body>

    <!-- Button with id "myBtn" -->
    <button id="myBtn">Click Me</button>

    <!-- Paragraph with id "demo" -->
    <p id="demo">Initial text...</p>

    <script>
        // Select the button and paragraph elements from the DOM
        const button = document.getElementById("myBtn");
        const paragraph = document.getElementById("demo");

        // Attach a click event listener to the button
        button.addEventListener("click", function() {
            paragraph.textContent = "Button was clicked!";
        });
    </script>

</body>
</html>


## Section F: Practical / Application Based (5 Marks)

**Q23.** Create a complete web page (HTML + JavaScript) that includes the following:

1. A heading: **"My First JavaScript Page"**
2. A button labeled **"Click Me"**
3. When the button is clicked:
   - Show an alert: `"Hello, B.Tech Student!"`
   - Change the background color of the page to light blue
4. Also print `"JavaScript is running successfully!"` in the browser console.

**Write the complete code** (you can use Inline or External JavaScript).

---Answer:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First JavaScript Page</title>
</head>
<body>

    <!-- 1. Heading -->
    <h1>My First JavaScript Page</h1>

    <!-- 2. Button labeled "Click Me" -->
    <button id="actionBtn">Click Me</button>

    <script>
        // Print message to the browser console
        console.log("JavaScript is running successfully!");

        // Select the button element
        const button = document.getElementById("actionBtn");

        // Add a click event listener to handle requirements when clicked
        button.addEventListener("click", function() {
            // 3a. Show an alert
            alert("Hello, B.Tech Student!");

            // 3b. Change the background color of the page to light blue
            document.body.style.backgroundColor = "lightblue";
        });
    </script>

</body>
</html>

## Section G: Higher Order Thinking (Bonus - 3 Marks)

**Q24.** JavaScript was originally created only for browsers. Today it is used in frontend, backend, mobile apps, desktop apps, and even AI/ML.  
In your own words, explain why JavaScript became so popular and multipurpose. Mention the role of **Node.js** and **ECMAScript** updates in this growth.

---Answer:
<img width="872" height="1279" alt="image" src="https://github.com/user-attachments/assets/536199d1-3a07-403b-8523-2cbd7cbe7c6d" />
<img width="822" height="1281" alt="image" src="https://github.com/user-attachments/assets/19aeba0b-9350-4370-8394-cd0af2644ae6" />

