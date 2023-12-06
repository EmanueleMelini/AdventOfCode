def replace_digit(to_replace: str):
    return (to_replace.replace("one", "o1e")
            .replace("two", "t2o")
            .replace("three", "th3ee")
            .replace("four", "f4ur")
            .replace("five", "f5ve")
            .replace("six", "s6x")
            .replace("seven", "se7en")
            .replace("eight", "ei8ht")
            .replace("nine", "n9ne"))


with (open('input.txt')) as f:
    lines = f.readlines()
    tot = 0
    for line in lines:
        n1 = ''
        first = True
        n2 = ''
        new_line = replace_digit(line)
        for c in new_line:
            if c.isdigit():
                if first:
                    n1 = c
                    first = False
                n2 = c

        ntot = int(n1 + n2)
        before = tot
        tot += ntot

    print(tot)
