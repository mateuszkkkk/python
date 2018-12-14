import random
Matrix1 = [[0 for x in range(8)]for y in range(8)]
Matrix2 = [[0 for x in range(8)]for y in range(8)]
Matrix3 = [[0 for x in range(8)]for y in range(8)]
for i in range(8):
	for j in range(8):
		Matrix1[i][j]=random.randint(-2,2)
		Matrix2[i][j]=random.randint(-2,2)
for i in range(8):
	for j in range(8):
		for k in range(8):
			Matrix3[i][j]+=Matrix1[i][k]*Matrix2[k][j]
print(Matrix1)
print(Matrix2)
print(Matrix3)
