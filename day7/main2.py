def printTypes(my_types):
    for type in my_types:
        print(type)

def sortByChar(my_list):
    custom_order = {'A': 13, 'K': 12, 'Q': 11, 'J': 0, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
    new_list = sorted(my_list, key=lambda x: [custom_order[c] for c in x])
    return new_list

def getType(hand):
    hmap = dict()
    j_cnt = 0
    for c in hand:
        if c == 'J':
            j_cnt += 1
        if c in hmap:
            hmap[c] += 1
        else:
            hmap[c] = 1
        
    min_key = min(hmap, key = lambda k: hmap[k])
    max_key = max(hmap, key = lambda k: hmap[k])
    print(max_key, hmap[max_key], hand, j_cnt, hmap[max_key]+j_cnt, list(hmap.values()).count(2))
    if max_key == 'J':
        if list(hmap.values()).count(1) == 2:
            return hmap[max_key]
        if list(hmap.values()).count(1) == 5:
            return hmap[max_key]
        if hmap[min_key] == 2:
            return 6
        if list(hmap.values()).count(2) == 2:
            return 5
    if hmap[max_key]+j_cnt == 1:
        return 0
    if hmap[max_key]+j_cnt == 2:
        cnt = list(hmap.values()).count(2)
        if cnt == 1:
            return 1
        return 2
    if hmap[max_key]+j_cnt == 3:
        if hmap[min_key] == 2:
            return 4
        return 3
    if hmap[max_key]+j_cnt == 4:
        return 5
    if hmap[max_key]+j_cnt == 5:
        return 6
# 246809074 too low
# 248213461 too low
# 238056487 too low
# 252006926 too low
# 252113970
# 250531419 too low
# 248638607 too low
# 247163100 too low
def main():
    with open("big1.txt", 'r') as f:
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
        printTypes(types)
        for i in range(len(types)):
            for j in range(len(types[i])):
                winnings += start*int(hand_to_bid[types[i][j]])
                start += 1
        print(winnings)

if __name__ == "__main__":
    main()