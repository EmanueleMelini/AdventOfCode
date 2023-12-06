with (open('input.txt')) as f:
    lines = f.readlines()
    tot = 0
    for line in lines:
        n1 = '0'
        n2 = '0'
        for c in line:
            if c.isdigit() and n1 == '0':
                n1 = c

            if c.isdigit():
                n2 = c

        ntot = int(n1 + n2)
        tot += ntot

    print(tot)
