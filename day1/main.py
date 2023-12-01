digits = ["notvaliddigits", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("input.txt", "r") as f:
    total = 0
    for line in f:
        curr = "" 
        line.rstrip()
        nums = ""
        
        for c in line:
            curr += c
            for i in range(len(digits)):
                if str(digits[i]) in curr:
                    nums += str(i)
                    curr = curr[1:len(curr)]
            if c.isdigit():
                nums += c
                curr = ""
        if len(nums) == 1:
            nums = nums*2
        n = len(nums)
        curr = ""
        curr += str(nums[0])
        curr += str(nums[n-1])
        # print(line, nums[0], nums[n-1], total)

        total += int(curr)
    print(total)