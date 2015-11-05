__author__ = 'sanaes'

def factorial(n):
  fac = 1
  for i in range(1, n + 1):
    fac *= i
  return fac

def rank(str):
    rank = 0
    temp = 'a'
    for i in 'abcdefgh':
        if(i == str):
         temp = 0
         break
        elif(temp == 0):
            continue
        else:
            rank = rank+1
    return rank


def orderNum(str):
    orderNum = 0
    for i in range(0,6):
       orderNum += (rank(str[i]) * factorial(7-i))
    return orderNum


print orderNum('abcdefgh')

print factorial(6)

#(rank(arr,tgtArr[i]) * factorial(7-i));


#abcdefgh | 1
#abcdefhg | 2
#abcdegfh | 3
