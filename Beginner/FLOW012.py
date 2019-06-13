#Problem Link : https://www.codechef.com/problems/FLOW012/
try:
    for i in range(int(input())):
        a,b,c=map(int,input().strip().split())
        if a+b+c==180:
            print('YES')
        else:
            print('NO')
except:
    pass
