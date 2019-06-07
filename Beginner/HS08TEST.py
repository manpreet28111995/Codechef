#Problem Link: https://www.codechef.com/problems/HS08TEST
try:
    amt,bal=input().split()
    amt=float(amt)
    bal=float(bal)
    if(amt%5==0) and (bal>=amt+0.5):
        print(bal-(amt+0.5))
    else:
        print(bal)
except:
    pass
