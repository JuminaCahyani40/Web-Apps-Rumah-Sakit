import random
import copy

board = [['[ ]' for _ in range(7)] for _ in range(7)]
row = ['A :', 'B :', 'C :', 'D :', 'E :', 'F :', 'G :']
col = '    1  2  3  4  5  6  7'
skor=[0,0]

def printboard(board):
    print("\n"*5)
    print(col)
    for r,i in enumerate(board):
        print(row[r],end='')
        for j in i:
            print(j,end="")
        print()

def checkend(board):
    for i in board:
        for j in i:
            if j == '[ ]':
                return False
    else :
        return True

def checkpoin(x,y,s,p,b):
    score = 0
    if s=='[S]':
        if _kanan(x,y,b):
            skor[p]+=1
            score+=1
        if _kananbawah(x,y,b):
            skor[p]+=1
            score+=1
        if _bawah(x,y,b):
            skor[p]+=1
            score+=1
        if _kiriatas(x,y,b):
            skor[p]+=1
            score+=1
        if _atas(x,y,b):
            skor[p]+=1
            score+=1
        if _kananatas(x,y,b):
            skor[p]+=1
            score+=1
        if _kiri(x,y,b):
            skor[p]+=1
            score+=1
        if _kiribawah(x,y,b):
            skor[p]+=1
            score+=1
    if s=='[O]':
        if _horizontal(x,y,b):
            skor[p]+=1
            score+=1
        if _vertikal(x,y,b):
            skor[p]+=1
            score+=1
        if _diagonal1(x,y,b):
            skor[p]+=1
            score+=1
        if _diagonal2(x,y,b):
            skor[p]+=1
            score+=1
    return score

def _kanan(x,y,bo):
    if y+1<7 and bo[x][y+1] == '[O]' and y+2<7 and bo[x][y+2] =='[S]' :
        return True
    return False

def _kiri(x,y,bo):
    if y-1>-1 and bo[x][y-1] == '[O]' and y-2>-1 and bo[x][y-2] =='[S]' :
        return True
    return False

def _atas(x,y,bo):
    if x-1>-1 and bo[x-1][y] == '[O]' and x-2>-1 and bo[x-2][y] =='[S]' :
        return True
    return False

def _bawah(x,y,bo):
    if x+1<7 and bo[x+1][y] == '[O]' and x+2<7 and bo[x+2][y] =='[S]' :
        return True
    return False

def _kiribawah(x,y,bo):
    if x+1<7 and y-1>-1 and bo[x+1][y-1] == '[O]' and x+2<7 and y-2>-1 and bo[x+2][y-2] =='[S]' :
        return True
    return False

def _kiriatas(x,y,bo):
    if x-1>-1 and y-1>-1 and bo[x-1][y-1] == '[O]' and x-2>-1 and y-2>-1 and bo[x-2][y-2] =='[S]' :
        return True
    return False

def _kananbawah(x,y,bo):
    if x+1<7 and y+1<7 and bo[x+1][y+1] == '[O]' and x+2<7 and y+2<7 and bo[x+2][y+2] =='[S]' :
        return True
    return False

def _kananatas(x,y,bo):
    if x-1>-1 and y+1<7 and bo[x-1][y+1] == '[O]' and x-2>-1 and y+2<7 and bo[x-2][y+2] =='[S]' :
        return True
    return False
def _horizontal(x,y,bo):
    if y+1<7 and bo[x][y+1] == '[S]' and y-1>-1 and bo[x][y-1]=='[S]':
        return True
    return False

def _vertikal(x,y,bo):
    if x+1<7 and bo[x+1][y] == '[S]' and x-1>-1 and bo[x-1][y]=='[S]':
        return True
    return False

def _diagonal1(x,y,bo):
    if x+1<7 and y-1>-1 and bo[x+1][y-1] == '[S]' and x-1>-1 and y+1<7 and bo[x-1][y+1]=='[S]':
        return True
    return False

def _diagonal2(x,y,bo):
    if x+1<7 and y+1<7 and bo[x+1][y+1] == '[S]' and x-1>-1 and y-1>-1 and bo[x-1][y-1]=='[S]':
        return True
    return False

def player():
    try :
        printboard(board)
        print('SKOR PLAYER :', skor[0])
        print('SKOR COMPUTER :', skor[1])
        print("\nplayer 1 main")
        print('Masukkan ex: A1 S')
        s = input('->').upper()
        x,y,s = translate(s)
        s = f'[{s}]'
        cekinput = True if board[x][y]=='[ ]' else False
        if cekinput:
            board[x][y] = s
        else:
            print('Slot sudah ada')
            player()
        lagi = checkpoin(x,y,s,0,board)
        checkend(board)
        if lagi >0:
            player()
    except:
        player()

def translate(s):
    baris = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    l=list(s)
    y = [i+1 for i,a in enumerate(baris) if l[0]==a]
    return (int(y[0])-1, int(l[1])-1, l[3])

def getPoinmove(bo):
    temp=[]
    for x in range(7):
        for y in range(7):
            if board[x][y] =='[ ]':
                if _kanan(x,y,bo) or _kiri(x,y,bo) or _bawah(x,y,bo) or _atas(x,y,bo) or\
                   _kananbawah(x,y,bo) or _kananatas(x,y,bo) or _kiribawah(x,y,bo) or _kiriatas(x,y,board):
                    temp.append([x,y,'[S]'])
                if _horizontal(x,y,bo) or _vertikal(x,y,bo) or _diagonal1(x,y,bo) or _diagonal2(x,y,board):
                    temp.append([x,y,'[O]'])
    return temp


def best_result(board):
    if checkend(board):
        return (0,0,0)
    getPoin = getPoinmove(board)
    if getPoin != []:
        return getPoin[0]
    loss=[]
    all_candidate = [[x,y,s] for x in range(7) for y in range(7) for s in ('[S]', '[O]') if board[x][y] == '[ ]']
    random.shuffle(all_candidate)
    for candidate_move in all_candidate:
        x,y,s = candidate_move
        cboard = copy.deepcopy(board)
        cboard[x][y] = s
        result = getPoinmove(cboard)
        if len(result)==0:
            return (x,y,s)
        else:
            loss.append([x,y,s])
    return random.choice(loss)

def bot():
    printboard(board)
    print('SKOR PLAYER :', skor[0])
    print('SKOR COMPUTER :', skor[1])
    x,y,s = best_result(board)
    if x == y and y == s:
        return
    board[x][y] = s
    lagi = checkpoin(x,y,s,1,board)
    checkend(board)
    if lagi >0:
        bot()

def main():
    print('welcome in SOS game')
    print("Game Start")
    print("Kamu main pertama")
    while not checkend(board):
        player()
        bot()
        
    if skor[0] == skor[1]:
        print("Game kali ini berakhir DRAW")
    else:
        print("Pemenang kali ini adalah")
        win = "PLAYER" if skor[0]>skor[1] else "COMPUTER"
        print(f"----------{win}------------")
        print('dengan poin sebanyak', skor[1])
        
main()
