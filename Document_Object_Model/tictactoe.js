var cells = document.querySelectorAll("td");

var restart = document.querySelector("#b");

var player1Turn = true;

function clearBoard() {
  for (var i = 0; i < cells.length; i++) {
      cells[i].textContent = '';
  }
}

restart.addEventListener('click', clearBoard);

function changeMarker() {
  if(this.textContent === '') {
    if (player1Turn) {
      this.textContent = "X";
      player1Turn = false;
    }
    else {
      this.textContent = "O";
      player1Turn = true;
    }
  }
}

// Use a for loop to add Event listeners to all the squares
for (var i = 0; i < cells.length; i++) {
    cells[i].addEventListener('click', changeMarker)
}


function checkWinner(cell) {
  cells = document.querySelectorAll("td");
  if ((cells[0].textContent === cell && cells[1].textContent === cell && cells[2].textContent === cell) ||
    (cells[0].textContent === cell && cells[4].textContent === cell && cells[8].textContent === cell) ||
    (cells[0].textContent === cell && cells[3].textContent === cell && cells[6].textContent === cell)

    var inArow = 0;
    for (var i = 0; i < cells.length; i++) {
      if (cells[i].textContent === cell) {
        inArow++;
      }
      
    }
}
