# non-tail recursive:
def countOccurrences(arr, num, i = 0):
	if i == len(arr):
		return 0
	elif arr[i] == num:
		return 1 + countOccurrences(arr, num, i+1)
	else:
		return countOccurrences(arr, num, i+1)
	
# tail recursive:
def countOccurrences(arr, num, i = 0, acc = 0):
	if i == len(arr):
		return acc
	elif arr[i] == num:
		return countOccurrences(arr, num, i+1, acc+1)
	else:
		return countOccurrences(arr, num, i+1, acc)