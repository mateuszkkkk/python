from copy import deepcopy 
import random
size=random.randint(1,10)
Matrix1 = [[0 for x in range(size)]for y in range(size)]
for i in range(size):
	for j in range(size):
		Matrix1[i][j]=random.randint(-2,2)
print("Twoja macierz: ", Matrix1)
def Minor(matrix,i): 
	minor = deepcopy(matrix) 
	del minor[0] 
	for j in range(len(matrix)-1):
		del minor[j][i] 
	return minor

def Det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        det = 0
        for i in range(len(matrix)):
            det += matrix[0][i] * (-1) ** (2+i) * Det(Minor(matrix,i))
        return det
print("Wyznacznik macierzy wynosi: ",Det(Matrix1))
