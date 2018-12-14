class Complex:
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag
	def __add__(self, second):
		return Complex(self.real + second.real, self.imag + second.imag)
	def __sub__(self, second):
		return(self.real - second.real, self.imag - second.imag)
	def __abs__(self):
		return(self.real**2 + self.imag**2)
	def __str__(self):
		return '(%g,%g)' % (self.real, self.imag)
first = Complex(1,1)
second = Complex(2,2)
print("first complex number: ", first)
print("second complex number: ", second)
print("addition: ", first+second)
print("substraction: ", first-second)
print("abs of the second complex number: ", abs(second))
