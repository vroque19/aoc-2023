def is_symbol(char):
    return char in "#$+=*-&/@%"

def is_valid_part(string, input, valid_pos, r, c, length):
    for i in range(length, 0, -1):
        # print(valid_pos[r][c-i], input[r][c-i])
        if valid_pos[r][c-i] == 1:
            return True
    return False
        # print(valid_pos[r][c-i], input[r][c-i])

def print_marked_pos(adj_list):
    for row in adj_list:
        print(row)

def mark_neighbors(mark, row, col, height, width):
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < height and 0 <= j < width and (i, j) != (row, col):
                mark[i][j] = 1

# 464347 too low
# 466411 too low
# 525181 correct
def main():
    with open("input1.txt", 'r') as f:
        lines = f.readlines()
        width = len(lines)-1
        height = len(lines[0])-1
        row = 0
        total = 0
        # print(height, width)
        mark = [[0 for i in range(width)]for i in range(height)]
        # print(mark)
        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if is_symbol(char):
                    mark_neighbors(mark, r, c, height, width)
            # print(line, end="")
            
        # analyze all the numbers
        for i in range(height):
            curr_part = ""
            for j in range(width+1):
                char = lines[i][j]
                if char.isdigit():
                    curr_part += char
                if not char.isdigit() and curr_part or j == width and curr_part:
                    length = len(curr_part)
                    valid = is_valid_part(curr_part, lines, mark, i, j, length)
                    # print(curr_part, valid)
                    if valid:
                        total += int(curr_part)
                    curr_part = ""
    print(total)

if __name__ == "__main__":
    main()