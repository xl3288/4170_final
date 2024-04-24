from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import load_cards
import random
app = Flask(__name__)

card_dict = load_cards.compile_img_dict()

learn_data = [
    {
        "id": 1,
        "title": "1. Game Overview",
        "image": "static/learn/img1.png",
        "text": ["In Splendor, you take on the role of a rich merchant during the Renaissance. You will use your resources to acquire mines, transportation methods, and artisans who will allow you to turn raw gems into beautiful jewels.",
                 "Setup: 2-4 players (best with 3)",
                 "Playing time: 30 min"],
        "highlight_text": ["Setup", "Playing time"],
    },
    {
        "id": 2,
        "title": "2. Basic Currency Units",
        "image": "static/learn/img2.png",
        "text": ["Players take turn to collect gem tokens, which are used as basic currencies to purchase development cards (coming up next)."],
        "highlight_text": ["gem tokens", "development cards"],
    },
    {
        "id": 3,
        "title": "3. Development Cards",
        "image": "static/learn/img3.png",
        "text": ["Development cards award player prestige points (top left number), with higher level cards worth more points.",
                 "Development cards also award player bonus (top right gem), which is worth an equivalent token of the same color. Unlike a token, bonus is permanent and can be reused infinitely many times."],
        "highlight_text": ["prestige points", "player bonus", "bonus is permanent"],
    },
    {
        "id": 4,
        "title": "3. Development Cards-Continued",
        "image": "static/learn/img4.png",
        "text": [
            "To purchase a development card, a player needs to spend the amount of tokens denoted by the cost at the bottom left of the card.",
            "For each bonus already in possession, the cost is deducted by 1 for that color.",
            "For example, to purchase “Example Card”, it will cost 4 white, 2 blue, and 1 black tokens. But if previously possessed all cards in “Example Player Pile”, then the cost is reduced to 3 white tokens only."],
        "highlight_text": ["cost at the bottom left", "cost is deducted by 1 for that color", "4 white, 2 blue, and 1 black tokens", "3 white tokens"],
    },
    {
        "id": 5,
        "title": "4. Game Setup",
        "image": "static/learn/img5.png",
        "text": ["At the beginning of the game: Shuffle each development card level deck separately and place them face down; Reveal 4 cards from each level; Place the tokens in 5 distinct piles"],
        "highlight_text": ["Shuffle", "face down", "Reveal 4 cards", "tokens in 5 distinct piles"],
    },
    {
        "id": 6,
        "title": "5. Player Action",
        "image": "static/learn/img5.png",
        "text": [
            "On their turn, a player choose to perform only one of the three actions: (1) Take 3 tokens of different color; (2) Take 2 tokens of the same color; (3) Purchase 1 face-up development card from the revealed selections.",
            "* Youngest player starts first",],
        "highlight_text": ["3 tokens of different color", "2 tokens of the same color", "1 face-up development card"],
    },
    {
        "id": 7,
        "title": "6. End of Game",
        "image": "static/learn/img5.png",
        "text": [
            "The first player reaching 15 prestige points wins!",
            "* Tied players share the victory."],
        "highlight_text": ["15 prestige points"],
    },
]

def get_random_cards(total_cards):
    one_star_list = list(total_cards["1-star"].keys())
    two_star_list = list(total_cards["2-star"].keys())
    three_star_list = list(total_cards["3-star"].keys())
    random.shuffle(one_star_list)
    random.shuffle(two_star_list)
    random.shuffle(three_star_list)

    rand_list = [one_star_list[:4], two_star_list[:4], three_star_list[:4]]
    return rand_list

def initial_board_state():
    card_status = card_dict.copy()
    rand_list = get_random_cards(card_status)

    revealed1 = []
    revealed2 = []
    revealed3 = []

    for card_name in rand_list[0]:
        this_card = card_status["1-star"].pop(card_name)
        revealed1.append(this_card)

    for card_name in rand_list[1]:
        this_card = card_status["2-star"].pop(card_name)
        revealed2.append(this_card)

    for card_name in rand_list[2]:
        this_card = card_status["3-star"].pop(card_name)
        revealed3.append(this_card)

    board_state = {
        "revealed_cards": [revealed1, revealed2, revealed3],
        "coin_num": {
            "white": 7,
            "red": 7,
            "green": 7,
            "blue": 7,
            "black": 7,},
        "oppo_token": {
            "white": 0,
            "red": 0,
            "green": 0,
            "blue": 0,
            "black": 0,},
        "oppo_bonus": {
            "white": 0,
            "red": 0,
            "green": 0,
            "blue": 0,
            "black": 0,},
        "oppo_point": 0,
        "my_token": {
            "white": 0,
            "red": 0,
            "green": 0,
            "blue": 0,
            "black": 0, },
        "my_bonus": {
            "white": 0,
            "red": 0,
            "green": 0,
            "blue": 0,
            "black": 0, },
        "my_point": 0,
        "oppo_last_action": "You move first. Opponent has not moved yet.",
        "oppo_lvl1_cards": 0
    }
    return board_state

