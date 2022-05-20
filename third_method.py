import random
list = [random.randrange(0, 1000, 1) for i in range(100)]
print(list)

list_set = set(list)
list_set.remove(max(list_set))
print(max(list_set))