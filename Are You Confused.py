import math
def ayc2():
    plane = []
    string = input()
    len_row = int(input())
    num_row = math.ceil(len(string) / len_row)
    area = num_row * len_row
    for i in range(num_row):
        plane += [["*"] * len_row]
    index = 0
    for y in range(len_row):
        case = 0
        if y + 1 >= (area - len(string)):
            case = 1
        for x in range(num_row - case):
            plane[x][y] = string[index + x]
        index += num_row - case
    final = ""
    for i in plane:
        final += "".join(i)
    print(final[:len(string)])
