def multiple_inside(values, place_val):
    total = 0
    for i in range(1, len(values.keys()) - 1):
        total += values.get(list(values.keys())[i])[0] * values.get(list(values.keys())[i])[1][place_val]
    return total


# Multi-variable Derivative
def derivative(values):
    learning_rate = 0.01
    intercept_step = 0
    # Derivative of intercept
    for i in range(0, len(values.get("d1")[1])):
        intercept_step += (-2 * (
                values.get("y-vals")[i] - (values.get("intercept") + multiple_inside(values, i)))) * learning_rate

    # Derivative of all dimensions
    dimension_steps = []
    for i in range(1, len(values.keys()) - 1):
        dimension_step = 0
        for j in range(0, len(values.get("d1")[1])):
            dimension_step += (-2 * values.get(list(values.keys())[i])[1][j] * (
                    values.get("y-vals")[i] - (values.get("intercept") + multiple_inside(values, i)))) * learning_rate
        dimension_steps.append(dimension_step)

    # Assign values to dictionary
    values["intercept"] = values.get("intercept") - intercept_step
    for i in range(1, len(dimension_steps)):
        values.get(list(values.keys())[i])[0] -= dimension_steps[i]


# Input Statement
values = {"intercept": 0, "d1": [1, [1, 2, 3, 4, 5]], "d2": [1, [1, 2, 3, 4, 5]], "d3": [1, [1, 2, 3, 4, 5]],
          "y-vals": [1, 2, 3, 4, 5]}
'''data = 0
dimension = 0
# Input of as many dimensions as needed
while True:
    dimension += 1
    data = input("List: ")
    if data == "break":
        break
    data = data.split(",")
    data = list(map(int, data))
    values[("d" + str(dimension))] = [0, data]

# Input of y-values
data = input("List: ")
data = data.split(",")
data = list(map(int, data))
values["y-vals"] = [data]'''
for i in range(0, 20000):
    derivative(values)

print(values)