#Problem Link : https://www.codechef.com/problems/FLOW009/
try:
    for i in range(int(input())):
        a,b=map(int,input().strip().split())
        if a>1000:
            print(str.format('{0:.6f}',float(0.9*a*b)))
        else:
            print(str.format('{0:.6f}',float(a*b)))
except:
    pass
