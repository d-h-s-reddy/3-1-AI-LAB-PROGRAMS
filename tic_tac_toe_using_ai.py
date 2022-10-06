board={}
for i in range(1,10):
    board[i]=' '

def printboard(board):
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("-----")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-----")
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("\n")

printboard(board)

#now we need to check if any space is free or not
def isspacefree(position):
    if(board[position]==' '):
        return True
    else:
        return False

def checkforwin():
    if(board[1]==board[2] and board[1]==board[3] and board[1]!=' '):
        return True
    elif(board[1]==board[4] and board[1]==board[7] and board[1]!=' '):
        return True
    elif(board[2]==board[5] and board[2]==board[8] and board[2]!=' '):
        return True
    elif(board[3]==board[6] and board[3]==board[9] and board[3]!=' '):
        return True
    elif(board[4]==board[5] and board[4]==board[6] and board[4]!=' '):
        return True
    elif(board[7]==board[8] and board[7]==board[9] and board[7]!=' '):
        return True
    elif(board[1]==board[5] and board[1]==board[9] and board[1]!=' '):
        return True
    elif(board[7]==board[5] and board[7]==board[3] and board[7]!=' '):
        return True
    else:
        return False

def checkwhichmarkwon(mark):
    if(board[1]==board[2] and board[1]==board[3] and board[1]==mark):
        return True
    elif(board[1]==board[4] and board[1]==board[7] and board[1]==mark):
        return True
    elif(board[2]==board[5] and board[2]==board[8] and board[2]==mark):
        return True
    elif(board[3]==board[6] and board[3]==board[9] and board[3]==mark):
        return True
    elif(board[4]==board[5] and board[4]==board[6] and board[4]==mark):
        return True
    elif(board[7]==board[8] and board[7]==board[9] and board[7]==mark):
        return True
    elif(board[1]==board[5] and board[1]==board[9] and board[1]==mark):
        return True
    elif(board[7]==board[5] and board[7]==board[3] and board[7]==mark):
        return True
    else:
        return False

def checkdraw():
    for key in board.keys():
        if(board[key]==' '):
            return False
    return True
    
#now we enter the element into the board from the user
def insertletter(letter,position):
    if(isspacefree(position)):
        board[position]=letter
        printboard(board)
        
        #now we check for the mach for draw or the winner
        if(checkdraw()):
            print("The mach is Draw")
            exit()
        
        #now check for the win 
        if(checkforwin()):
            if(letter =='x'):
                print("bot wins")
                exit()
            else:
                print("human wins")
                exit()
        return 

    else:
        print("cann't insert the element")
        position=int(input("please re enter the valid position:"))
        insertletter(letter,position)
        return



player='0'
computer='x'
def playermove():
    position=int(input("Enter the position for the player('o'):"))
    insertletter(player, position)
    return

def computermove():
#here we should implement the minimax method which is used to think the bot by its own
    bestscore=-1000
    bestmove=0
    for key in board.keys():
        if(board[key]==' '):
            board[key]=computer
            score=minimax(board,0,False)
            board[key]=' '
            if(score>bestscore):
                bestscore=score
                bestmove=key
    insertletter(computer,bestmove)
    return


def minimax(board,depth,ismaximizing):
    if(checkwhichmarkwon(computer)):
        return 1
    elif(checkwhichmarkwon(player)):
        return -1
    elif(checkdraw()):
        return 0
    
    if(ismaximizing):
        bestscore=-1000
        for key in board.keys():
            if(board[key]==' '):
                board[key]=computer
                score=minimax(board,depth+1,False)
                board[key]=' '
                if(score>bestscore):
                    bestscore=score
        return bestscore
    else:
        bestscore=1000
        for key in board.keys():
            if(board[key]==' '):
                board[key]=computer
                score=minimax(board,depth+1,True)
                board[key]=' '
                if(score<bestscore):
                    bestscore=score
        return bestscore

#now iterate the loop until the win
while not checkforwin():
    computermove()
    playermove()
