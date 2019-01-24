def chunk(array, size):
	chunked = []
	index = 0
	
	while (index < len(array)):
		chunked.append(array[index:index+size])
		index+=size
		
	return chunked

if __name__ == '__main__':
	a = [1,2,3,4]
	s = 2
	print(chunk(a,s))
