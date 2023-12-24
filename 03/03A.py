def find_numbers(lines, n):
    line = lines[n]
    i = 0
    current_number = ""
    while i < len(lines[n]):
        if line[i].isdigit():
            current_number = line[i]
        else:
            current_number = ""
        i += 1


with open("03/input.txt", "r") as f:
    lines = f.read()
    for n in range(len(lines)):
        find_numbers(lines, n)