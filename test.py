coordinate = input("Enter your coordinate (x,y): ")
coordinate = coordinate.split(",")
x_coordinate = int(coordinate[0][1:])
y_coordinate = int(coordinate[1][:-1])


def find_closest_ten(value):
    value = abs(value)
    test_val = 0
    while True:
        test_val += 10
        if 10 >= test_val - value > 0:
            return test_val
            break


for i in range(-1 * find_closest_ten(y_coordinate), find_closest_ten(y_coordinate)):
    row = ''
    if i == 0:
        for j in range(-1 * find_closest_ten(x_coordinate), find_closest_ten(x_coordinate)):
            row += "- "
        print(row)
        continue
    for j in range(-1 * find_closest_ten(x_coordinate), find_closest_ten(x_coordinate)):
        if j == 0:
            row += '| '
        elif j == x_coordinate and i == y_coordinate:
            row += "* "
        else:
            row += '  '
    print(row)
