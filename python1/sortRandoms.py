import random
randomList = random.sample(range(1000), 50)
print(randomList)
listL = len(randomList) - 1
sort = 1
while (sort):
	sort = 0
	for i in range(listL):
		if (randomList[i] > randomList[i+1]):
			temp = randomList[i]
			randomList[i] = randomList[i+1]
			randomList[i+1] = temp
			sort = 1
print(randomList)
