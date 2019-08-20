n=int(input())
s=0
copyback=0
i=1;
while(s<=(int)((n-1)/2)):
    copyback=s;
    s=s +(i);
    i+=1;       
if((n-copyback*2)>(s*2-n)):
    print(chr(95+i))
else:
      print(i-1);
      