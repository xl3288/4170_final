
    $(document).ready(function() {
      var img_zone = $("<div class='row'></div>")

      var image = $("<img class='col-md-8' src='../" + res['image'] + "'>")
      img_zone.append(image)

      var text_part = $("<div class='col-md-4'></div>")
      var title_content = $("<div class='title'></div>")
      title_content.html(res["title"])
      text_part.append(title_content)
      $.each(res["text"], function(i) {
        var this_paragraph = $("<p class='intel_font_text''></p>")
        this_paragraph.html(res["text"][i])

        $.each(res["highlight_text"], function(i, val) {
          var keyword = val
          var rgxp = new RegExp(keyword, 'ig')
          var highlighted = "<span class='highlight'>" + keyword + "</span>"
          this_paragraph.html($(this_paragraph).html().replace(rgxp, highlighted))
        })

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