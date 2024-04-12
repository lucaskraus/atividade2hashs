import hashlib


def sha256(myString):
	stringHashed = hashlib.sha256(myString.encode('utf-8')).hexdigest()
	return stringHashed


def md5(myString):
	stringHashed = hashlib.md5(myString.encode('utf-8')).hexdigest()
	return stringHashed


def main():
	with open('frases.txt', 'r') as file:
		frases = file.readlines()

	for frase in frases:
		frase_stripped = frase.strip()
		if frase_stripped:
			print("Frase:", frase_stripped)
			print(sha256(frase_stripped), "-", md5(frase_stripped))
			print()


if __name__ == "__main__":
	main()
