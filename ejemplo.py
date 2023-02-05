def plusMinus(arr):
    numpos=0
    numneg=0
    zeros=0
    for i in arr:
        if i>0:
            numpos+=1
        elif i<0:
            numneg+=1
        else:
            zeros+=1
    total=[numpos,numneg,zeros]
    for x in total:
        y=int(x)/(len(arr)+1)
        
        print(y)    
plusMinus([-2,1,2,0,-3])

