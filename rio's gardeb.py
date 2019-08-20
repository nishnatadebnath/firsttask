import numpy as np
n=int(input())
arr=np.zeros((n,n));
for i in range(n):
    s=input()
    k=0
    for j in s.split():
        arr[i,k]=np.int(j)
        k=k+1
k=int(input())
for z in range(0,n,k):
    sum=0
    for i in range(0,n,k):
        y=arr[z:z+k,i:i+k]
        avg=np.average(y)
        ar1=np.zeros((k,k))
        for a in range(k):
            for b in range(k):
                ar1[a,b]=int(avg)
        arr[z:z+k,i:i+k]=ar1
print (arr)

                
        
        
        
    
         
         
         
        