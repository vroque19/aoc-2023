import re
def set_game_freq(hmap, length):
    for i in range(1, length):
        hmap[i] = 1
    return hmap
def get_curr_total(hmap, count):
    return 0
    ...
def get_winning_nums(winning_nums, my_nums):
    my_wins = []
    for num in my_nums:
        if num in winning_nums:
            my_wins.append(num)
    return my_wins

def update_game_freq(cards, curr_card, card_freq):
    # print("game:", curr_card)
    # print("duplicates:", cards)
    # count = card_freq[curr_card]
    for i in range(curr_card+1, curr_card+1+cards):
        card_freq[i] += 1
    return card_freq


# 28276 not correct
def main():
    with open("input2.txt", 'r') as f:
        lines = f.readlines()
        total = 0
        game_freq = dict()
        set_game_freq(game_freq, len(lines)+1)
        game_num = 1
        ### parse input
        for line in lines:
            line = line.split(':')[1]
            matches1 = re.findall(r'\d+', line.split('|')[0])
            matches2 = re.findall(r'\d+', line.split('|')[1])
        ###
            winning_nums = list(map(int, matches1))
            my_nums = list(map(int, matches2))
            my_wins = get_winning_nums(winning_nums, my_nums)
            duplicates = len(my_wins)

            if duplicates > 0:
                print(f"adding {duplicates}cards from game{game_num}")
                for i in range(game_freq[game_num]):
                    update_game_freq(duplicates, game_num, game_freq)

            total += game_freq[game_num]
            game_num += 1
        # print(game_freq)
        print(total)


if __name__ == "__main__":
    main()