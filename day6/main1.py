import re
def main():
    with open("small.txt", 'r') as f:
        lines = f.readlines()
        times = lines[0].rstrip().split(": ")[1]
        times = re.findall(r'(\d+)', times)
        distances = lines[1].rstrip().split(": ")[1]
        distances = re.findall(r'(\d+)', distances)
        races = len(times)
        total = 0
        for i in range(races):
            count = 0
            dist = int(distances[i])
            time_remaining = int(times[i])
            for j in range(1, time_remaining):
                vel = j
                if isWin(time_remaining-j, vel, dist):
                    count += 1
            if i == 0:
                total = count
            else:
                total = total * count
            # print(count, total)
        print(total)
            
def isWin(time_remaining, vel, distance):
        end = vel*time_remaining
        if end > distance:
            # print(time_remaining, vel, distance)
            return True
        return False

if __name__ == "__main__":
    main()
