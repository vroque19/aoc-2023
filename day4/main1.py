import re

# 28276 not correct
def main():
    with open("input1.txt", 'r') as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            line = line.split(':')[1]
            matches1 = re.findall(r'\d+', line.split('|')[0])
            matches2 = re.findall(r'\d+', line.split('|')[1])
            print(matches1)
            print(matches2)

            winning_nums = list(map(int, matches1))
            my_nums = list(map(int, matches2))
            my_wins = []
            
            for num in my_nums:
                if num in winning_nums:
                    my_wins.append(num)
            if len(my_wins) > 0:
                total += 2**(int(len(my_wins)-1))
            else: total += 0
        print(total)


if __name__ == "__main__":
    main()