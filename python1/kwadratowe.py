import math
a = float(input('Podaj wspolczynnik a (rozny od 0): '))
b = float(input('Podaj wspolczynnik b: '))
c = float(input('Podaj wspolczynnik c: '))
print('Twoje równanie to: y=',a,'x^2+',b,'x+',c)
d = float((b*b)-4*a*c)
print('Delta rownania wynosi: ',d)
if (d>0):
	sd = math.sqrt(d)
	x1 = ((-b)-sd)/(2*a)
	x2 = ((-b)+sd)/(2*a)
	print('Pierwiastki Twojego rownania to: x1 = ',x1,' oraz x2 = ',x2)
elif (d==0):
	x = (-b)/(2*a)
	print('Rozwianiem Twojego rownania jest: x = ',x)
else:
	print('Brak rozwiazan nieurojonych')

