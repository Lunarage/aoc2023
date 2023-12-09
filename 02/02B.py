def extract_game_id(line):
    return int(line.split(":")[0].split()[1])


def extract_cube_colors(line):
    colors = {"r": 0, "g": 0, "b": 0}
    for hand in line.split(":")[1].split(";"):
        for cubes in hand.split(","):
            amount = int(cubes.lstrip(" ").split(" ")[0])
            color = cubes.lstrip(" ").split(" ")[1]
            if color == "red":
                colors["r"] = max(colors["r"], amount)
            elif color == "green":
                colors["g"] = max(colors["g"], amount)
            elif color == "blue":
                colors["b"] = max(colors["b"], amount)
    return colors


with open("02/input.txt.", "r") as f:
    sum = 0
    for line in f:
        line = line.rstrip("\n")
        possible = True
        hand = extract_cube_colors(line)
        sum += hand["r"]*hand["g"]*hand["b"]
    print(sum)