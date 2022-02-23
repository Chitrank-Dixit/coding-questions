# non-tail recursive:
def sumOfDigts(n):
    if n < 0:
		return sumOfDigts(-n)
    elif n < 10:
		return n
    else:
		return (n % 10) + sumOfDigts(n // 10)
	
# tail recursive:
def sumOfDigts(n, acc=0):
	if n < 0:
		return sumOfDigits(-n)
	elif n < 10:
		return n+acc
	else:
		return sumOfDigits(n//10, acc+n%10)