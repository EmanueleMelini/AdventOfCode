matrix = []
CHARS = ["#", "+", "$", "*", "-", "@", "=", "/", "&", "%", "!", "£", "(", ")", "?", "^", "[", "]"]
coords_found = []
all_numbers = []

MAX_X = 140
MAX_Y = 140
file = "input.txt"


def get_number(x: int, y: int):
    number = matrix[y][x]
    if not number.isdigit():
        return
    i = x - 1
    while i >= 0:
        n = matrix[y][i]
        if n.isdigit():
            number = n + number
            i -= 1
        else:
            break
    i += 1
    coords = str(i) + "," + str(y)
    keep = False
    try:
        coords_found.index(coords)
    except ValueError:
        keep = True

    if keep:
        coords_found.append(coords)
        i = x + 1
        while i < MAX_X:
            n = matrix[y][i]
            if n.isdigit():
                number = number + n
                i += 1
            else:
                break
                #i = 140
        all_numbers.append(int(number))

    return


def try_adjacent(x: int, y: int):
    yy = y - 1
    while yy <= y + 1:
        if 0 <= yy < 140:
            xx = x - 1
            while xx <= x + 1:
                if 0 <= xx < 140:
                    get_number(xx, yy)
                xx += 1
        yy += 1


with (open(file)) as f:
    lines = f.readlines()

    for line in lines:
        arr = []
        for c in line:
            if c != "\n":
                arr.append(c)
        matrix.append(arr)

    y = 0
    while y < MAX_Y:
        x = 0
        while x < MAX_X:
            char = matrix[y][x]
            try:
                i = CHARS.index(char)
                try_adjacent(x, y)
            except ValueError:
                pass
            x += 1
        y += 1

    tot = 0
    for n in all_numbers:
        tot += n
    print(tot)
