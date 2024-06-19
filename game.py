print('''
Welcome to my Rock, Paper, Scissors Game.
Let's begin! Pick your Pick...
\tAuthor : Ka-Chungu Isaac Nyamekye
''')

try:
    k = 1;
    while k == 1:
        print('\t[ Rock, Paper, Scissors ] <=> [R, P, S]\n')
        player1 = str(input('Enter your @PLAYER1 :: ')).upper()
        player2 = str(input('Enter your @PLAYER2 :: ')).upper()
        
        if player1 != player2:
            if (player1 == 'ROCK' and player2 == 'SCISSORS') or (player1 == 'R' and player2 == 'S'):
                print(f'{player1} wins! @PLAYER1 WINS!!!\n')
            elif (player1 == 'SCISSORS' and player2 == 'PAPER') or (player1 == 'S' and player2 == 'P'):
                print(f'{player1} wins! @PLAYER1 WINS!!!\n')
            elif (player1 == 'PAPER' and player2 == 'ROCK') or (player1 == 'P' and player2 == 'R'):
                print(f'{player1} wins! @PLAYER1 WINS!!!\n')
            else:
                print(f'{player2} wins! @PLAYER2 WINS!!!\n')
        else:
            print('We are at a stand off...\nMatching answers.\n')
        cutoff = str(input('Do you want to continue the game? [y/n] ')).lower()
        if cutoff == 'n':
            k = 0
        else:
            k = 1
        
    pass
except Exception as e:
    print('[ Error occurred in runtime ] | [ ', e, ' ]')