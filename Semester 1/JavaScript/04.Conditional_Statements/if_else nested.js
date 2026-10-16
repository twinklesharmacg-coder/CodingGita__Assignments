// 1. Write a program that takes a month number (1–12) and prints the corresponding season:  
//    Winter (12, 1, 2), Summer (3, 4, 5), Monsoon (6, 7, 8), Autumn (9, 10, 11).

//Answer:
let month_number=1;
if (month_number==1 || month_number==2 || month_number==12){
    console.log("winter");
}
else if (month_number==3 || month_number==4 || month_number==5){
    console.log("Summer")
} else if(month_number==6 || month_number==7 || month_number==8){
    console.log("Monsoon")
} else {
    console.log("Autumn")
}


// 2. Create a simple tax calculator based on income:  
//    Income < 3,00,000 → No tax  
//    3,00,000 – 7,00,000 → 5% tax  
//    7,00,000 – 10,00,000 → 10% tax  
//    Above 10,00,000 → 15% tax  
//    Print the tax amount.

//Answer:
let income = 365_000
if (income<700_000 && income>=300_000) {
    taxAmt = income * 0.05
    console.log(taxAmt);
} else if (income<1_000_000 && income>=700_000) {
    taxAmt = income * 0.1
    console.log(taxAmt);
} else if (income>1_000_000) {
    taxAmt = income * 0.15
    console.log(taxAmt);
} else {
    console.log("No tax");
}

// 3. Write a program that checks a student’s score and prints:  
//    “Outstanding” (90 and above), “Good” (70–89), “Average” (40–69), “Needs Improvement” (below 40).

//Answer:
let score = 78
if (score>=90){
    console.log("Outstanding");
}else if (score>=70 && score<=89){
    console.log("Good");
}else if (score>=40 && score<=69){
    console.log("Average");
}else{
    console.log("Needs Improvement");
}

// 4. Check the speed of a vehicle and print:  
//    “Slow” (below 40), “Normal” (40–80), “Fast” (above 80).
//Answer:
let speed=80;
if (speed>80){
    console.log("Fast")
}else if (speed<=80 && speed>=40){
    console.log("Normal")
}else{
    console.log("slow")
}

// 5. Write a program that checks a person’s height (in cm) and prints:  
//    “Short” (< 150), “Average” (150–170), “Tall” (> 170).
//Answer:
let height=170;
if (height>=170){
    console,log("Tall")
}else if (height>=150){
    console.log("Average")

}else{
    console.log("Short")
}

// 6. Check the day number (1–7) and print whether it is a Weekday or Weekend  
//    (1 to 5 = Weekday, 6 and 7 = Weekend).
//Answer:
let day=4;
if (day==6 || day==7){
    console.log("weekend")
}else if(day>=1 && day<=5){
    console.log("weekday")
}else{
    console.log("Invalid Day")
}


// 7. Write a program that calculates electricity bill based on units:  
//    0–50 units → ₹2 per unit  
//    51–150 units → ₹4 per unit  
//    Above 150 units → ₹6 per unit  
//    Print the total bill.
//Answer:
let units = 47
let totalBill
if (units>=150){
    totalBill = units * 6
}else if (units>=51){
    totalBill = units * 4
}else if (units>=0){
    totalBill = units * 2
}else{
    console.log("Invalid Value")
}
console.log(totalBill);

// 8. Create a program that checks a student’s attendance percentage and prints:  
//    “Excellent” (≥ 90), “Good” (75–89), “Satisfactory” (50–74), “Poor” (< 50).
//Answer:
let attendance = 99
if (attendance>=90){
    console.log("Excellent");
}else if (attendance>=75){
    console.log("Good");
}else if (attendance>=50){
    console.log("Satisfactory");
}else{
    console.log("Poor");
}

// 9. Write a program that takes three subject marks and finds the highest mark among them using `if...else if...else`.
let marks1 = 65
let marks2 = 85
let marks3 = 23
if (marks1>marks2 && marks1 > marks3){
    console.log(marks1);
}else if (marks2>marks1 && marks2 > marks3){
    console.log(marks2);
}else{
    console.log(marks3);
}


// 10. Check a number and print one of the following:  
//     “Positive Even”, “Positive Odd”, “Negative Even”, “Negative Odd”, or “Zero”.
// Answer:
let num = -121
if (num>0 && num%2==0) {
    console.log("Positive Even");
} else if (num>0 && num%2==1) {
    console.log("Positive Odd");
} else if (num<0 && num%2==0) {
    console.log("Negative Even");
} else if (num<0 && (num%2==-1)) {
    console.log("Negative Odd");
} else {
    console.log("Zero");
}
// ---


