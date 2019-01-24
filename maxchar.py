def maxchar(string):
	charmap = dict()
	max_count = 0
	
	for letter in string:
		if letter not in charmap:
			charmap[letter] = 1
		else:
			charmap[letter]+=1
		
		if charmap[letter] > max_count:
			max_count = charmap[letter]
			most_repeated_char = letter
	
	return most_repeated_char

	

if __name__ == "__main__":
	i = input("Enter the string:")
	print("Most frequent character: "+maxchar(i))

