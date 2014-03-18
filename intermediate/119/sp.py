import queue

gridSize = int(input())

world = [gridSize * [0] for i in range(gridSize)]
startPos = ()
endPos = ()

for i in range(gridSize):
	worldRow = list(input())
	world[i] = worldRow
	for j in range(gridSize):
		if worldRow[j] == 'S':
			startPos = (i, j, 0)

q = queue.Queue()
q.put(startPos)
found = False
while not q.empty():
	curr = q.get()
	if world[curr[0]][curr[1]] == 'E':
		print("path length = ", curr[2])
		break
	world[curr[0]][curr[1]] = 'W'
	for i in range(gridSize):
		print(world[i])
	print('\n')
	if curr[0] > 0:
		north = (curr[0] - 1, curr[1], curr[2] + 1)
		if world[north[0]][north[1]] != 'W':
			q.put(north)

	if curr[1] < gridSize - 1:
		east = (curr[0], curr[1] + 1, curr[2] + 1)
		if world[east[0]][east[1]] != 'W':
			q.put(east)

	if curr[0] < gridSize - 1:
		south = (curr[0] + 1, curr[1], curr[2] + 1)
		if world[south[0]][south[1]] != 'W':
			q.put(south)

	if curr[1] > 0:
		west = (curr[0], curr[1] - 1, curr[2] + 1)
		if world[west[0]][west[1]] != 'W':
			q.put(west)

