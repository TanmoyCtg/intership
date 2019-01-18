
'''
# solution 1
def reverseString(str):
	
	a = str[::-1] 
	return a
	
'''

'''
# solution 2

def reverse(string):
	return "".join(reversed(string))
		
'''
	
# solution 3

def reverse_string(s):
	
	chars = list(s)
	for i in range(len(s) //2): # range(0,2)
		tmp = chars[i]  # chars[0] = 'a' => tmp = 'a'
		chars[i] = chars[len(s) - i - 1] # chars[0] = 'e' 
		chars[len(s) - i - 1] = tmp # chars[4] = 'a'
	return ''.join(chars)
	
a = input("Write down a string:")
print (reverse_string(a))


