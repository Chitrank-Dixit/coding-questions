# method 1:
def rec(n, bin, nbZeros, output):
  if nbZeros > 2:
    return
  elif n == 0:
    output.append(''.join(bin))
  else:
    bin.append('0')
    rec(n-1, bin, nbZeros+1, output)
    bin.pop()
    bin.append('1')
    rec(n-1, bin, nbZeros, output)
    bin.pop()

def binaryNumbers(n):
  output = []
  rec(n, [], 0, output)
  return output

# method 2:
def binaryNumbers(n):
  if n == 0:
    return ['']
  else:
    fromNext = binaryNumbers(n-1)
    output = []
    for bin in fromNext:
      if bin.count('0') < 2:
        output.append('0'+bin)
    for bin in fromNext:
      output.append('1'+bin)
    return output
	
