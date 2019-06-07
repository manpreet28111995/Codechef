#Problem Link:https://www.codechef.com/problems/COINS
def calculate(a):
    if a == 0: 
        arr[a] = a
    if a not in arr.keys() :
        arr[a] = max (a, calculate(a//2) +calculate(a//3) +calculate(a//4))
    return arr[a]

while (True):
    try:
        a = int(input())
        arr = {}
        calculate(a)
        print(arr[a])
    except:
        break
