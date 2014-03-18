import sys

def main():
	if len(sys.argv) != 3:
		print("usage: python3 program.py [-e or -d] [shift amount]")
		sys.exit()

	try:
		shift = int(sys.argv[2])
	except ValueError:
		print("please enter an integer for shift amount")
		sys.exit()
	else:
		if sys.argv[1] == "-e":
			textToEncrypt = input("enter message to encrypt\n")
			print(encryptCaesar(textToEncrypt, shift))
		elif sys.argv[1] == "-d":
			textToDecrypt = input("enter message to decrypt\n")
			print(decryptCaesar(textToDecrypt, shift))
		else:
			print("usage: python3 program.py [-e or -d] [shift amount]")
			sys.exit()

def encryptCaesar(text, shift):
	encryptedText = list(text.lower())
	for i in range(len(encryptedText)):
		if ord(encryptedText[i]) >= 97 and ord(encryptedText[i]) <= 123:
			alphaIndex = ord(encryptedText[i]) - 96
			shiftedAlphaIndex = ((alphaIndex + shift) % 26) + 96
			encryptedText[i] = chr(shiftedAlphaIndex)
	return "".join(encryptedText)

def decryptCaesar(text, shift):
	decryptedText = list(text.lower())
	for i in range(len(decryptedText)):
		if ord(decryptedText[i]) >= 97 and ord(decryptedText[i]) <= 123:
			alphaIndex = ord(decryptedText[i]) - 96
			shiftedAlphaIndex = ((alphaIndex - shift) % 26) + 96
			decryptedText[i] = chr(shiftedAlphaIndex)
	return "".join(decryptedText)

if __name__ == "__main__":
	main()