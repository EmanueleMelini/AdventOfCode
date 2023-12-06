import re


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
    tot_power = 0
    for line in lines:
        red = get_color(line, "red")
        green = get_color(line, "green")
        blue = get_color(line, "blue")
        game_power = red * green * blue
        tot_power += game_power

    print(tot_power)
