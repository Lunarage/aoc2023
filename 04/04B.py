import re


def increment_points(number):
    if number == 0:
        return 1
    return number * 2


def split_line(line):
    card_prefix = line.split(":")[0]
    numbers = line.split(":")[1]

    card_no = int(re.match(r'Card\s+(\d+)', card_prefix)[1])
    card_index = card_no - 1

    winning_numbs = numbers.split("|")[0]
    winning_numbs = [int(n) for n in winning_numbs.split()]

    my_numbs = numbers.split("|")[1]
    my_numbs = [int(n) for n in my_numbs.split()]

    return (card_index, winning_numbs, my_numbs)


def count_winning_numbers(winning_numbers, my_numbers):
    count = 0
    for number in my_numbers:
        if number in winning_numbers:
            count += 1
    return count


def main():
    with open("04/input.txt", "r") as f:
        lines = f.read().split('\n')
        print(lines)
        copies = [1 for _ in lines]
        for line in lines:
            card_index, winning_numbs, my_numbs = split_line(line)
            win_count = count_winning_numbers(winning_numbs, my_numbs)
            for i in range(1, win_count+1):
                copies[card_index + i] += copies[card_index]
        print(copies, sum(copies))


if __name__ == "__main__":
    main()