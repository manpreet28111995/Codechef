#Problem Link : https://www.codechef.com/problems/FLOW010/
try:
    for i in range(int(input())):
        a=input()
        if(a=='B' or a=='b'):
            print('BattleShip')
        elif(a=='C' or a=='c'):
            print('Cruiser')
        elif(a=='D' or a=='d'):
            print('Destroyer')
        elif(a=='F' or a=='f'):
            print('Frigate')            
except:
    pass
