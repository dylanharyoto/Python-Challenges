def amm():
    plane = []
    for i in range(10):
        plane.append(["*"] * 10)
    plane[2][2] = "M"
    current = [2, 2]
    move = input()
    for dir in move:
        y, x = current[0], current[1]
        plane[y][x] = "*"
        if dir == "N":
            y -= 1
        elif dir == "S":
            y += 1
        elif dir == "W":
            x -= 1
        elif dir == "E":
            x += 1
        plane[y][x] = "M"
        current[0], current[1] = y, x
    for i in plane:
        print("".join(i))
