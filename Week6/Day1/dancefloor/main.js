
var container = $('.container');

function createGrid(rows, columns) {
  for (var i = 0; i < columns; i++) {
    const columns = $("<div class='RowClass'>")
    for (var j = 0; j <= rows-1; j++) {
      const rows = $(`<div class='ColumnClass cell' id=${i*j}>`)
      columns.append(rows)
    };    
    $(".container").append(columns);
  };
}

function getRandomNumber(num) {
  return Math.round(Math.random() * num);
}

function changeColor()  {
  var element = document.getElementsByClassName("ColumnClass");
  element.classList.toggleClass("newStyleRows")
}

function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}


function changeColors(rows, columns) {
  setInterval(function() {
    // num = getRandomNumber(rows*columns);
    $(".cell").each(function() {
      $(this).css(`background-color`, getRandomColor());  
    }); 
  }, 500);
}

// $(".cell").each(function(index) {
//   addEventListener("click", turnBlack(index));
// })

// function turnBlack(index)  {
//   (this).css(`background-color`, '#004400');
// }

function onClick(){
  $(".cell").each(function() {
    $(this).on('click', function() {
      $(this).css("background-color", "black")
      
      $(this).add("black")
      $(this).toggleClass( "cell", "cell" );
    });
  });
} 

createGrid(10,10)
changeColors(10,3)
onClick()