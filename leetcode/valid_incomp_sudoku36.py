def isValidSudoku(board) -> bool:
    for i in range(9):
        for j in range(9):
            if(board[i][j].isnumeric()):
                board[i][j]=int(board[i][j])
            else:
                board[i][j]=0
    for i in range(9):
        for j in range(9):
            if(board[i][j]!=0):
                if(board[i].count(board[i][j])!=1):return False
    
    t=list(zip(*board))
    for i in range(9):
        for j in range(9):
            if(t[i][j]!=0):
                if(t[i].count(t[i][j])!=1):return False
    t=[]
    for i in (3,6,9):
        t3=list(zip(*board[i-3:i]))
        for j in (3,6,9):
            t2=[]
            for k in range(j-3,j):
                t2.extend(list(t3[k]))
            t.append(t2)
    for i in range(9):
        for j in range(9):
            if(t[i][j]!=0):
                if(t[i].count(t[i][j])!=1):return False
    return True



print(isValidSudoku(
[["5", "3", ".", ".", "7", ".", ".", ".", "."], 
["6", ".", ".", "1", "9", "5", ".", ".", "."], 
[".", "9", "8", ".", ".", ".", ".", "6", "."],
["8", ".", ".", ".", "6", ".", ".", ".", "3"],
["4", ".", ".", "8", ".", "3", ".", ".", "1"], 
["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
[".", "6", ".", ".", ".", ".", "2", "8", "."], 
[".", ".", ".", "4", "1", "9", ".", ".", "5"], 
[".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
