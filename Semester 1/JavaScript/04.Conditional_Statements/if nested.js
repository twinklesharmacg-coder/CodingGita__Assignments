
// 1. Check if a number is greater than 10.  
//    If yes, then check whether it is divisible by 3 and print the appropriate message.
// Answer:
let num = 12
if (num > 10){
    if (num%3==0){
        console.log(num, "is greater than 10 and also is divisible by 3");
    }
}

// 2. Write a program that first checks if a person is 18 or older.  
//    If yes, then check if they have a voter ID. Print “Can Vote” only if both conditions are true.
//Answer:
let age = 22
let hasVoterId = true
if (age>=18){
    if (hasVoterId==true){
        console.log("Can Vote");
    }
}

// 3. Check if a student has scored 40 or more marks.  
//    If yes, then check if the score is 80 or above and print “Passed with Distinction”.
// Answer:
let score = 95;
if (score>=40){
    if (score>=80){
        console.log("Passed with Distinction");
    }
}


// 4. Create a simple ATM system:  
//    First check if the PIN is correct.  
//    If PIN is correct, then check if the account balance is sufficient for withdrawal.
// Answer:
let pinEntered = 7890
let pinCorrect = 1234
let accountBalance = 10000
let withdrawalAmount = 1000
if (pinEntered == pinCorrect){
    if (withdrawalAmount <= accountBalance){
        console.log("Withdrawal Successful");
    }
}

// 5. Write a program that checks if a year is divisible by 4.  
//    If yes, then further check if it is divisible by 100.  
//    If it is divisible by 100, then check if it is also divisible by 400 to confirm it is a leap year.
// Answer:
let year = 2026
if (year%4==0){
    if (year%100==0){
        if (year%400==0){
            console.log(" It is a Leap year");
        }
    }
}

// 6. Check if a user has entered a valid email (contains “@”).  
//    If yes, then check if the email ends with “.com”.  
//    If both are true, then check if the length of the email is greater than 10 characters and print “Valid Email”.
// Answer:
let emailAddress = "twinkle134@gmail.com"
if (emailAddress.includes("@")){
    if (emailAddress.endsWith(".com")){
        if (emailAddress.length>10){
            console.log("Valid Email");
        }
    }
}

// 7. Write a program for online shopping:  
//    First check if the cart total is ₹1000 or more.  
//    If yes, then check if the user is a premium member.  
//    If the user is premium, give 20% discount, otherwise give 10% discount.  
//    Finally print the final amount after discount.
//  Answer:
let cartTotal = 8000
let isPremiumUser = true
if (cartTotal >= 1000){
    if (isPremiumUser){
        cartTotal = cartTotal - (cartTotal * 0.2)
    }else{
        cartTotal = cartTotal - (cartTotal * 0.1)
    }
}
console.log(cartTotal);

// 8. Check if a number is positive.  
//    If yes, then check whether it is even.  
//    If it is even, then further check if it is divisible by 4 and print “Positive Even and Divisible by 4”.
// Answer:
let number=20;
if (number>0){
    if (number%2==0){
        if (number%4==0){
            console.log("Positive Even and Divisible by 4");
        }
    }
}

// 9. Create a job eligibility checker with multiple conditions:  
//    First check if age is between 21 and 30.  
//    If age is valid, then check if the candidate has a graduation degree.  
//    If the degree is present, then check if the candidate has at least 2 years of experience.  
//    Print “Eligible for Interview” only if all three conditions are true.
// Answer:

let Age = 29;
let hasGraduationDegree = true
let experience = 5
if (Age>21 && Age<30){
    if (hasGraduationDegree){
        if (experience >=2){
            console.log("Eligible for Interview");
        }
    }
}

// 10. Write a nested program for exam eligibility:  
//     First check if the student is present.  
//     If present, then check if internal marks are ≥ 30.  
//     If internal marks are valid, then check if external marks are ≥ 35.  
//     Print “Eligible for Final Exam” only when all conditions are satisfied.
// Answer:

let present=true;
let internalMarks=70;
let externalMarks=80;
if (present){
    if(internalMarks>=30){
        if(externalMarks>=35){
            console.log("Eligible for Final Exam")
        }
    }
}

// ---