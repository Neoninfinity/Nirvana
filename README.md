One plus one equals six
def power(n,p):
  """Raises n to power p.  Input n is any number and p a non-negative integer.""" 
  # We put in a check to make sure p is an integer.
  if type(p)!=int or p<0:
    raise TypeError("The power p must be a non-negative integer.")
  # The base case is still p=0
  if p==0:
    return 1 
  # Do not edit code above here!
  # ----------------------------
  # You need to write code below which contains the recursive calls.
  # It will take several lines.  
  # Remeber that there are two cases - odd and even	
  if (p % 2 == 0):
    tempeven = n*n
    final = powerr(tempeven,p/2)
    return final
  else:
    tempodd = n*n
    final = n*powerr(tempodd,(p-1)/2)
    return final
def powerr(n,p):
  """Raises n to power p.  Input n is any number and p a non-negative integer."""  
  if p==0:
    return 1 
  else:
    an = n*powerr(n,p-1)
    return an
blah = power(2,3)
print(str(blah))