@app.route('/')
def welcome():
    return render_template('welcome.html', card_dict=card_dict)


@app.route('/learn/<id>')
def learn(id):
    global learn_data
    id = int(id)
    next_id = id + 1
    if next_id > 7:
        next_id = 100

    for res in learn_data:
        if res["id"] == id:
            return render_template('learn.html', card_dict=card_dict, res=res, next_id=next_id)

@app.route('/play')
def play():
    board_state = initial_board_state()
    return render_template('play.html', card_dict=card_dict, board_state=board_state)

def get_card_info(path_name):
    return path_name.split('/')[-1].split('.')[0].split('_')

def update_round(total_clicked, board_state, new_board_state):
    for this_pick in total_clicked:
        parse_res = get_card_info(this_pick)

        if parse_res[0] == 'coin':
            coin_color = parse_res[1]
            new_board_state['coin_num'][coin_color] -= 1
            new_board_state['my_token'][coin_color] += 1
        else:
            card_level = int(parse_res[0])
            card_color = parse_res[1]
            card_point = int(parse_res[2])
            card_cost = {
                "white": max(0, int(parse_res[3][0]) - board_state['my_bonus']['white']),
                "red": max(0, int(parse_res[3][1]) - board_state['my_bonus']['red']),
                "green": max(0, int(parse_res[3][2]) - board_state['my_bonus']['green']),
                "blue": max(0, int(parse_res[3][3]) - board_state['my_bonus']['blue']),
                "black": max(0, int(parse_res[3][4]) - board_state['my_bonus']['black']),
            }
            new_board_state['my_bonus'][card_color] += 1
            new_board_state['my_point'] += card_point
            for color in ["white", "red", "green", "blue", "black"]:
                new_board_state['coin_num'][color] += card_cost[color]
                new_board_state['my_token'][color] -= card_cost[color]

            loc = 0
            for rev_card in new_board_state['revealed_cards'][card_level - 1]:
                if this_pick.split('/')[-1].split('.')[0] in rev_card['file_path']:
                    break
                else:
                    loc += 1

            draw_deck = list(card_dict["%s-star" % card_level].keys())
            random.shuffle(draw_deck)
            new_rand_name = draw_deck[0]
            new_rand_card = card_dict["%s-star" % card_level][new_rand_name]
            new_board_state['revealed_cards'][card_level - 1][loc] = new_rand_card
    return new_board_state

