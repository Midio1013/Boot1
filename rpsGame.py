import random, sys

print('Rock,Paper,Scissors')

wins = 0
los = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, los, ties))
    while True:
        print('Enter your move:(r)ock (s)cissors (p)aper or (q)uit')
        pm = input(">")
        if pm == 'q':
            print('\ndone.')
        if pm == 'r' or pm == 's' or pm == 'p':
            break
        print('Type r,s,p or q.')

    if pm == 'r':
        print('Rock versus...')
    elif pm == 's':
        print('Scissors versus...')
    elif pm == 'p':
        print('Paper versus...')

    rn = random.randint(1, 3)
    if rn == 1:
        print('Rock')
        cm = 'r'
    elif rn == 2:
        print('Scissors')
        cm = 's'
    elif rn == 3:
        print('Paper')
        cm = 'p'

    if pm == cm:
        print('It is a tie')
