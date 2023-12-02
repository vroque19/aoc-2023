import re

RED = 12
GREEN = 13
BLUE = 14

def main():
    poss_games = 0
    curr_game = 1
    sum_of_powers = 0
    with open("input.txt", 'r') as f:
        for line in f:
            line = re.search(r':(.*)', line).group(1)
            # part 1
            if part1(line) == True:
                poss_games += curr_game
            curr_game += 1

        # print(poss_games)
            # part 2
            sum_of_powers += part2(line)
            print(sum_of_powers)

def part2(inp):
    curr = ""
    inp += ';'
    red = 0
    blue = 0
    green = 0

    for c in inp:
        if c == ';':
            red_match = re.search(r'(\d+)\s+red', curr)
            blue_match = re.search(r'(\d+)\s+blue', curr)
            green_match = re.search(r'(\d+)\s+green', curr)
            red = max(int(red_match.group(1)) if red_match else 0, red)
            blue = max(int(blue_match.group(1)) if blue_match else 0, blue)
            green = max(int(green_match.group(1)) if green_match else 0, green)

            curr = ""
        curr += c
    return red * blue * green

def part1(inp):
    red = 0
    blue = 0
    green = 0
    curr = ""
    inp += ';'
    for c in inp:
        if c == ';':
            red_match = re.search(r'(\d+)\s+red', curr)
            blue_match = re.search(r'(\d+)\s+blue', curr)
            green_match = re.search(r'(\d+)\s+green', curr)
        
            red = int(red_match.group(1)) if red_match else 0
            blue = int(blue_match.group(1)) if blue_match else 0
            green = int(green_match.group(1)) if green_match else 0

            curr = ""
            
            if red > RED or blue > BLUE or green > GREEN:
                return False
            else:
                continue
        curr += c


if __name__ == "__main__":
    main()