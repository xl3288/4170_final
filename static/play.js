
  function display_board(board_state) {
    $("#three_star_zone").empty()
    $("#two_star_zone").empty()
    $("#one_star_zone").empty()
    $("#coin_zone1").empty()
    $("#coin_zone2").empty()
    $("#coin_num_zone").empty()
    $("#oppo_token_zone").empty()
    $("#oppo_bonus_zone").empty()
    $("#oppo_point_zone").empty()
    $("#my_token_zone").empty()
    $("#my_bonus_zone").empty()
    $("#my_point_zone").empty()
    $("#oppo_action_zone").empty()

    var three_star_zone = $("<div class='row'></div>")
    var three_star_back = $("<img class='col-md-2' src='../" + card_dict['back']['3-star'] + "'>")
    var three_star_1 = $("<img class='col-md-2' src='../" + board_state['revealed_cards'][2][0]['file_path'] + "'>")
    var three_star_2 = $("<img class='col-md-2' src='../" + board_state['revealed_cards'][2][1]['file_path'] + "'>")
    var three_star_3 = $("<img class='col-md-2' src='../" + board_state['revealed_cards'][2][2]['file_path'] + "'>")
    var three_star_4 = $("<img class='col-md-2' src='../" + board_state['revealed_cards'][2][3]['file_path'] + "'>")
    three_star_zone.append(three_star_back)
    three_star_zone.append(three_star_1)
    three_star_zone.append(three_star_2)
    three_star_zone.append(three_star_3)
    three_star_zone.append(three_star_4)
    $("#three_star_zone").append(three_star_zone)

    var two_star_zone = $("<div class='row'></div>")
    var two_star_back = $("<img class='col-md-2' src='../" + card_dict['back']['2-star'] + "'>")
    var two_star_1 = $("<img class='col-md-2' src='../" + board_state['revealed_cards'][1][0]['file_path'] + "'>")
    var two_star_2 = $("<img class='col-md-2' src='../" + board_state['revealed_cards'][1][1]['file_path'] + "'>")
    var two_star_3 = $("<img class='col-md-2' src='../" + board_state['revealed_cards'][1][2]['file_path'] + "'>")
    var two_star_4 = $("<img class='col-md-2' src='../" + board_state['revealed_cards'][1][3]['file_path'] + "'>")
    two_star_zone.append(two_star_back)
    two_star_zone.append(two_star_1)
    two_star_zone.append(two_star_2)
    two_star_zone.append(two_star_3)
    two_star_zone.append(two_star_4)
    $("#two_star_zone").append(two_star_zone)

    var one_star_zone = $("<div class='row'></div>")
    var one_star_back = $("<img class='col-md-2' src='../" + card_dict['back']['1-star'] + "'>")
    var one_star_1 = $("<img class='col-md-2' src='../" + board_state['revealed_cards'][0][0]['file_path'] + "'>")
    var one_star_2 = $("<img class='col-md-2' src='../" + board_state['revealed_cards'][0][1]['file_path'] + "'>")
    var one_star_3 = $("<img class='col-md-2' src='../" + board_state['revealed_cards'][0][2]['file_path']+ "'>")
    var one_star_4 = $("<img class='col-md-2' src='../" + board_state['revealed_cards'][0][3]['file_path'] + "'>")
    one_star_zone.append(one_star_back)
    one_star_zone.append(one_star_1)
    one_star_zone.append(one_star_2)
    one_star_zone.append(one_star_3)
    one_star_zone.append(one_star_4)
    $("#one_star_zone").append(one_star_zone)

    var coin_zone = $("<div class='row'></div>")
    var coin_white = $("<img class='col-md-2' id='coins' src='../" + card_dict['coin']['white'] + "'>")
    var coin_red = $("<img class='col-md-2' id='coins' src='../" + card_dict['coin']['red'] + "'>")
    var coin_green= $("<img class='col-md-2' id='coins' src='../" + card_dict['coin']['green'] + "'>")
    var coin_blue = $("<img class='col-md-2' id='coins' src='../" + card_dict['coin']['blue'] + "'>")
    var coin_black = $("<img class='col-md-2' id='coins' src='../" + card_dict['coin']['black'] + "'>")
    coin_zone.append(coin_white)
    coin_zone.append(coin_red)
    coin_zone.append(coin_green)
    coin_zone.append(coin_blue)
    coin_zone.append(coin_black)
    $("#coin_zone1").append(coin_zone)

    var coin2_zone = $("<div class='row'></div>")
    var coin2_white = $("<img class='col-md-2' id='coins' src='../" + card_dict['coin']['white'] + "'>")
    var coin2_red = $("<img class='col-md-2' id='coins' src='../" + card_dict['coin']['red'] + "'>")
    var coin2_green= $("<img class='col-md-2' id='coins' src='../" + card_dict['coin']['green'] + "'>")
    var coin2_blue = $("<img class='col-md-2' id='coins' src='../" + card_dict['coin']['blue'] + "'>")
    var coin2_black = $("<img class='col-md-2' id='coins' src='../" + card_dict['coin']['black'] + "'>")
    coin2_zone.append(coin2_white)
    coin2_zone.append(coin2_red)
    coin2_zone.append(coin2_green)
    coin2_zone.append(coin2_blue)
    coin2_zone.append(coin2_black)
    $("#coin_zone2").append(coin2_zone)
    
    var coin_num_zone = $("<div class='row'></div>")
    var coin_num_white = $("<div class='col-md-2 cointext'></div>")
    coin_num_white.html("White: " + board_state['coin_num']['white'])
    var coin_num_red = $("<div class='col-md-2 cointext'></div>")
    coin_num_red.html("Red: " + board_state['coin_num']['red'])
    var coin_num_green = $("<div class='col-md-2 cointext'></div>")
    coin_num_green.html("Green: " + board_state['coin_num']['green'])
    var coin_num_blue = $("<div class='col-md-2 cointext'></div>")
    coin_num_blue.html("Blue: " + board_state['coin_num']['blue'])
    var coin_num_black = $("<div class='col-md-2 cointext'></div>")
    coin_num_black.html("Black: " + board_state['coin_num']['black'])
    coin_num_zone.append(coin_num_white)
    coin_num_zone.append(coin_num_red)
    coin_num_zone.append(coin_num_green)
    coin_num_zone.append(coin_num_blue)
    coin_num_zone.append(coin_num_black)
    $("#coin_num_zone").append(coin_num_zone)

    var oppo_token_zone = $("<div class='row'></div>")
    var oppo_token_white = $("<div class='col-md-2 cointext'></div>")
    oppo_token_white.html("White: " + board_state['oppo_token']['white'])
    var oppo_token_red = $("<div class='col-md-2 cointext'></div>")
    oppo_token_red.html("Red: " + board_state['oppo_token']['red'])
    var oppo_token_green = $("<div class='col-md-2 cointext'></div>")
    oppo_token_green.html("Green: " + board_state['oppo_token']['green'])
    var oppo_token_blue = $("<div class='col-md-2 cointext'></div>")
    oppo_token_blue.html("Blue: " + board_state['oppo_token']['blue'])
    var oppo_token_black = $("<div class='col-md-2 cointext'></div>")
    oppo_token_black.html("Black: " + board_state['oppo_token']['black'])
    oppo_token_zone.append(oppo_token_white)
    oppo_token_zone.append(oppo_token_red)
    oppo_token_zone.append(oppo_token_green)
    oppo_token_zone.append(oppo_token_blue)
    oppo_token_zone.append(oppo_token_black)
    $("#oppo_token_zone").append(oppo_token_zone)
    
    var oppo_bonus_zone = $("<div class='row'></div>")
    var oppo_bonus_white = $("<div class='col-md-2 cointext'></div>")
    oppo_bonus_white.html("White: " + board_state['oppo_bonus']['white'])
    var oppo_bonus_red = $("<div class='col-md-2 cointext'></div>")
    oppo_bonus_red.html("Red: " + board_state['oppo_bonus']['red'])
    var oppo_bonus_green = $("<div class='col-md-2 cointext'></div>")
    oppo_bonus_green.html("Green: " + board_state['oppo_bonus']['green'])
    var oppo_bonus_blue = $("<div class='col-md-2 cointext'></div>")
    oppo_bonus_blue.html("Blue: " + board_state['oppo_bonus']['blue'])
    var oppo_bonus_black = $("<div class='col-md-2 cointext'></div>")
    oppo_bonus_black.html("Black: " + board_state['oppo_bonus']['black'])
    oppo_bonus_zone.append(oppo_bonus_white)
    oppo_bonus_zone.append(oppo_bonus_red)
    oppo_bonus_zone.append(oppo_bonus_green)
    oppo_bonus_zone.append(oppo_bonus_blue)
    oppo_bonus_zone.append(oppo_bonus_black)
    $("#oppo_bonus_zone").append(oppo_bonus_zone)
    
    var oppo_point_zone = $("<div class='row'></div>")
    var oppo_point_content = $("<div class='col-md-2 cointext'></div>")
    oppo_point_content.html("Prestige Points: " + board_state['oppo_point'])
    oppo_point_zone.append(oppo_point_content)
    $("#oppo_point_zone").append(oppo_point_zone)
    
    var my_token_zone = $("<div class='row'></div>")
    var my_token_white = $("<div class='col-md-2 cointext'></div>")
    my_token_white.html("White: " + board_state['my_token']['white'])
    var my_token_red = $("<div class='col-md-2 cointext'></div>")
    my_token_red.html("Red: " + board_state['my_token']['red'])
    var my_token_green = $("<div class='col-md-2 cointext'></div>")
    my_token_green.html("Green: " + board_state['my_token']['green'])
    var my_token_blue = $("<div class='col-md-2 cointext'></div>")
    my_token_blue.html("Blue: " + board_state['my_token']['blue'])
    var my_token_black = $("<div class='col-md-2 cointext'></div>")
    my_token_black.html("Black: " + board_state['my_token']['black'])
    my_token_zone.append(my_token_white)
    my_token_zone.append(my_token_red)
    my_token_zone.append(my_token_green)
    my_token_zone.append(my_token_blue)
    my_token_zone.append(my_token_black)
    $("#my_token_zone").append(my_token_zone)

    var my_bonus_zone = $("<div class='row'></div>")
    var my_bonus_white = $("<div class='col-md-2 cointext'></div>")
    my_bonus_white.html("White: " + board_state['my_bonus']['white'])
    var my_bonus_red = $("<div class='col-md-2 cointext'></div>")
    my_bonus_red.html("Red: " + board_state['my_bonus']['red'])
    var my_bonus_green = $("<div class='col-md-2 cointext'></div>")
    my_bonus_green.html("Green: " + board_state['my_bonus']['green'])
    var my_bonus_blue = $("<div class='col-md-2 cointext'></div>")
    my_bonus_blue.html("Blue: " + board_state['my_bonus']['blue'])
    var my_bonus_black = $("<div class='col-md-2 cointext'></div>")
    my_bonus_black.html("Black: " + board_state['my_bonus']['black'])
    my_bonus_zone.append(my_bonus_white)
    my_bonus_zone.append(my_bonus_red)
    my_bonus_zone.append(my_bonus_green)
    my_bonus_zone.append(my_bonus_blue)
    my_bonus_zone.append(my_bonus_black)
    $("#my_bonus_zone").append(my_bonus_zone)
    
    var my_point_zone = $("<div class='row'></div>")
    var my_point_content = $("<div class='col-md-2 cointext'></div>")
    my_point_content.html("Prestige Points: " + board_state['my_point'])
    my_point_zone.append(my_point_content)
    $("#my_point_zone").append(my_point_zone)


    var oppo_action_zone = $("<div class='row'></div>")
    var oppo_action_content = $("<div class='col-md-12'></div>")
    oppo_action_content.html("Opponent's Last Action: " + board_state['oppo_last_action'])
    oppo_action_zone.append(oppo_action_content)
    $("#oppo_action_zone").append(oppo_action_zone)

    if (board_state['my_point'] >= 15) {
        game_end("You won!")
    }

    if (board_state['oppo_point'] >= 15) {
        game_end("The opponent won.")
    }
  }

  function save_selections(selected_cards) {
    var save_res = [selected_cards, board_state]
    console.log(save_res)

    $.ajax({
        async: false,
        type: "POST",
        url: "finish_turn",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(save_res),
        success: function(result) {
            board_state = result['new_board_state']
            console.log(board_state)
            display_board(board_state)
            $('.selected').removeClass('selected')
            invoke_clicking()
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    })
  }

  function check_fields_correct(selected_cards, board_state) {
    var overall_flag = true
    var error_message = ""
    $("#player_warning").empty()
    var check_res = [selected_cards, board_state]

    $.ajax({
        async: false,
        type: "POST",
        url: "check_fields",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(check_res),
        success: function(result) {
            overall_flag = result['check_flag']
            error_message = result['error_msg']
            $("#player_warning").append(error_message)
            console.log(error_message)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    })

    return overall_flag
  }

  function invoke_clicking() {
    var click_counter = {}
    $('img').off("click").on("click", function() {
      if (this.src in click_counter) {
        click_counter[this.src] = click_counter[this.src] + 1
      } else {
        click_counter[this.src] = 0
      }

      if (click_counter[this.src] % 2 == 0) {
        $(this).addClass('selected')
      } else {
        $(this).removeClass('selected')
      }

      console.log(this.src)
    })

    $("#finish_button").off("click").on("click", function() {
      var total_clicked = []
      $(".selected").each(function() {
        total_clicked.push(this.src)
      })

      if (check_fields_correct(total_clicked, board_state)) {
        save_selections(total_clicked)
      }
    })
  }

  function game_end(end_msg) {
    var end_msg_zone = $("<div class='row'></div>")
    var end_msg_content = $("<div class='col-md-12'></div>")
    end_msg_content.html("Game Ended! " + end_msg)
    end_msg_zone.append(end_msg_content)
    $("#end_msg_zone").append(end_msg_zone)

    $("#endDialog")[0].showModal()

    $("#homeBtn").click(function (event) {
      $("#endDialog")[0].close()
      window.location.href = "/"
    })

    $("#restartBtn").click(function (event) {
      $("#endDialog")[0].close()
      window.location.href = "/play"
    })
  }

  $(document).ready(function() {
    display_board(board_state)
    invoke_clicking()
  })

