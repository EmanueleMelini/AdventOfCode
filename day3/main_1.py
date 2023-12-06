matrix = []
CHARS = ["#", "+", "$", "*", "-", "@"]
coords_found = []


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
    coords = str(i) + "," + str(y)
    keep = False
    try:
        coords_found.index(coords)
    except ValueError:
        keep = True

    if keep:
        coords_found.append(coords)
        i = x + 1
        while i < 140:
            n = matrix[y][i]
            if n.isdigit():
                number = number + n
                i += 1
            else:
                break
                #i = 140
        return int(number)
    else:
        return -1


def try_adjacent(x: int, y: int):
    numbers = []
    yy = y - 1
    #print("Base x:" + str(x))
    #print("Base y:" + str(y))
    #print("Start x:" + str(x - 1))
    #print("Start y:" + str(y - 1))
    while yy <= y + 1:
        if 0 <= yy < 140:
            xx = x - 1
            while xx <= x + 1:
                #print("Trying " + str(xx) + ", " + str(yy))
                if 0 <= xx < 140:
                    n_found = get_number(xx, yy)
                    if n_found > 0:
                        try:
                            found = numbers.index(n_found)
                        except ValueError:
                            pass
                        numbers.append(n_found)
                xx += 1
        yy += 1
    return numbers


with (open('input.txt')) as f:
    lines = f.readlines()

    for line in lines:
        arr = []
        for c in line:
            if c != "\n":
                arr.append(c)
        matrix.append(arr)

    tot = 0
    all_numbers = []
    y = 0
    while y < 140:
        x = 0
        while x < 140:
            char = matrix[y][x]
            try:
                i = CHARS.index(char)
                try_numbers = try_adjacent(x, y)
                all_numbers += try_numbers
                for n in try_numbers:
                    tot += n
            except ValueError:
                pass
            x += 1
        y += 1

    print(all_numbers)
    print(coords_found)
    print(tot)
