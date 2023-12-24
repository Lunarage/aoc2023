def increment_points(number):
    if number == 0:
        return 1
    return number * 2


with open("04/input.txt", "r") as f:
    points = 0
    for line in f:
        numbers = line.split(":")[1]
        winning_numbs = numbers.split("|")[0]
        winning_numbs = [int(n) for n in winning_numbs.split()]
        my_numbs = numbers.split("|")[1]
        my_numbs = [int(n) for n in my_numbs.split()]

        card_points = 0
        for number in my_numbs:
            if number in winning_numbs:
                card_points = increment_points(card_points)
        points += card_points
    print(points)