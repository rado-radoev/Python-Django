var cells = document.querySelectorAll("td");

var restart = document.querySelector("#b");

function clearBoard() {
  for (var i = 0; i < cells.length; i++) {
      cells[i].textContent = '';
  }
}


restart.addEventListener('click', clearBoard);

// Create a function that will check the square marker
function changeMarker(marker){
    if(this.innerHTML === '') {
      this.innerHTML = marker;
    }
}

// Use a for loop to add Event listeners to all the squares
for (var i = 0; i < cells.length; i++) {
    cells[i].addEventListener('click', function() {changeMarker("X")});
}
