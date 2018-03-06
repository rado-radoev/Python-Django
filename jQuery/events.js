$('h1').click(function() {
  $(this).text("I was cahnged")
})

$("li").click(function() {
  console.log("li was clicked");
})

$('input').eq(0).keypress(function(event){
  if (event.which === 13) {
    $('h3').toggleClass("turnBlue");
  }
})

$('h1').on("mouseenter", function() {
  $(this).toggleClass("turnBlue");
})


$('input').eq(1).on("click", function() {
  $(".container").fadeOut(3000);
})
