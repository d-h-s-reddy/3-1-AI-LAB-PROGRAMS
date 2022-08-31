print("Missionaries and the cannibals program")
lsms=3
lsca=3
rims=0
rica=0
k=0
'''Now calculate how many truns can a body will move from one bank to another with the following constraints
   1)fisrtly the boat should carry less than or equal to 2 members per each trip
   2)the missionaries should be greater than the cannibals
   3)the boat should no move empty'''
print("enter no of turns required to move the 3 missionaries and 3 cannibals from left to right")
try:
    while(True):
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
        lsms-=um
        lsca-=uc
        rims+=um
        rica+=uc
        for i in range(0,lsms):
            print("m ",end="")
        for i in range(0,lsca):
            print("c ",end="")
        print(".......",end="")
        for i in range(0,rims):
            print("m ",end="")
        for i in range(0,rica):
            print("c ",end="")
        ''' Now increment the k value which is mainly used to check for how many times a boat traveled'''
        k+=1
        
        if(((lsca==3)and (0 < lsms <= 2)) or((lsca==2)and(lsms==1)) or((rica==3)and (0 <rims<=2))or((rica==2)and(rims==1))):
            print("the cannibals eat the massinaries")
            break
        
        print("\n")
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
        lsms+=um
        lsca+=uc
        rims-=um
        rica-=uc
        for i in range(0,rims):
            print("m ",end="")
        for i in range(0,rica):
            print("c ",end="")
        print(".......",end="")
        for i in range(0,lsms):
            print("m ",end="")
        for i in range(0,lsca):
            print("c ",end="")
        print("\n")
        k=+1
            
        if(((lsca==3)and (0 <lsms <= 2)) or((lsca==2)and(lsms==1)) or((rica==3)and (0 <rims<=2))or((rica==2)and(rims==1))):
            print("the cannibals eat the massinaries")
            break
        if((rims+rica)==6 and(lsca+lsms)==0):
            print("The missinaries and canibals problem has been solved")
            break
except EOFError as e:
    print("\nInvalid input please retry !!")