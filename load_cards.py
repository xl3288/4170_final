import os

def load_back_image():
    back_dict = {
        "1-star": "static/cards/back/back_1.jpg",
        "2-star": "static/cards/back/back_2.jpg",
        "3-star": "static/cards/back/back_3.jpg"
    }
    return back_dict

def load_coin_image():
    coin_dict = {
        "white": "static/cards/coin/coin_white.png",
        "red": "static/cards/coin/coin_red.png",
        "green": "static/cards/coin/coin_green.png",
        "blue": "static/cards/coin/coin_blue.png",
        "black": "static/cards/coin/coin_black.png",
    }

    # coin_name_mapping = {}
    return coin_dict

def load_main_cards():
    directory_path = "static/cards/main/"

    main_dict = {
        1: {},
        2: {},
        3: {},
    }

    for filename in os.listdir(directory_path):
        f = os.path.join(directory_path, filename)
        # checking if it is a file
        # if os.path.isfile(f):
        #     print(f)

        split_codes = filename.split('.')[0].split('_')
        star_level = int(split_codes[0])
        gem_type = split_codes[1]
        card_score = int(split_codes[2])
        card_cost = {
            "white": int(split_codes[3][0]),
            "red": int(split_codes[3][1]),
            "green": int(split_codes[3][2]),
            "blue": int(split_codes[3][3]),
            "black": int(split_codes[3][4]),
        }

        main_dict[star_level][filename] = {
            "file_path": f,
            "gem_type": gem_type,
            "card_score": card_score,
            "card_cost": card_cost
        }

    return main_dict

def compile_img_dict():
    main_dict = load_main_cards()
    back_dict = load_back_image()
    coin_dict = load_coin_image()

    final_dict = {
        "1-star": main_dict[1],
        "2-star": main_dict[2],
        "3-star": main_dict[3],
        "back": back_dict,
        "coin": coin_dict
    }
    return final_dict


def get_random_cards(total_cards):
    import random
    one_star_list = list(total_cards["1-star"].keys())
    two_star_list = list(total_cards["2-star"].keys())
    three_star_list = list(total_cards["3-star"].keys())
    random.shuffle(one_star_list)
    random.shuffle(two_star_list)
    random.shuffle(three_star_list)

    rand_list = [one_star_list[:4], two_star_list[:4], three_star_list[:4]]
    return rand_list


def get_card_info(path_name):
    return path_name.split('/')[-1].split('.')[0].split('_')

if __name__ == '__main__':
    card_dict = compile_img_dict()
    import ipdb; ipdb.set_trace()