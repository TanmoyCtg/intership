def is_palindrome(string):
	reverse_string = string[::-1]
	if reverse_string == string:
		return "it is palindrome"
		
		
	else:
		return "it is not palindrome"

if __name__ == "__main__":

	p = input("Enter your string:")
	print(is_palindrome(p))

