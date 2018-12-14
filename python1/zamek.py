haslo = input("Podaj kod potrzebny do sprawdzenia: ")
while True:
	haslo2 = input("Podaj wczesniej ustalony kod: ")
	if haslo2 == haslo:
		print("Poprawne haslo.")
		break
	print("Bledne haslo, sprobuj ponownie.")
	

