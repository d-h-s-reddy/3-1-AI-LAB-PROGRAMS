print("The water jug problem")
jug1=int(input("Enter the size of the jug1:"))
jug2=int(input("Enter the size of the jug2:"))
jt1=int(input("Enter the target for the jug1:"))
jt2=int(input("Enter the target for the jug2:"))
X,Y=0,0
counter=0
print('''Select any one of the production rules:
                 1)X<jug1->(jug1,Y)
                 2)X>0->(0,Y)
                 3)(Y<jug2->(X,jug2)
                 4)(Y>0->(X,0)
                 5)(X+Y<=jug1 and Y>0)->(X+Y,0)
                 6)(X+Y<=Jug2) and X>0 ->(0,X+Y)
                 7)(X+Y>=jug1 and Y>0 -> (jug1,Y-(Jug1-X))
                 8)(X+Y>=jug2 and X>0 -> (X-(jug2-Y),jug2)''')
while(True):
    print(X,Y)
    if(jt1==X and jt2==Y):
        print("The jugs has been filled upto the target")
        break
    else:
        counter=counter+1
        choice=int(input("Enter the production rule:"))
        if(choice==1):
            X=jug1
        elif(choice==2):
            X=0
        elif(choice==3):
            Y=jug2
        elif(choice==4):
            Y=0
        elif(choice==5):
            X=X+Y
            Y=0
        elif(choice==6):
            X=0
            Y=X+Y
        elif(choice==7):
            Y=Y-(jug1-X)
            X=jug1
        elif(choice==8):
            X=X-(jug2-Y)
            Y=jug2
print("No of truns requires are:",counter)