import re


def process_input(lines):
    exprs = [
        r'^seed-to-soil map: *$\n([\d \n]+)$',
        r'^soil-to-fertilizer map: *$\n([\d \n]+)$',
        r'^fertilizer-to-water map: *$\n([\d \n]+)$',
        r'^water-to-light map: *$\n([\d \n]+)$',
        r'^light-to-temperature map: *$\n([\d \n]+)$',
        r'^temperature-to-humidity map: *$\n([\d \n]+)$',
        r'^humidity-to-location map: *$\n([\d \n]+)$',
    ]

    def process_map(map_list):
        for index, item in enumerate(map_list):
            map_list[index] = tuple([int(n) for n in item.split()])
        return map_list

    seeds = re.match(r'^seeds: (.+)$', lines, re.MULTILINE)[1].split()
    seeds = [int(n) for n in seeds]
    maps = []
    for expr in exprs:
        maps.append(re.search(expr, lines, re.MULTILINE)[1].rstrip().split('\n'))
    maps = list(map(lambda x: process_map(x), maps))
    return (seeds, maps)


def process_maps(input_number, maps):

    def process_step(input_number, step):
        for dest_start, src_start, rng in step:
            if src_start <= input_number <= src_start + rng:
                offset = input_number - src_start
                dest = dest_start + offset
                return dest
        return input_number

    next = input_number
    for step in maps:
        next = process_step(next, step)
    return next


def main():
    with open("05/input.txt", "r") as f:
        lines = f.read()
        seeds, maps = process_input(lines)
        locations = []
        for seed in seeds:
            locations.append(process_maps(seed, maps))
        print(min(locations))

if __name__ == "__main__":
    main()