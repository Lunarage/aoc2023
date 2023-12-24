import re
import math

def process_input(lines):
    time_list = lines[0].split(":")[1].split()
    time_list = [int(n) for n in time_list]
    distance_list = lines[1].split(":")[1].split() 
    distance_list = [int(n) for n in distance_list]
    return (time_list, distance_list)

def main():
    with open("06/input.txt", "r") as f:
        lines = f.read().split('\n')
        time_list, distance_list = process_input(lines)
        product = 1
        for t, d in zip(time_list, distance_list):
            ways = math.ceil((t+math.sqrt(t**2-4*d))/2) - math.floor((t-math.sqrt(t**2-4*d))/2) - 1
            product *= ways
        print(product)


if __name__ == "__main__":
    main()