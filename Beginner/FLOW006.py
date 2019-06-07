#Problem Link: https://www.codechef.com/problems/FLOW006
try:
    for i in range(int(input())):
        n=int(input())
        r=0
        while n:
            r, n = r + n % 10, n // 10
        print(r)            
except:
    pass
