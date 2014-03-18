vertices, numLines = map(int, input().split())
matrix = [vertices * [0] for i in range(vertices)]

for i in range(numLines):
	symbols = input().split()
	splitIndex = 0
	for j in range(len(symbols)):
		if symbols[j] == '->':
			splitIndex = j
	
	fromNodes = symbols[:splitIndex]
	toNodes = symbols[splitIndex + 1:]

	for fromNode in fromNodes:
		for toNode in toNodes:
			matrix[int(fromNode)][int(toNode)] = 1

for i in range(vertices):
	print(matrix[i])
