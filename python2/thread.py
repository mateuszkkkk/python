import random
import threading
def array(size):
	array = [0 for x in range(size)]
	return array
def histogramS(size):
	histogram = [0 for x in range(size)]
	for i in range(size):
		histogram[i]=random.randint(0,10)
	return histogram
def histogramC(array, histogram):
	for i in array:
		histogram[i] = histogram[i] + 1
	return histogram
array = array(10)
histogram1 = histogramS(50000)
p1 = threading.Thread(target=histogramC, args=(array, histogram1[0:25000]))
p2 = threading.Thread(target=histogramC, args=(array, histogram1[25000:50000]))
p1.start()
p2.start()
p1.join()
p2.join()

