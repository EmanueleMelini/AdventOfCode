import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def get_id(game: str):
    game_arr = game.split(':')
    return int(re.findall(r'\d+', game_arr[0])[0])


def get_color(game: str, find_color: str):
    game_arr = game.split(':')
    extractions = game_arr[1].split(';')
    max_color = 0
    for extraction in extractions:
        colors = extraction.split(',')
        for color in colors:
            if color.find(find_color) > 0:
                color_number = int(re.findall(r'\d+', color)[0])
                if max_color < color_number:
                    max_color = color_number
    return max_color


with (open('input.txt')) as f:
    lines = f.readlines()
    id_tot = 0
    for line in lines:
        game_id = get_id(line)
        red = get_color(line, "red")
        green = get_color(line, "green")
        blue = get_color(line, "blue")

        if red <= MAX_RED and green <= MAX_GREEN and blue <= MAX_BLUE:
            id_tot += game_id

    print(str(id_tot))
