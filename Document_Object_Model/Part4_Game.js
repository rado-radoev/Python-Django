// Restart Game Button
var restart = document.querySelector('#b');

// Grab all the squares
var squares = document.querySelectorAll("td");


// Clear Squares Function
function clearBoard() {
  for (var i = 0; i < squares.length; i++) {
      squares[i].textContent = '';
  }

}
restart.addEventListener('click',clearBoard)




// Create a function that will check the square marker
function changeMarker(marker, cell){
    if(cell.textContent === ''){
      cell.textContent = marker;
    }
};\

// Use a for loop to add Event listeners to all the squares
for (var i = 0; i < cells.length; i++) {
    cells[i].addEventListener('click', function() {
      changeMarker("X", cells[i])
    });
}
