import sys

def main():
	if len(sys.argv) != 2:
		print("usage: python3 pangram.py [input file]")
		sys.exit()
	inputFile = open(sys.argv[1], 'r')
	numLines = int(inputFile.readline())
	for i in range(numLines):
		sentence = inputFile.readline().lower()
		letterDict = {}
		for letter in sentence:
			if ord(letter) > 96 and ord(letter) < 124:
				try:
					occurences = letterDict[letter]
					letterDict[letter] = occurences + 1
				except KeyError:
					letterDict[letter] = 1
		if len(letterDict.keys()) == 26:
			print("True ")
		else:
			print("False ")
		print(str(letterDict).replace('{', '').replace('}', '').replace('\'', ''))



	inputFile.close()


if __name__ == "__main__":
	main()