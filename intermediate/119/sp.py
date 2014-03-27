"""
Shortest Path

http://www.reddit.com/r/dailyprogrammer/comments/17jvoh/013013_challenge_119_intermediate_find_the/
"""

import queue
import math
import heapq
import sys
import time

# turn text input into a 2-dimensional array, then finds the shortest path 2 ways
def main():
	if len(sys.argv) != 2 or (sys.argv[1] != '-d' and sys.argv[1] != '-a'):
		print("usage: sp.py [opt]")
		print("    options are -d for depth first search, or -a for a* search")
		sys.exit()

	gridSize = int(input())
	world = [gridSize * [0] for i in range(gridSize)]

	startPos = ()
	endPos = ()

	for i in range(gridSize):
		worldRow = list(input())
		world[i] = worldRow
		for j in range(gridSize):
			if worldRow[j] == 'S':
				startPos = (i, j)
			elif worldRow[j] == 'E':
				endPos = (i, j)

	if sys.argv[1] == '-d':
		bfsStart = time.clock()
		breadthFirstSearch(world, startPos)
		print("bfs time taken: {0:.5f}".format(time.clock() - bfsStart))
	else:
		asStart = time.clock()
		aStarSearch(world, startPos, endPos)
		print("a* time taken: {0:.5f}".format(time.clock() - asStart))
	
# basic breadth first search using a queue
def breadthFirstSearch(world, startPos):
	q = queue.Queue()
	# add distance from start tile so final distance can be calculated
	startPos = (startPos[0], startPos[1], 0)
	q.put(startPos)
	done = False
	while not q.empty() and not done:
		curr = q.get()
		if curr[0] > 0:
			north = (curr[0] - 1, curr[1], curr[2] + 1)
			done = checkTileDfs(north, world, q)

		if curr[1] < len(world) - 1:
			east = (curr[0], curr[1] + 1, curr[2] + 1)
			done = checkTileDfs(east, world, q)

		if curr[0] < len(world) - 1:
			south = (curr[0] + 1, curr[1], curr[2] + 1)
			done = checkTileDfs(south, world, q)

		if curr[1] > 0:
			west = (curr[0], curr[1] - 1, curr[2] + 1)
			done = checkTileDfs(west, world, q)
	if not done:
		print("no path found")	

# a* search using distance as the crow flies for a heuristic
def aStarSearch(world, startPos, endPos):
	heap = []
	# add distance from start tile so final distance can be calculated
	startPos = (startPos[0], startPos[1], 0)
	pushToHeap(heap, startPos, endPos)
	done = False
	while len(heap) > 0 and not done:
		curr = heapq.heappop(heap)[1]
		if curr[0] > 0:
			north = (curr[0] - 1, curr[1], curr[2] + 1)
			done = checkTileAStar(north, world, heap, endPos)

		if curr[1] < len(world) - 1:
			east = (curr[0], curr[1] + 1, curr[2] + 1)
			done = checkTileAStar(east, world, heap, endPos)

		if curr[0] < len(world) - 1:
			south = (curr[0] + 1, curr[1], curr[2] + 1)
			done = checkTileAStar(south, world, heap, endPos)

		if curr[1] > 0:
			west = (curr[0], curr[1] - 1, curr[2] + 1)
			done = checkTileAStar(west, world, heap, endPos)
	if not done:
		print("no path found")

# calculate distance between two points for a* heuristic
def pushToHeap(heap, pos, end):
	heuristic = math.hypot(end[0] - pos[0], end[1] - pos[1])
	heapq.heappush(heap, (heuristic, pos))

def checkTileAStar(tile, world, heap, end):
	if world[tile[0]][tile[1]] == '.':
		world[tile[0]][tile[1]] = 'Q'
		pushToHeap(heap, tile, end)	
		return False
	elif world[tile[0]][tile[1]] == 'E':
		print("True, " + str(tile[2]))
		return True

def checkTileDfs(tile, world, q):
	if world[tile[0]][tile[1]] == '.':
		world[tile[0]][tile[1]] = 'Q'
		q.put(tile)	
		return False
	elif world[tile[0]][tile[1]] == 'E':
		print("True, " + str(tile[2]))
		return True


if __name__ == "__main__":
	main()