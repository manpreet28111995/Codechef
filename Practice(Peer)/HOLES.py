#Problem Link: https://www.codechef.com/problems/HOLES
for i in range(int(input())):
    string=input()
    ctr=0
    for a in string:
        if (a=='A' or a=='D' or a=='O' or a=='P' or a=='R'or a=='Q'):
            ctr=ctr+1
        elif (a=='B'):
            ctr=ctr+2
        else:
            ctr=ctr+0
    print(ctr)
