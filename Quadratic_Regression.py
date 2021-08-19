import matplotlib.pyplot as plt


def quadratic_regression(x_data, y_data, learning=0.001, reps=10000):
    a = 0
    b = 0
    c = 0

    for i in range(0, reps):
        a, b, c = step_size(x_data, y_data, learning, a, b, c)

    return [round(a, 8), round(b, 8), round(c, 8)]
    # return [round(a, 4), round(b, 4), round(c, 4)]


def step_size(x_data, y_data, learning, a, b, c):
    step_size_a = 0
    step_size_b = 0
    step_size_c = 0

    for i in range(0, len(x_data)):
        step_size_a += (-2 * x_data[i] ** 2) * (y_data[i] - (a * x_data[i] ** 2) - (b * x_data[i]) - c)
        step_size_b += (-2 * x_data[i]) * (y_data[i] - (a * x_data[i] ** 2) - (b * x_data[i]) - c)
        step_size_c += -2 * (y_data[i] - (a * x_data[i] ** 2) - (b * x_data[i]) - c)

    step_size_a *= learning
    step_size_b *= learning
    step_size_c *= learning

    a -= step_size_a
    b -= step_size_b
    c -= step_size_c

    return a, b, c


x_data = [-3, -2, -1, 0, 1, 2, 3]
y_data = [11, 6, 3, 1, 3, 6, 11]

values = quadratic_regression(x_data, y_data)

print(values)
x = -1 * (values[1] / (2 * values[0]))
print("Vertex: (" + str(x) + ", " + str((values[0] * x ** 2) + (values[1] * x) + values[2]) + ")")

'''error = 0
for i in range(0, len(x_data)):
    error += (y_data[i] - ((values[0] * (x_data[i] ** 2)) + (values[1] * x_data[i]) + values[2])) ** 2
print(error)'''

a = []
b = []

x = min(x_data)

while x <= max(x_data) + 0.1:
    y = (values[0] * x ** 2) + (values[1] * x) + values[2]
    a.append(x)
    b.append(y)
    x += 0.1

plt.scatter(x_data, y_data, color='green')
plt.plot(a, b, color="red")

plt.show()