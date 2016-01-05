import math
import hashlib

hashKey = "bgvyzdsv"

def getFirst5():
	hashInput = ""
	for i in range(100000000):
		# no leading 0s
		stri = str(i)

		hashInput = hashKey + stri
		hasher = hashlib.md5(hashInput)
		hashOutput = hasher.hexdigest()

		if hashOutput[:6] == '000000':
			print hashOutput
			print i
			return

def main():
	getFirst5()

if __name__ == '__main__':
	main()