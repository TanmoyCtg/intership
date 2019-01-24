def fizzbuzzProblem(n):
	
	for i in range(1,n):
		
		if (n%3==0 and n%5==0):
			return "fizzbuzz"
		elif (n%3 == 0):
			return "fizz"
		elif (n%5 == 0):
			return "buzz"
		else:
			return i
	
			

if __name__ == "__main__":
	n = int (input("Enter the number: "))
	print(fizzbuzzProblem(n))
