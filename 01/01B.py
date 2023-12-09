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

def find_last_digit_word(segment):
    for i in range(-1, -len(segment)-1, -1):
        if segment[i].isdigit():
            print(segment[i])
            return segment[i]
        for n_string, n_number in numbers.items():
            k = i
            match = True
            for n_char in n_string:
                if k >= 0:
                    match = False
                    break
                if n_char != segment[k]:
                    match = False
                    break
                k += 1
            if match:
                print(n_number)
                return n_number


def find_first_digit_word(segment):
    for i in range(len(segment)):
        if segment[i].isdigit():
            return segment[i]
        for n_string, n_number in numbers.items():
            k = i
            match = True
            for n_char in n_string:
                if k >= len(segment):
                    match = False
                    break
                if n_char != segment[k]:
                    match = False
                    break
                k += 1
            if match:
                return n_number

with open("01/input.txt.", "r") as f:
    sum = 0
    for line in f:
        line = line.rstrip('\n')
        print(line)
        number = find_first_digit_word(line)
        number += find_last_digit_word(line)
        # print(number)
        number = int(number)
        sum += number
    print(sum)