#Problem Link: https://www.codechef.com/problems/FCTRL2
try:
    for i in range(int(input())):
        n=int(input())
        ans=1
        for x in range(2,n+1):
            ans=ans*x
        print(ans)
except:
    pass
