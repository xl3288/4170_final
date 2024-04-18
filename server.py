from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import load_cards
import random
app = Flask(__name__)

# <img class="img-responsive col-md-5" src="{{ url_for('static', filename='back_00.jpg') }}" alt="f1">

card_dict = load_cards.compile_img_dict()

learn_data = [
    {
        "id": 1,
        "title": "1. Game Overview",
        "image": "static/learn/img1.png",
        "text": ["In Splendor, you take on the role of a rich merchant during the Renaissance. You will use your resources to acquire mines, transportation methods, and artisans who will allow you to turn raw gems into beautiful jewels.",
                 "Setup: 2-4 players (best with 3)",
                 "Playing time: 30 min"],
    },
    {
        "id": 2,
        "title": "2. Basic Currency Units",
        "image": "static/learn/img2.png",
        "text": ["Players take turn to collect gem tokens, which are used as basic currencies to purchase development cards (coming up next)."],
    },
    {
        "id": 3,
        "title": "3. Development Cards",
        "image": "static/learn/img3.png",
        "text": ["Development cards award player prestige points (top left number), with higher level cards worth more points.",
                 "Development cards also award player bonus (top right gem), which is worth an equivalent token of the same color. Unlike a token, bonus is permanent and can be reused infinitely many times."],
    },
    {
        "id": 4,
        "title": "3. Development Cards-Continued",
        "image": "static/learn/img4.png",
        "text": [
            "To purchase a development card, a player needs to spend the amount of tokens denoted by the cost at the bottom left of the card.",
            "For each bonus already in possession, the cost is deducted by 1 for that color.",
            "For example, to purchase “Example Card”, it will cost 4 white, 2 blue, and 1 black tokens. But if previously possessed all cards in “Example Player Pile”, then the cost is reduced to 3 white tokens only."],
    },
    {
        "id": 5,
        "title": "4. Game Setup",
        "image": "static/learn/img5.png",
        "text": [
            "At the beginning of the game: Shuffle each development card level deck separately and place them face down; Reveal 4 cards from each level; Place the tokens in 5 distinct piles"],
    },
    {
        "id": 6,
        "title": "5. Player Action",
        "image": "static/learn/img5.png",
        "text": [
            "On their turn, a player choose to perform only one of the three actions: (1) Take 3 tokens of different color; (2) Take 2 tokens of the same color; (3) Purchase 1 face-up development card from the revealed selections.",
            "* Youngest player starts first",
            "* Player may not have more than 10 tokens at the end of their turn. Must discard until 10 are left.",],
    },
    {
        "id": 7,
        "title": "6. End of Game",
        "image": "static/learn/img5.png",
        "text": [
            "The first player reaching 15 prestige points wins!",
            "* Tied players share the victory."],
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
        "oppo_last_action": "You move first. Opponent has not moved yet."
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

            # del_card = new_board_state['revealed_cards'][card_level - 1].pop(loc)
            # del_name = del_card['file_path'].split('/')[-1].split('.')[0]
            # card_status["%s-star" % card_level].pop(del_name)

            draw_deck = list(card_dict["%s-star" % card_level].keys())
            print(len(draw_deck))
            random.shuffle(draw_deck)
            new_rand_name = draw_deck[0]
            new_rand_card = card_dict["%s-star" % card_level][new_rand_name]
            new_board_state['revealed_cards'][card_level - 1][loc] = new_rand_card
    return new_board_state

@app.route('/finish_turn', methods=['GET', 'POST'])
def finish_turn():
    # validate user input
    json_data = request.get_json()
    total_clicked, board_state = json_data
    new_board_state = board_state.copy()

    new_board_state = update_round(total_clicked, board_state, new_board_state)
    return jsonify(new_board_state=new_board_state)

if __name__ == '__main__':
   app.run(debug = True)

