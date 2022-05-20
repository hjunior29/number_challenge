import random
list = random.sample(range(0,1000), 100)
print(list)

list_sorted = sorted(list)
print(list_sorted[len(list_sorted)-2])