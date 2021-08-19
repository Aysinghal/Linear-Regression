import random


def derivative(x_vals, y_vals, slope, intercept, learning_rate):
    step_size_intercept = 0
    step_size_slope = 0
    for i in range(0, len(x_vals)):
        step_size_intercept += (-2 * (y_vals[i] - (intercept + (slope * x_vals[i])))) * learning_rate
        step_size_slope += (-2 * x_vals[i] * (y_vals[i] - (intercept + (slope * x_vals[i])))) * learning_rate
    intercept -= step_size_intercept
    slope -= step_size_slope

    return [intercept, slope]


reps = int(input("Number of repetitions (the more reps, the more accurate the result): "))
learning_rate = float(input("Learning rate (the lower the rate, the more accurate the result): "))

x_vals = input("List all of the X values (separate by comma): ")
y_vals = input("List all of the Y values (separate by comma): ")
x_vals = x_vals.split(",")
y_vals = y_vals.split(",")
map_x_vals = map(int, x_vals)
map_y_vals = map(int, y_vals)
x_vals = list(map_x_vals)
y_vals = list(map_y_vals)
#x_vals = [0, 1, 2, 3, 4, 5, 6]
#y_vals = [4,7,10,13,16,19,22]

#learning_rate = 0.01
intercept = random.random()
slope = random.random()

for i in range(0, reps):
    output = derivative(x_vals, y_vals, slope, intercept, learning_rate)
    intercept = output[0]
    slope = output[1]

print(str(slope) + "x + " + str(intercept))
