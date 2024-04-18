
    $(document).ready(function() {
      $("#title").append(res["title"])

      var img_zone = $("<div class='row'></div>")

      var image = $("<img class='col-md-8' src='../" + res['image'] + "'>")
      img_zone.append(image)

      var text_part = $("<div class='col-md-4'></div>")
      $.each(res["text"], function(i) {
        var this_paragraph = $("<p></p>")
        this_paragraph.html(res["text"][i])
        text_part.append(this_paragraph)
      })
      img_zone.append(text_part)
      $("#img_zone").append(img_zone)

      if (next_id == 100) {
        $("#cond_button").click(function() {
          window.location.href = "/"
        })
      } else {
        $("#cond_button").click(function() {
          window.location.href = "/learn/" + next_id
        })
      }
    })