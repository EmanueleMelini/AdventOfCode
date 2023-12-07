matrix = []
GEAR = '*'

MAX_X = 140
MAX_Y = 140
file = "input.txt"


def get_number(x: int, y: int):
    number = matrix[y][x]
    if not number.isdigit():
        return -1
    i = x - 1
    while i >= 0:
        n = matrix[y][i]
        if n.isdigit():
            number = n + number
            i -= 1
        else:
            break
    i += 1

    i = x + 1
    while i < MAX_X:
        n = matrix[y][i]
        if n.isdigit():
            number = number + n
            i += 1
        else:
            break
    return int(number)


def try_adjacent(x: int, y: int):
    numbers = []
    yy = y - 1
    while yy <= y + 1:
        if 0 <= yy < 140:
            xx = x - 1
            while xx <= x + 1:
                if 0 <= xx < 140:
                    n = get_number(xx, yy)
                    if n >= 0:
                        try:
                            numbers.index(n)
                        except ValueError:
                            numbers.append(n)
                xx += 1
        yy += 1
    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    else:
        return 0


with (open(file)) as f:
    lines = f.readlines()

    for line in lines:
        arr = []
        for c in line:
            if c != "\n":
                arr.append(c)
        matrix.append(arr)

    tot = 0
    y = 0
    while y < MAX_Y:
        x = 0
        while x < MAX_X:
            char = matrix[y][x]
            if char == GEAR:
                tot += try_adjacent(x, y)
            x += 1
        y += 1

    print(tot)
