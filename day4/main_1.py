import re

file = 'input.txt'


def get_numbers(in_list: list):
    return list(filter(lambda x: x.isdigit(), in_list))


def get_id(card_str: str):
    card_id = re.findall(r'\d+', card_str)
    return int(card_id[0])


def get_winning(card_str: str):
    numbers_arr = card_str.split('|')
    return get_numbers(numbers_arr[0].split(' '))


def get_played(card_str: str):
    numbers_arr = card_str.split('|')
    return get_numbers(numbers_arr[1].split(' '))


def get_winners(winning_list: list, played_list: list):
    winners_list = []
    for win in winning_list:
        try:
            played_list.index(win)
            winners_list.append(win)
        except ValueError:
            pass
    return winners_list


with (open(file)) as f:
    lines = f.readlines()

    tot = 0

    for line in lines:
        card = line.replace("\n", "")

        card_arr = card.split(':')
        card_winning = get_winning(card_arr[1])
        card_played = get_played(card_arr[1])
        card_winners = get_winners(card_winning, card_played)

        tot_winners = len(card_winners)

        if tot_winners > 0:
            tot_winners -= 1
            points = 2 ** tot_winners
            before = tot
            tot += points

    print(tot)
