import matplotlib.pyplot as plt
import numpy
import random
import Quadratic_Regression as qr


def choose_shop(customers, price1, price2, rationality=20):
    prob_shop1 = (price2 / price1) ** rationality
    prob_shop2 = (price1 / price2) ** rationality
    prob_shop1 = prob_shop1 / (prob_shop1 + prob_shop2)
    shop1_purchased = 0
    for i in range(0, customers):
        shop1_purchased += numpy.random.binomial(1, prob_shop1)
    return [shop1_purchased, customers - shop1_purchased]


shop1 = [[], []]
shop2 = [[], []]

for i in range(0, 10):
    shop1_price = random.randint(1, 100)
    shop2_price = random.randint(1, 100)
    shop1[0].append(shop1_price)
    shop2[0].append(shop2_price)
    choices = choose_shop(200, shop1_price, shop2_price)
    shop1[1].append(choices[0] * shop1_price)
    shop2[1].append(choices[1] * shop2_price)

print(shop1)
print(shop2)

plt.scatter(shop1[0], shop1[1], color = "green")
plt.show()

plt.scatter(shop2[0], shop2[1], color = "red")
plt.show()

print(qr.quadratic_regression(shop1[0], shop1[1]))
print(qr.quadratic_regression(shop2[0], shop2[1]))