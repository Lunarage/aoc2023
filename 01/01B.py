numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    }

with open("01/input.txt.", "r") as f:
    sum = 0
    for line in f:
        for n_string, n_integer in numbers.items():
            line = line.replace(n_string, n_integer)

        number = ""
        for char in line:
            if char.isdigit():
                number += char
                break
        for char in reversed(line):
            if char.isdigit():
                number += char
                break
        number = int(number)
        print(number)
        sum += number
    print(sum)