import numpy as np
import sys
import cv2
import pdb
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
        if os.path.isfile(f):
            print(f)

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

def test_img_dict():
    main_dict = load_main_cards()
    for key, val in main_dict[1].items():
        this_img = cv2.imread(val['file_path'], cv2.IMREAD_ANYCOLOR)
        resized = cv2.resize(this_img, (600, 800))
        cv2.imshow(','.join(map(str, [val['gem_type'], val['card_score'], val['card_cost']])), resized)
        cv2.waitKey(0)

    for key, val in main_dict[2].items():
        this_img = cv2.imread(val['file_path'], cv2.IMREAD_ANYCOLOR)
        resized = cv2.resize(this_img, (600, 800))
        cv2.imshow(','.join(map(str, [val['gem_type'], val['card_score'], val['card_cost']])), resized)
        cv2.waitKey(0)

    for key, val in main_dict[3].items():
        this_img = cv2.imread(val['file_path'], cv2.IMREAD_ANYCOLOR)
        resized = cv2.resize(this_img, (600, 800))
        cv2.imshow(','.join(map(str, [val['gem_type'], val['card_score'], val['card_cost']])), resized)
        cv2.waitKey(0)

    back_dict = load_back_image()
    coin_dict = load_coin_image()

    for key, val in back_dict.items():
        this_img = cv2.imread(val, cv2.IMREAD_ANYCOLOR)
        resized = cv2.resize(this_img, (375, 500))
        cv2.imshow(key, resized)
        cv2.waitKey(0)

    for key, val in coin_dict.items():
        this_img = cv2.imread(val, cv2.IMREAD_ANYCOLOR)
        resized = cv2.resize(this_img, (375, 500))
        cv2.imshow(key, resized)
        cv2.waitKey(0)


if __name__ == '__main__':
   test_img_dict()
