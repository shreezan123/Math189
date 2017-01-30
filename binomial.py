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
#Output came as "1 a^ 50 b^ 0 + 50 a^ 49 b^ 1 + 1225 a^ 48 b^ 2 + 19600 a^ 47 b^ 3 + 230300 a^ 46 b^ 4 + 2118760 a^ 45 b^ 5 +
# 15890700 a^ 44 b^ 6 + 99884400 a^ 43 b^ 7 + 536878650 a^ 42 b^ 8 + 2505433700 a^ 41 b^ 9 + 10272278170 a^ 40 b^ 10 +
# 37353738800 a^ 39 b^ 11 + 121399651100 a^ 38 b^ 12 + 354860518600 a^ 37 b^ 13 + 937845656300 a^ 36 b^ 14 + 2250829575120 a^ 35 b^ 15
# + 4923689695575 a^ 34 b^ 16 + 9847379391150 a^ 33 b^ 17 + 18053528883775 a^ 32 b^ 18 + 30405943383200 a^ 31 b^ 19 + 47129212243960 a^ 30 b^ 20
# + 67327446062800 a^ 29 b^ 21 + 88749815264600 a^ 28 b^ 22 + 108043253365600 a^ 27 b^ 23 + 121548660036300 a^ 26 b^ 24 +
# 126410606437752 a^ 25 b^ 25 + 121548660036300 a^ 24 b^ 26 + 108043253365600 a^ 23 b^ 27 + 88749815264600 a^ 22 b^ 28 +
# 67327446062800 a^ 21 b^ 29 + 47129212243960 a^ 20 b^ 30 + 30405943383200 a^ 19 b^ 31 + 18053528883775 a^ 18 b^ 32 +
# 9847379391150 a^ 17 b^ 33 + 4923689695575 a^ 16 b^ 34 + 2250829575120 a^ 15 b^ 35 + 937845656300 a^ 14 b^ 36 +
# 354860518600 a^ 13 b^ 37 + 121399651100 a^ 12 b^ 38 + 37353738800 a^ 11 b^ 39 + 10272278170 a^ 10 b^ 40 + 2505433700 a^ 9 b^ 41 +
# 536878650 a^ 8 b^ 42 + 99884400 a^ 7 b^ 43 + 15890700 a^ 6 b^ 44 + 2118760 a^ 5 b^ 45 + 230300 a^ 4 b^ 46 + 19600 a^ 3 b^ 47 +
# 1225 a^ 2 b^ 48 + 50 a^ 1 b^ 49 + 1 a^ 0 b^ 50
