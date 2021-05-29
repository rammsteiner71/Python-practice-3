import math
import random

summ = 0
amount_of_tries = 1000000
for i in range(amount_of_tries):
    x = random.random()
    y = random.random()
    summ += math.sqrt(x ** 2 + y ** 2)
pi = summ * 4 / amount_of_tries
print(pi)