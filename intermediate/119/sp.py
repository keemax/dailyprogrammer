"""
Shortest Path

http://www.reddit.com/r/dailyprogrammer/comments/17jvoh/013013_challenge_119_intermediate_find_the/
"""

import queue
import sys

def main():
	gridSize = int(input())
	world = [gridSize * [0] for i in range(gridSize)]
	q = queue.Queue()

	startPos = ()

	for i in range(gridSize):
		worldRow = list(input())
		world[i] = worldRow
		for j in range(gridSize):
			if worldRow[j] == 'S':
				startPos = (i, j, 0)

	q.put(startPos)
	while not q.empty():
		curr = q.get()
		if curr[0] > 0:
			north = (curr[0] - 1, curr[1], curr[2] + 1)
			checkTile(north, world, q)

		if curr[1] < gridSize - 1:
			east = (curr[0], curr[1] + 1, curr[2] + 1)
			checkTile(east, world, q)

		if curr[0] < gridSize - 1:
			south = (curr[0] + 1, curr[1], curr[2] + 1)
			checkTile(south, world, q)

		if curr[1] > 0:
			west = (curr[0], curr[1] - 1, curr[2] + 1)
			checkTile(west, world, q)

	print("no path found")


def checkTile(tile, world, q):
	if world[tile[0]][tile[1]] == '.':
			world[tile[0]][tile[1]] = 'Q'
			q.put(tile)	
	elif world[tile[0]][tile[1]] == 'E':
		print("True, " + str(tile[2]))
		sys.exit()


if __name__ == "__main__":
	main()