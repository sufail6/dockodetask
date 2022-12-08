

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))


matrix = [[0 for j in range(C)] for i in range(R)]

num = 1
for i in range(R):
	for j in range(C):
		matrix[i][j] = num
		num += 1


for i in range(R):
	for j in range(C):
		print(matrix[i][j], end="   ")
	print()

