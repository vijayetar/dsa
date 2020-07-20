def find_fibonacci1(n):
  n1 = 0
  n2 = 1
  counter = 0
  while counter<n-1:
    next = n1+n2
    n1, n2 = n2, next
    counter += 1
  return next



def find_fibonacci2(n):
  def walk(n):
    if n==0:
      return 0
    elif n ==1:
      return 1
    else:
      sum = walk(n-1)+walk(n-2)
      return sum
  sum = walk(n)
  return sum

