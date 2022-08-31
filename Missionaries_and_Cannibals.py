print("Missionaries and the cannibals program")
lsms=3
lsca=3
rims=0
rica=0
condition=True
k=0
def calculation(um,uc,n):
    global lsms,lsca,rims,rica,k
    if(n==1):
        lsms-=um
        lsca-=uc
        rims+=um
        rica+=uc
        k+=1
    else:
        lsms+=um
        lsca+=uc
        rims-=um
        rica-=uc
        k+=1
def printing():
    for i in range(0,lsms):
        print("m ",end="")
    for i in range(0,lsca):
        print("c ",end="")
    print(".......",end="")
    for i in range(0,rims):
        print("m ",end="")
    for i in range(0,rica):
        print("c ",end="")
    print("\n")
def left_to_right():
    print("boat travel from left to right")
    while(True):
        um=int(input("enter no of missionaries to travel on boat : "))
        uc=int(input("enter no of cannibals to travel on boat :"))
        if((um==0) and (uc==0)):
            print("it is not possible")
            print("reenter the user missionaries and cannibals")
        elif(((um+uc)<=2) and (lsms-um)>=0 and (lsca-uc)>=0):
            break
        else:
            print("entered the input wrongly")
    calculation(um,uc,1)
    printing()
def right_to_left():
    print("the boat travelling from right to left")    
    while(True):
        um=int(input("enter no of missionaries to travel on boat :"))
        uc=int(input("enter no of cannibals to travel on boat :"))
        if((um==0) and (uc==0)):
            print("it is not possible")
        elif((um+uc)<=2 and (rims-um)>=0 and (rica-uc)>=0):
            break
        else:
            print("this is not possible")
    calculation(um,uc,2)
    printing()
def conditioncheck():
    if(((lsca==3)and (0 < lsms <= 2)) or ((lsca==2)and(lsms==1)) or((rica==3)and (0 <rims<=2))or((rica==2)and(rims==1))):
        print("the cannibals eat the massinaries")
        return False
    if((rims+rica)==6 and (lsca+lsms)==0):
        print("The missinaries and canibals problem has been solved")
        print("no of turns required are",k)
        return False
while(True):
    left_to_right()
    condition=conditioncheck()
    if(condition==False):
        break
    right_to_left()
    condition=conditioncheck()
    if(condition==False):
        break
    
    
    
        
