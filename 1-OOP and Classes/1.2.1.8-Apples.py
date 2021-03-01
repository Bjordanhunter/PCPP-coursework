from random import uniform

class Apple:
    totalWeight = 0
    totalApples = 0

    def __init__(self, weight):
        self.weight = weight

        Apple.totalWeight += self.weight
        Apple.totalApples += 1

maxApples = 1000
maxWeight = 350

while Apple.totalApples < maxApples:
    newAppleWeight = uniform(0.2,0.5)
    if Apple.totalWeight+newAppleWeight < maxWeight:
        newApple = Apple(newAppleWeight)
    else:
        break

print(f"total number of apples: {Apple.totalApples}")
print(f"total weight of apples: {Apple.totalWeight}")