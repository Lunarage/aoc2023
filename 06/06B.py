import math


def process_input(lines):
    time_list = lines[0].split(":")[1].replace(" ", "")
    time = int(time_list)
    distance_list = lines[1].split(":")[1].replace(" ", "")
    distance = int(distance_list)
    return (time, distance)


def main():
    with open("06/input.txt", "r") as f:
        lines = f.read().split('\n')
        t, d = process_input(lines)
        ways = math.ceil((t+math.sqrt(t**2-4*d))/2) - math.floor((t-math.sqrt(t**2-4*d))/2) - 1
        print(ways)


if __name__ == "__main__":
    main()