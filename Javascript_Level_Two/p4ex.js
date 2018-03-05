alert("Hello")

var students = [];
var act = "";
while (act.toLowerCase() !== "quit") {
  act = prompt("please choose one of the following actions:\nadd,remove,display or quit")
  if (act.toLowerCase() === "add") {
    var student = prompt("Enter student name");
    students.push(student);
  }
  else if (act.toLowerCase() === "remove") {
    var student = prompt("Enter student name");
    var index = students.indefOf(student);
    students.splice(index, 1);
    }
  }
  else if (act.toLowerCase() === "display") {
    for (s of students) {
      console.log(s + "\n");
    }
  }
  else if (act.toLowerCase() === "quit") {
    break;
  }

}

alert("Goodbye!");
