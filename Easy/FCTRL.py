#Problem Link:https://www.codechef.com/problems/FCTRL
try:
    for i in range(int(input())):
        n=int(input())
        d=5
        count=0
        while(n/d=>1):
            count=int(n/d)
            d=d*5
        print(count)
except:
    pass
