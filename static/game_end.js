$(document).ready(function() {
  var image = $("<img class='image' src='../static/end/" + end_id + ".png'>")
  if (end_id == 1) {
    var text = $("<div>Congratulations! You won!</div>")
  } else {
    var text = $("<div>Game ended. You lost...</div>")
  }
  $("#img_zone").append(image)
  $("#text_zone").append(text)

  $("#homeBtn").click(function (event) {
    window.location.href = "/"
  })

  $("#restartBtn").click(function (event) {
    window.location.href = "/play"
  })
})