import re
def main():
    with open("big.txt", 'r') as f:
        lines = f.readlines()
        # i didnt want to change my code
        time_remaining = int(''.join(re.findall(r'(\d+)', lines[0].split(":")[1])))
        dist = int(''.join(re.findall(r'(\d+)', lines[1].split(":")[1])))
        print(time_remaining)
        print(dist)
        total = 0
        small = 1
        found_small = False
        big = dist
        found_big = False
        while not found_small:
            for j in range(1, time_remaining):
                vel = j
                if isWin(time_remaining-j, vel, dist):
                    small = time_remaining-j
                    found_small = True
        while not found_big:
            for j in range(time_remaining, -1, -1):
                vel = j
                if isWin(time_remaining-j, vel, dist):
                    big = time_remaining-j
                    found_big = True
            total = big-small+1
        print("small", small)
        print("big", big)
    print(total)
            
def isWin(time_remaining, vel, distance):
        end = vel*time_remaining
        # print(end)
        if end > distance:
            # print(time_remaining, vel, distance)
            return True
        return False

if __name__ == "__main__":
    main()
