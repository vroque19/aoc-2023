def printTypes(my_types):
    for type in my_types:
        print(type)

def sortByChar(my_list):
    custom_order = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
    new_list = sorted(my_list, key=lambda x: [custom_order[c] for c in x])
    return new_list

def getType(hand):
    hmap = dict()
    for c in hand:
        if c in hmap:
            hmap[c] += 1
        else:
            hmap[c] = 1
    min_key = min(hmap, key = lambda k: hmap[k])
    max_key = max(hmap, key = lambda k: hmap[k])
    if hmap[max_key] == 1:
        return 0
    if hmap[max_key] == 2:
        cnt = list(hmap.values()).count(2)
        if cnt == 1:
            return 1
        return 2
    if hmap[max_key] == 3:
        if hmap[min_key] == 2:
            return 4
        return 3
    if hmap[max_key] == 4:
        return 5
    if hmap[max_key] == 5:
        return 6

def main():
    with open("small1.txt", 'r') as f:
        lines = f.readlines()
        hands = []
        types = [[] for _ in range(7)]
        hand_to_bid = {}
        winnings = 0
        for line in lines:
            hand = line.split(' ')[0]
            bid = line.split(' ')[1].rstrip()
            hand_to_bid[hand] = bid
            # sort by type
            hand_type = getType(hand)
            if hand_type == 0:
                types[0].append(hand)
            if hand_type == 1:
                types[1].append(hand)
            if hand_type == 2:
                types[2].append(hand)
            if hand_type == 3:
                types[3].append(hand)
            if hand_type == 4:
                types[4].append(hand)
            if hand_type == 5:
                types[5].append(hand)
            if hand_type == 6:
                types[6].append(hand)
        # sort by chars
        for i in range(7):
            types[i] = sortByChar(types[i])
        start = 1
        # printTypes(types)
        for i in range(len(types)):
            # print(types[i])
            # print("length:", len(types[i]))
            for j in range(len(types[i])):
                # print(i, j)
                # print(types[i][j], i, j)
                # print("adding", hand_to_bid[types[i][j]], "times", start)
                winnings += start*int(hand_to_bid[types[i][j]])
                start += 1
        print(winnings)
        # print(types)



if __name__ == "__main__":
    main()