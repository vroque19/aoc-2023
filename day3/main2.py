def is_symbol(char):
    return char in "#$+=*-&/@%"

def is_valid_part(string, input, valid_pos, r, c, length, gears, num):
    for i in range(length, 0, -1):
        key = valid_pos[r][c-i]
        if key == num:
            if key not in gears:
                gears[key] = int(string)
                return False
            else:
                val = gears[key]
                # print(val, string)
                return True # there are two neighbors
    

def print_marked_pos(adj_list):
    for row in adj_list:
        print(row)

def mark_neighbors(mark, row, col, height, width, num):
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < height and 0 <= j < width and (i, j) != (row, col):
                mark[i][j] = num

def main():
    with open("input2.txt", 'r') as f:
        lines = f.readlines()
        width = len(lines)-1
        height = len(lines[0])-1
        row = 0
        total = 0
        num = 1
        
        gears = {} ## initialize dict to hold values of neighbors
        ###
        mark = [[0 for i in range(width)]for i in range(height)] # mark all neighbors
        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                ratio = 0
                if is_symbol(char):
                    mark_neighbors(mark, r, c, height, width, num)
        ###
                    # analyze all the numbers right after marking current neighbors
                    for i in range(height):
                        curr_part = ""
                        for j in range(width+1):
                            char = lines[i][j]
                            if char.isdigit():
                                curr_part += char
                            if not char.isdigit() and curr_part or j == width and curr_part:
                                length = len(curr_part)
                                valid = is_valid_part(curr_part, lines, mark, i, j, length, gears, num)
                                if valid:
                                    ratio = gears[num]*int(curr_part)
                                    total += ratio
                                    # print(curr_part, valid)
                                curr_part = ""
        ###
                    num += 1

        # print(gears)
    print(total)

if __name__ == "__main__":
    main()