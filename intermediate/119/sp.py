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
		breadthFirstSearch(world, startPos)
	else:
		aStarSearch(world, startPos, endPos)
	
# basic breadth first search using a queue
def breadthFirstSearch(world, startPos):
	q = queue.Queue()
	# add distance from start tile so final distance can be calculated
	startPos = (startPos[0], startPos[1], None)
	q.put(startPos)
	lastTile = None
	while not q.empty() and lastTile == None:
		curr = q.get()
		if curr[0] > 0:
			north = (curr[0] - 1, curr[1], curr)
			lastTile = checkTileDfs(north, world, q)

		if curr[1] < len(world) - 1:
			east = (curr[0], curr[1] + 1, curr)
			lastTile = checkTileDfs(east, world, q)

		if curr[0] < len(world) - 1:
			south = (curr[0] + 1, curr[1], curr)
			lastTile = checkTileDfs(south, world, q)

		if curr[1] > 0:
			west = (curr[0], curr[1] - 1, curr)
			lastTile = checkTileDfs(west, world, q)
	if lastTile == None:
		print("no path found")
	else:
		printFinishedWorld(world, lastTile)	


# a* search using distance as the crow flies for a heuristic
def aStarSearch(world, startPos, endPos):
	heap = []
	# add distance from start tile so final distance can be calculated
	# also add the previously travelled tile
	startPos = (startPos[0], startPos[1], None)
	pushToHeap(heap, startPos, endPos)
	lastTile = None
	while len(heap) > 0 and lastTile == None:
		curr = heapq.heappop(heap)[1]
		if curr[0] > 0:
			north = (curr[0] - 1, curr[1], curr)
			lastTile = checkTileAStar(north, world, heap, endPos)

		if curr[1] < len(world) - 1:
			east = (curr[0], curr[1] + 1, curr)
			lastTile = checkTileAStar(east, world, heap, endPos)

		if curr[0] < len(world) - 1:
			south = (curr[0] + 1, curr[1], curr)
			lastTile = checkTileAStar(south, world, heap, endPos)

		if curr[1] > 0:
			west = (curr[0], curr[1] - 1, curr)
			lastTile = checkTileAStar(west, world, heap, endPos)
	if lastTile == None:
		print("no path found")
	else:
		printFinishedWorld(world, lastTile)

# calculate distance between two points for a* heuristic
def pushToHeap(heap, pos, end):
	heuristic = math.hypot(end[0] - pos[0], end[1] - pos[1])
	heapq.heappush(heap, (heuristic, pos))

def checkTileAStar(tile, world, heap, end):
	if world[tile[0]][tile[1]] == '.':
		world[tile[0]][tile[1]] = 'Q'
		pushToHeap(heap, tile, end)	
		return None
	elif world[tile[0]][tile[1]] == 'E':
		return tile

def checkTileDfs(tile, world, q):
	if world[tile[0]][tile[1]] == '.':
		world[tile[0]][tile[1]] = 'Q'
		q.put(tile)	
		return None
	elif world[tile[0]][tile[1]] == 'E':
		return tile

def printFinishedWorld(world, lastTile):
	pathCount = 0
	while lastTile[2] != None:
		pathCount += 1
		world[lastTile[0]][lastTile[1]] = '@'
		lastTile = lastTile[2]

	for worldRow in world:
		for tile in worldRow:
			if tile == 'Q':
				print('.', end='')
			else:
				print(tile, end='')
		print('')

	print("True, {0}".format(pathCount))

if __name__ == "__main__":
	main()