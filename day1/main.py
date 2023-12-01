def part2(line, tot):
    curr = ""
    nums = ""
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for c in line:
        curr += c
        if c.isdigit():
            nums += c
            curr = ""
        for i in range(len(digits)):
            if digits[i] in curr:
                nums += str(i+1)
                curr = curr[len(curr)//2:]
    if len(nums) == 1:
        nums = nums*2
    n = len(nums)
    curr = ""
    curr += str(nums[0])
    curr += str(nums[n-1])
    # print(f"(current){curr} +(previous){tot}")
    return int(curr)

def part1(line):
    curr = ""
    nums = ""
    for c in line:
        curr += c
        if c.isdigit():
            nums += c
            curr = ""
    if len(nums) == 1:
        nums = nums*2
    n = len(nums)
    curr = ""
    curr += str(nums[0])
    curr += str(nums[n-1])
    return int(curr)

def main():
    with open("input.txt", "r") as f:
        total = 0
        for line in f:
            curr = "" 
            line.rstrip()
            nums = ""
            # total += part1(line)
            print(line)
            total += part2(line, total)
            print(total)
            
        print(total)
        
if __name__ == "__main__":
    main()
                
