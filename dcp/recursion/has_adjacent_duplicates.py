def hasAdjacentDuplicates(str, i=1):
  if i >= len(str):
    return False
  elif str[i] == str[i-1]:
    return True
  else:
    return hasAdjacentDuplicates(str, i+1)