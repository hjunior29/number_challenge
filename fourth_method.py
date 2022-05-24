import random
list = [random.randrange(0, 1000, 1) for i in range(100)]
print(list)

lenght = 0
for element in list:
    lenght += 1

for i in range(lenght):
    while i != 0 and list[i] > list[i-1]:
        aux = list[i]
        list[i] = list[i-1]
        list[i-1] = aux
        i = i - 1

for i in range(lenght):
    if list[i] > list[i+1]:
        print(list[i+1])
        break