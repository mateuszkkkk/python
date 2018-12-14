import time
import threading
class Filozof(threading.Thread):
	def __init__(self, name, forks, stomach = 3):
		threading.Thread.__init__(self)
		self.name = name
		self.forks = forks
		self.amounts = 0
		self.stomach = stomach
	def run(self):
		if self.name % 2 == 0:
			self.run_even()
		else:
			self.run_odd()
		if self.amount < self.stomach:
			time.sleep(0.1)
			self.run()
	def run_even(self):
		first = self.name
		second = (self.name + 1) % len(self.forks)
		print("Filozof " + str(self.name) + " czeka na 1 widelec")
		self.forks[first].acquire()
		print("Filozof " + str(self.name) + " bierze 1 widelec")
		print("Filozof " + str(self.name) + " czeka na 2 widelec")
		self.forks[second].acquire()
		print("Filozof " + str(self.name) + " bierze 2 widelec")
		self.amount = self.amount +1
		print("Filozof " + str(self.name) + " je obiad")
		self.forks[second].release()
		print("Filozof " + str(self.name) + " odklada 2 widelec")
		self.forks[first].release()
		print("Filozof " + str(self.name) + " odklada 1 widelec")
	def run_odd(self):
		first = self.name
		second = (self.name + 1) % len(self.forks)
		print ("Filozof " + str(self.name) + " czeka na 1 widelec")
		if self.forks[first].acquire(False):
			print ("Filozof " + str(self.name) + " bierze 1 widelec")
			print ("Filozof " + str(self.name) + " czeka na 2 widelec")
			if self.forks[second].acquire(False):
				print ("Filozof " + str(self.name) + " bierze 2 widelec")
				self.amount += 1
				print ("Filozof " + str(self.name) + " zjadl")
				self.forks[second].release()
				print ("Filozof " + str(self.name) + " odklada 2 widelec")
				self.forks[first].release()
				print ("Filozof " + str(self.name) + " odklada 1 widelec")
			else:
				print ("Filozof " + str(self.name) + " nie dostal 2 widelca wiec upuszcza 1")
				print ("Filozof " + str(self.name) + " czeka")
				self.forks[first].release()
				time.sleep(0.1)
				self.run()
		else:
			print ("Filozof " + str(self.name) + " nie podniosl 1 widelca, czeka")
			time.sleep(0.1)
			self.run()
forks = []
amounts = []
philosophers = []
for i in range(5):
	forks.append(threading.Lock())
	amounts.append(0)
 
for name in range(5):
	philosophers.append(Filozof(name, forks, 2))
 
for philosopher in philosophers:
	philosopher.start()
 
for philosopher in philosophers:
	philosopher.join()
 
for philosopher in philosophers:
	print (philosopher.amounts)
 
print ("Zjedzone")