def sim_opponent_turn(new_board):
    adj_board = new_board.copy()
    if adj_board['oppo_lvl1_cards'] >= 10:
        avail_cards = adj_board['revealed_cards'][2] + adj_board['revealed_cards'][1] + adj_board['revealed_cards'][0]
    else:
        avail_cards = adj_board['revealed_cards'][0]

    purchase_card = None
    for card in avail_cards:
        enough_token = [adj_board['oppo_bonus'][x] + adj_board['oppo_token'][x] - card['card_cost'][x] >= 0 for x in
                        ['white', 'red', 'green', 'blue', 'black']]
        if all(enough_token):
            purchase_card = card
            break

    if purchase_card is not None:
        # buy the card
        card_level = int(purchase_card['file_path'].split('/')[-1].split('.')[0].split('_')[0])
        if card_level == 1:
            adj_board['oppo_lvl1_cards'] += 1
        for color in ['white', 'red', 'green', 'blue', 'black']:
            this_payment = max(0, int(purchase_card['card_cost'][color] - adj_board['oppo_bonus'][color]))
            adj_board['coin_num'][color] += this_payment
            adj_board['oppo_token'][color] -= this_payment

        adj_board['oppo_bonus'][purchase_card['gem_type']] += 1
        adj_board['oppo_point'] += purchase_card['card_score']

        loc = 0
        for rev_card in adj_board['revealed_cards'][card_level - 1]:
            if purchase_card['file_path'].split('/')[-1].split('.')[0] in rev_card['file_path']:
                break
            else:
                loc += 1

        draw_deck = list(card_dict["%s-star" % card_level].keys())
        random.shuffle(draw_deck)
        new_rand_name = draw_deck[0]
        new_rand_card = card_dict["%s-star" % card_level][new_rand_name]
        adj_board['revealed_cards'][card_level - 1][loc] = new_rand_card
        adj_board['oppo_last_action'] = "Opponent just bought the card of level %s with gem type %s" % (
        card_level, purchase_card['gem_type'])
    else:
        # take random coins
        avail_coins = [x for x in ['white', 'red', 'green', 'blue', 'black'] if adj_board['coin_num'][x] > 0]
        random.shuffle(avail_coins)
        for coin_color in avail_coins[:3]:
            adj_board['coin_num'][coin_color] -= 1
            adj_board['oppo_token'][coin_color] += 1

        adj_board['oppo_last_action'] = "Opponent just took the following 3 coins: %s" % (', '.join(avail_coins[:3]))

    return adj_board

@app.route('/finish_turn', methods=['GET', 'POST'])
def finish_turn():
    json_data = request.get_json()
    total_clicked, board_state = json_data
    new_board_state = board_state.copy()

    new_board_state = update_round(total_clicked, board_state, new_board_state)
    final_board = sim_opponent_turn(new_board_state)
    return jsonify(new_board_state=final_board)

@app.route('/check_fields', methods=['GET', 'POST'])
def check_fields():
    # validate user input
    json_data = request.get_json()
    selected_cards, board_state = json_data
    check_flag = True
    error_msg = ""

    all_cards_type = [x.split('/')[-2] for x in selected_cards]

    if len(all_cards_type) == 0:
        check_flag = False
        error_msg = "You must select coin or card to proceed."

    if len(set(all_cards_type)) > 1:
        check_flag = False
        error_msg = "Cannot select both coins and card"

    if 'back' in all_cards_type:
        check_flag = False
        error_msg = "You must not select any unrevealed cards"
    elif 'coin' in all_cards_type:
        # selected coins
        if len(selected_cards) == 1:
            check_flag = False
            error_msg = "You must select more than 1 coin"
        elif len(selected_cards) == 2:
            coin_colors = [x.split('/')[-1].split('.')[0].split('_')[-1] for x in selected_cards]
            if len(set(coin_colors)) > 1:
                check_flag = False
                error_msg = "When you select 2 coins, they must be of the same color"
            else:
                if board_state['coin_num'][coin_colors[0]] < 4:
                    check_flag = False
                    error_msg = "You cannot select 2 coins of the same color when this color has less than 4 coins remaining on the board"
        elif len(selected_cards) == 3:
            coin_colors = [x.split('/')[-1].split('.')[0].split('_')[-1] for x in selected_cards]
            if len(set(coin_colors)) != 3:
                check_flag = False
                error_msg = "When you select 3 coins, they must all be different colors"
        else:
            check_flag = False
            error_msg = "You must not select more than 3 coins"
    else:
        # selected card
        if len(selected_cards) == 1:
            parse_res = selected_cards[0].split('/')[-1].split('.')[0].split('_')
            card_cost = {
                "white": max(0, int(parse_res[3][0]) - board_state['my_bonus']['white']),
                "red": max(0, int(parse_res[3][1]) - board_state['my_bonus']['red']),
                "green": max(0, int(parse_res[3][2]) - board_state['my_bonus']['green']),
                "blue": max(0, int(parse_res[3][3]) - board_state['my_bonus']['blue']),
                "black": max(0, int(parse_res[3][4]) - board_state['my_bonus']['black']),
            }
            have_enough_tokens = [board_state['my_token'][x] >= card_cost[x] for x in ['white', 'red', 'green', 'blue', 'black']]
            if not all(have_enough_tokens):
                check_flag = False
                error_msg = "You do not have enough tokens to purchase this card"
        else:
            check_flag = False
            error_msg = "You must not select more than 1 card"

    return jsonify(check_flag=check_flag, error_msg=error_msg)

if __name__ == '__main__':
   app.run(debug = True)

