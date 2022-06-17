


rows, cols = (9, 9)
board = [["#"]*3 for _ in range(3)]
move = 0
l = [0, 0]
p1_w = [1, 1]
p2_w = [1, 2]


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


def disp_board():
    r1 = board[0][0]+"|"+board[0][1]+"|"+board[0][2]
    r2 = board[1][0]+"|"+board[1][1]+"|"+board[1][2]
    r3 = board[2][0]+"|"+board[2][1]+"|"+board[2][2]
    bd = r1+'\n'+r2+'\n'+r3
    print(bd)


def cb(s):
    w = s.split(",")

    if w[2] == '1':
        board[int(w[0])-1][int(w[1])-1] = 'o'
        # print(board[int(w[0])-1][int(w[1])-1])
    elif w[2] == '2':
        board[int(w[0])-1][int(w[1])-1] = 'x'


def horizontal_win():

    if listToString(board[0]) == 'xxx':
        return p2_w
    elif listToString(board[0]) == 'ooo':
        return p1_w
    if listToString(board[1]) == 'xxx':
        return p2_w
    elif listToString(board[2]) == 'ooo':
        return p1_w
    if listToString(board[2]) == 'xxx':
        return p2_w
    elif listToString(board[2]) == 'ooo':
        return p1_w
    else:
        return l


def vertical_win():
    s1 = board[0][0]+board[1][0]+board[2][0]
    s2 = board[0][1]+board[1][1]+board[2][1]
    s3 = board[0][2]+board[1][2]+board[2][2]
    if s1 == 'xxx':
        return p2_w
    elif s1 == 'ooo':
        return p1_w
    if s2 == 'xxx':
        return p2_w
    elif s2 == 'ooo':
        return p1_w
    if s3 == 'xxx':
        return p2_w
    elif s3 == 'ooo':
        return p1_w
    else:
        return l


def diag_win():
    s1 = board[0][0]+board[1][1]+board[2][2]
    s2 = board[0][2]+board[1][1]+board[2][0]
    if s1 == 'xxx':
        return p2_w
    elif s1 == 'ooo':
        return p1_w
    if s2 == 'xxx':
        return p2_w
    elif s2 == 'ooo':
        return p1_w
    else:
        return l


def check_winner():
    a = horizontal_win()
    b = vertical_win()
    c = diag_win()
    if a[0] != 0:
        return a
    elif b[0] != 0:
        return b
    elif c[0] != 0:
        return c
    else:
        return l


def print_winner():
    s = "P"+str(k[1])+" Wins!!!"
    print(s)


k = []
while(move < 9):
    if move % 2 == 0:
        i1 = input("Move P1: ")
        i1 += ',1'
        cb(i1)
    else:
        i2 = input("Move P2: ")
        i2 += ',2'
        cb(i2)
    disp_board()
    m = check_winner()
    print(m)
    if m[0] == 1:
        k = m
        break
    elif move == 9:
        print("Game Tied!!!")
        break
    move += 1
    # print(move)
if k[0] == 1:
    print_winner()
