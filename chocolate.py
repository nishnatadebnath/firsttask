import sympy as sp
n=int(input())
counter=0
while n>=2 :
    counter+=1
    n=n-sp.prevprime(n+1)
if(n==1):
    print(counter+1)
else:
    print(counter)