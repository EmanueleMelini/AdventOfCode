input_arr = {
    'seeds': [],
    'seed-to-soil': [],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': []
}


def get_map(string: str):
    lines = string.split(',')
    new_arr = []
    for line in lines:
        line_obj_arr = line.split(' ')
        line_obj = {
            'dest': line_obj_arr[0],
            'src': line_obj_arr[1],
            'range': line_obj_arr[2]
        }
        new_arr.append(line_obj)
    return new_arr


def get_dest(map_arr: list, seed: int):
    min_dest = 999999999
    for map_obj in map_arr:
        if int(map_obj['src']) > int(seed):
            dest = seed
        else:
            max_src = int(map_obj['src']) + int(map_obj['range'])
            if max_src < seed:
                dest = seed
            else:
                dest = int(map_obj['dest']) - int(map_obj['src']) + seed
                min_dest = dest
                break
        if dest < min_dest:
            min_dest = dest
    return min_dest


with (open('input.txt')) as f:

    inpr = f.read().split('\n\n')

    for inp in inpr:

        inp_str = inp.replace('\n', ',')
        inp_str = inp_str.replace(': ', ':,')
        line_arr = inp_str.split(':,')
        line_id = line_arr[0].replace(' map', '')
        line_numbers = line_arr[1]
        if line_id.find('seeds') >= 0:
            input_arr['seeds'] = line_numbers.split(' ')
        else:
            input_arr[line_id] = get_map(line_numbers)

    min_loc = 999999999

    for seed in input_arr['seeds']:

        soil = get_dest(input_arr['seed-to-soil'], int(seed))

        fertilizer = get_dest(input_arr['soil-to-fertilizer'], int(soil))

        water = get_dest(input_arr['fertilizer-to-water'], int(fertilizer))

        light = get_dest(input_arr['water-to-light'], int(water))

        temperature = get_dest(input_arr['light-to-temperature'], int(light))

        humidity = get_dest(input_arr['temperature-to-humidity'], int(temperature))

        location = get_dest(input_arr['humidity-to-location'], int(humidity))


        print('Seed ' + seed + ', soil ' + str(soil) + ', fertiziler ' + str(fertilizer) + ', water ' + str(water) + ', light ' + str(light) + ', temperature ' + str(temperature) + ', humidity ' + str(humidity) + ', location ' + str(location))

        if min_loc > location:
            min_loc = location

    print('Location: ' + str(min_loc))


