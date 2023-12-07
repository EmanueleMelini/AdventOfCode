import re

cards = []
file = 'input.txt'


def get_numbers(in_list: list):
    return list(filter(lambda x: x.isdigit(), in_list))


def get_id(card: str):
    card_id = re.findall(r'\d+', card)
    return int(card_id[0])


def get_winning(card: str):
    numbers_arr = card.split('|')
    return get_numbers(numbers_arr[0].split(' '))


def get_played(card: str):
    numbers_arr = card.split('|')
    return get_numbers(numbers_arr[1].split(' '))


def get_winners(winning: list, played: list):
    winners = []
    for win in winning:
        try:
            played.index(win)
            winners.append(win)
        except ValueError:
            pass
    return winners


with (open(file)) as f:
    lines = f.readlines()

    tot = 0

    for line in lines:
        card_l = line.replace("\n", "")
        card_arr = card_l.split(':')
        card_id = get_id(card_arr[0])
        winning = get_winning(card_arr[1])
        played = get_played(card_arr[1])
        winners = get_winners(winning, played)
        card = {
            "id": card_id,
            "count": 1,
            "winners": winners
        }
        cards.append(card)

    for card in cards:

        if len(card["winners"]) > 0:

            i = cards.index(card) + 1
            max_i = min(i + len(card["winners"]), len(cards))

            while i < max_i:
                cards[i]["count"] += 1 * card["count"]
                i += 1

    for card in cards:
        tot += card["count"]

    print(tot)
