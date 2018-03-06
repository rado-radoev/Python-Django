var cells = document.querySelectorAll("td");
var restart = document.querySelector("#b");

let isPlayer1Turn = true;
let allowedToEnter = true;

const winCondition = [
  [0,1,2],
  [3,4,5],
  [6,7,8],
  [0,3,6],
  [1,4,7],
  [2,5,8],
  [0,4,8],
  [6,4,2]
]

function clearBoard() {
  for (var i = 0; i < cells.length; i++) {
      cells[i].textContent = '';
      allowedToEnter = true;
      isPlayer1Turn = true;
  }
}

restart.addEventListener('click', clearBoard);

function changeMarker() {
  if(this.textContent === '' && allowedToEnter) {
    if (isPlayer1Turn) {
      this.textContent = "X";
      isPlayer1Turn = false;
    }
    else {
      this.textContent = "O";
      isPlayer1Turn = true;
    }
  }
}

// Use a for loop to add Event listeners to all the squares
for (var i = 0; i < cells.length; i++) {
    cells[i].addEventListener('mousedown', changeMarker);
    cells[i].addEventListener('mouseup', checkWinner);
}


function checkWinner() {
  var tempCells = document.querySelectorAll("td");

  for (let i = 0; i < winCondition.length; i++) {
    var row = winCondition[i];
    var mark = tempCells[row[0]].textContent
    if (mark !== "") {
      if (tempCells[row[0]].textContent === mark && tempCells[row[1]].textContent === mark && tempCells[row[2]].textContent === mark) {
        allowedToEnter = false;
        alert(mark + " is winner");
      }
    }
  }
}
