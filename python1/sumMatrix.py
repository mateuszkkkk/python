import random
Matrix1 = [[0 for x in range(128)]for y in range(128)]
Matrix2 = [[0 for x in range(128)]for y in range(128)]
Matrix3 = [[0 for x in range(128)]for y in range(128)]
for i in range(128):
	for j in range(128):
		Matrix1[i][j]=random.randint(-5,5)
		Matrix2[i][j]=random.randint(-5,5)
		Matrix3[i][j]=Matrix1[i][j]+Matrix2[i][j]
print(Matrix1)
print(Matrix2)
print(Matrix3)
