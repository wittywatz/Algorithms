#For a number to be prime, it must be greater than one
def prime(n):
  if n<=1:
      return 0
  primes = []
  #Populate an array with true values of size n
  isPrime = [True,] * (n+1)
  
  #Set first and second element to false
  isPrime[0] = False
  isPrime[1] = False

  for i in range(2,n+1):
    if isPrime[i]:
      primes.append(i)
      for j in range(i+i,n+1,i):#Set multiples to false
        isPrime[j] = False
    
  return primes

def primeFactors(n):
  '''
  Finds all prime factors when given an integer value.
  '''
  try:
    if(n.is_integer()):
      n = int(n)
    assert type(n) == type(1) 
    if n<=1:
      return
    possiblePrime = prime(n)
    primy={}
    temp = n
    for i in possiblePrime:
      
      if temp == 1:
        break
      while temp % i == 0:
        if i not in primy:
          primy[i]=1
        else:
          primy[i]+=1
        temp/=i
    primeSorted = sorted(primy.keys())
    
    print(f"prime factors of {n}:" , end =" ")
    for i in range((len(primeSorted)-1)):
      if(primy[primeSorted[i]] > 1):
        print(f"{primeSorted[i]}^{primy[primeSorted[i]]} x", end = " ")
      else:
        print(f"{primeSorted[i]} x", end = " ")
    if(primy[primeSorted[-1]] > 1):
      print(f"{primeSorted[-1]}^{primy[primeSorted[-1]]}", end = "")
    else:
      print(f"{primeSorted[-1]}", end = "")
    return primy
  except AssertionError:
    print("Please Enter an Integer value")
  except:
    print('An error occurred')
  

primeFactors(2825.0000)