import random
list = random.sample(range(0,1000), 100)
print(list)

list.remove(max(list))
print(max(list))