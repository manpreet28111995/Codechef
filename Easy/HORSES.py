#Problem Link:https://www.codechef.com/problems/HORSES
try:
    for i in range(int(input())):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        arr=sorted(arr,reverse=True)
        diff=10**20
        for j in arr:
            if arr[j]-arr[j+1]<diff:
                diff=arr[j]-arr[j+1]
        print(diff)
except:
    pass
