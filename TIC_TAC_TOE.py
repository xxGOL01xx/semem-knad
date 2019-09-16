import time
board = [' ', ' ', ' ', ' ', ' ', ' ' , ' ', ' ', ' ']
play_1_wins = 0
play_2_wins = 0
def check(out, p_1_w, p_2_w):
    if out == 1:
        print('Player 1 Wins.')
        p_1_w += 1
    elif out == 2:
        print('Player 2 Wins.')
        p_2_w += 1
    else:
        print("It's a tie.")
    print()
    print('Player 1 has won', p_1_w, 'times.')
    print('Player 2 has won', p_2_w, 'times.')
    if input('Do you want to play again (y/n)? ').lower() == 'y':
        print()
        for i in range(8, -1, -1):
            board.pop(i)
            board.append(' ')
        again(p_1_w, p_2_w)
    else:
        print('\n\n\t\t\t\t Game Over \n')
        print('\t\t\t Leaderboard  | \tWins')
        print('\t\t\t -------------+------')
        if p_1_w > p_2_w:
            print('\t\t\t 1. Player 1  |  ', p_1_w)
            print('\t\t\t 2. Player 2  |  ', p_2_w)
        elif p_2_w > p_1_w:
            print('\t\t\t 1. Player 2  |  ', p_2_w)
            print('\t\t\t 2. Player 1  |  ', p_1_w)
        return 0, 0
def print_board():
    print('(1) | (2) |(3)')
    print(' ' + board[0] + '  |  ' + board[1] + '  | ' + board[2])
    print('--------------')
    print('(4) | (5) |(6)')
    print(' ' + board[3] + '  |  ' + board[4] + '  | ' + board[5])
    print('--------------')
    print('(7) | (8) |(9)')
    print(' ' + board[6] + '  |  ' + board[7] + '  | ' + board[8])
def again(p_1_w, p_2_w):
    print_board()
    for i in range(1, 10):
        if i%2 != 0:
            turn = 'p_1'
        else:
            turn = 'p_2'
        out = play(turn)
        if out != 0:
            break
    p_1_w, p_2_w = check(out, p_1_w, p_2_w)
        
def p_1():
    access = int(input('P1, Pick an empty square: '))-1
    if board[access] != ' ':
        print('I said an empty square.')
        time.sleep(1)
        print()
        p_1()
    else:
        board[access] = 'X'
        print()
        print_board()
def p_2():
    access = int(input('P2, Pick an empty square: '))-1
    if board[access] != ' ':
        print('I said an empty square.')
        time.sleep(1)
        print()
        p_2()
    else:
        board[access] = 'O'
        print()
        print_board()
        
def play(turn):
    win = 0
    for i in range(0, 8, 3):
        if board[i] == board[i+1] and board[i] == board[i+2]:
            if board[i] == 'X':
                win = 1
                break
            elif board[i] == 'O':
                win = 2
                break
    for i in range(3):
        if board[i] == board[i+3] and board[i] == board[i+6]:
            if board[i] == 'X':
                win = 1
                break
            elif board[i] == 'O':
                win = 2
                break
    if board[0] == board[4] and board[0] == board[8]:
        if board[0] == 'X':
            win = 1
        elif board[0] == 'O':
            win = 2
    elif board[2] == board[4] and board[2] == board[6]:
        if board[2] == 'X':
            win = 1
        elif board[2] == 'O':
            win = 2
    if win != 0:
        return win
    if turn == 'p_1':
        p_1()
    else:
        p_2()     
    return win
again(play_1_wins, play_2_wins)