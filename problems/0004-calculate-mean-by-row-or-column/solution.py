def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	if mode == "row":
		means = []
		for i in range(len(matrix)):
			total = 0
			for j in range(len(matrix[i])):
				total += matrix[i][j]
			mean = total / len(matrix[i])
			means.append(mean)
	elif mode == "column":
		means = []
		for j in range(len(matrix[0])):
			total = 0
			for i in range(len(matrix)):
				total += matrix[i][j]
			mean = total / len(matrix)
			means.append(mean)
	return means