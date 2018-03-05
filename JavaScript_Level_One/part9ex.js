var firstName = prompt("What is your first name?");
var lastName = prompt("What is your last name?");
var age = prompt("What is your age?");
var height = prompt("How tall are you (in cm)?");
var petName = prompt("What's your pet name?");
alert("Thank you for your participation. \n A memeber of our team will contact you if you are a spy!");

if (firstName[0].toLowerCase() === lastName[0].toLowerCase() &&
    (age > 20 && age < 30) &&
    (height >= 170) &&
    (petName[petName.length -1].toLowerCase() === "y")) {
        console.log("Hello your spiness!");
    }
else {
    console.log("Who are you?");
}
