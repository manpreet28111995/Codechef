#Problem Link: https://www.codechef.com/problems/FLOW005
try:
    notes=[1,2,5,10,50,100]
    for i in range(int(input())):
        num=int(input())
        count=0
        i=len(notes)-1
        while i>=0:
            if num==0:
                break
            if num>=notes[i]:
                count+=1
                num=num-notes[i]	
            else:
                i=i-1
        print(count)
except:
    pass
