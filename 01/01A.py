with open("01/input.txt.", "r") as f:
    sum = 0
    for line in f:
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
        sum += number
    print(sum)