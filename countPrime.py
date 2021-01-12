#For a number to be prime, it must be greater than one
def countPrime(n):
    """
    Returns the count of prime numbers when given an integer n
    """
    if n<=1:
        return 0
    count = 0
    #Populate an array with true values of size n
    isPrime = [True,] * n
    
    #Set first and second element to false
    isPrime[0] = False
    isPrime[1] = False

    for i in range(2,n):
        if isPrime[i]:
            count +=1
            for j in range(i+i,n,i):#Set multiples to false
                isPrime[j] = False

    return count
    
    print(countPrime(100))
