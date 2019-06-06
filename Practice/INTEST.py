#Problem Link: https://www.codechef.com/problems/INTEST
try:
    n,k=input().split()
    n=int(n)
    k=int(k)
    ctr=0
    for i in range(n):
        x=int(input())
        if (x%k==0):
            ctr=ctr+1
    print(ctr)        
except:
    pass
