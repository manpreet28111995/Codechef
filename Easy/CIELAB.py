#Problem Link:https://www.codechef.com/problems/CIELAB
try:
    a,b=map(int,input().strip().split())
    n=a-b
    if(n%10!=9):
        n=n+1
    else:
        n=n-1
    print(n)
except:
    pass
