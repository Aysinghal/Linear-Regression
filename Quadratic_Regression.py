import matplotlib.pyplot as plt
import time


def quadratic_regression(x_data, y_data, learning=0.00000000001, reps=100000):
    a = float(0)
    b = float(0)
    c = float(0)

    for i in range(1, reps + 1):
        a, b, c = step_size(x_data, y_data, learning, a, b, c)
        #print(i, "/", reps)
        #print("<" + ("-" * int(i / reps * 15)).ljust(15, ' ') + ">")
        #print("\n" * 2)

    return [round(a, 8), round(b, 8), round(c, 8)]
    # return [round(a, 4), round(b, 4), round(c, 4)]


def step_size(x_data, y_data, learning, a, b, c):
    step_size_a = float(0)
    step_size_b = float(0)
    step_size_c = float(0)

    for i in range(0, len(x_data)):
        step_size_a += (-2 * x_data[i] ** 2) * (y_data[i] - (a * x_data[i] ** 2) - (b * x_data[i]) - c)
        step_size_b += (-2 * x_data[i]) * (y_data[i] - (a * x_data[i] ** 2) - (b * x_data[i]) - c)
        step_size_c += -2 * (y_data[i] - (a * x_data[i] ** 2) - (b * x_data[i]) - c)

    step_size_a *= learning
    step_size_b *= learning
    step_size_c *= (learning * 100000)

    a -= step_size_a
    b -= step_size_b
    c -= step_size_c
    print(c)

    return a, b, c


def data_regression(x_data, y_data, data_type):
    print(data_type + " - Regression Starting")
    time.sleep(2)

    values = quadratic_regression(x_data, y_data)

    print(data_type + " - Regression Complete")
    print(values)

    x = -1 * (values[1] / (2 * values[0]))
    print("Vertex: (" + str(x) + ", " + str((values[0] * x ** 2) + (values[1] * x) + values[2]) + ")")
    print("\n\n")
    time.sleep(2)

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

    plt.scatter(x_data, y_data, label=data_type + " - raw")
    plt.plot(a, b, label=data_type + " - learned")


y_data = []
x_data = []
for i in range(-200, 200, 2):
    y_data.append(i ** 2 + 5 * i + 300)
    x_data.append(i)


data_regression(x_data, y_data, "Test")

plt.legend()
plt.show()
