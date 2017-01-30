#Copyright Shrijan Aryal
#recursive factorial calculating function
def factorialcalculator (n):
    if n <= 0 :
        return 1
    else:
        return n*factorialcalculator(n-1)

#this function passes its arguments onto the factorial function and returns the combination for any given r and n
def combinationcalculator(n,r):
    numerator = factorialcalculator(n)
    denominator = factorialcalculator(n-r)*factorialcalculator(r)
    return (numerator//denominator)

#this function returns the required expansion
def binomialexpansion(n):
    for k in range (0,n+1):
        temp_combination = combinationcalculator(n,k)
        print (temp_combination,"a^",n-k,"b^",k,"+",end=" ")

binomialexpansion(50)
