#Problem Link:https://www.codechef.com/problems/SABAR
try:
    for i in range(int(input())):
        a,b=map(int,input().strip().split())
        print(a+b-1,abs(a-b)+1)
except:
    pass
