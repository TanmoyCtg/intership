'''
In this problem, we give a input 12. which is string and and convert it integer and 
make it 21. if the input is 500 , the possible outcome is 5. This solution not working in 
minus number. if input is -5 output should be -5. But this not gonna work.
'''

import math
def reverseInt(n):

	l = list(n)
	r = "".join(reversed(l))
	i = int(r)
	return i 	

if __name__ == "__main__":

	i = input("Input: ")
	print(reverse_int(i))
	#print(reverseInt(i))
