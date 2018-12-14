import random
from multiprocessing import Pool
def array(size):
	array = [0 for x in range(size)]
	for i in range (size):
		array[i]=random.randint(0,30)
	return array
def histogramS(size):
	histogram = [0] * size
	return histogram
def histogramC(array, histogram):
	for i in array:
		histogram[i] = histogram[i] + 1
	return histogram
array = array(50)
histogram1 = histogramS(50)
p = Pool()
result = p.map(histogramC(array,histogram1), range(10000))
print(result)

