# Python3 program to implement
# Luhn algorithm
# Returns true if given card
# number is valid
def checkLuhn(cardNo):
	nDigits = len(cardNo)
	nSum = 0
	isSecond = False
	
	for i in range(nDigits - 1, -1, -1):
		d = ord(cardNo[i]) - ord('0')
        
		if (isSecond == True):
			d = d * 2
		# We add two digits to handle
		# cases that make two digits after
		# doubling
		nSum += d // 10
		nSum += d % 10

		isSecond = not isSecond
	
	if (nSum % 10 == 0):
	
		if (cardNo[0] =='2'):
			print("MasterCard")
	
		if (cardNo[0] =='3'):
			print("AmericanExpress")

		if (cardNo[0] == '4'):
			print("VISA")
		
		if (cardNo[0] =='5'):
			print("MasterCard")

		if (cardNo[0] =='6'):
			print("Discover")

		return True
	else:
		return False

# Driver code 
if __name__=="__main__":
	
	cardNo = "2221000000000009"
    	
	if (checkLuhn(cardNo)):
		print("VALID")
	else:
		print("INVALID")

# cardNo = "6176292929" invalid
# American Epress: 378282246310005
# American Express: 371449635398431
# American Express Corporate: 378734493671000
# Discover: 6011111111111117
# Discover: 6011000990139424
# MasterCard: 2221000000000009
# MasterCard: 2223000048400011
# MasterCard: 2223016768739313
# MasterCard: 5555555555554444
# MasterCard: 5105105105105100
# Visa: 	4111111111111111
# Visa: 4012888888881881
# Visa: 4222222222222
