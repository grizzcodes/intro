import sys, random

print('ROCK', 'PAPER', 'SCISSORS')

#this will keep track of the #s of wins,losses, and ties
#player's record
wins = 0
losses = 0
ties = 0

while True: # this is the Game Loop #always shows up 
    print('%s wins, %s losses, %s ties' % (wins,losses, ties)) #keeps track of records
    #this keeps track of records at ALL time.
    
    while True: # The player input loop. -> LOOP INSIDE OF A LOOP
        print('Enter your move: (r)ock, (p)aper, (s)cissor or (q)uit')
        playerMove = input()    #  player's input gets stored in playerMove
        if playerMove == 'q': # if the player types 'q'
            sys.exit() #quits the program 
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's': # if the player types this
            break # Gets the input player out of the loop for next instructions
        print('Type one of r, p, s, or q') #this gets called if player's input != r,p,s or q

    #Display the player's print() if he successfully typed r,p or s:
    if playerMove == 'r':           #if player's input is r, THEN print the statement
        print('ROCK versus...')     #skips over the rest 
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSOR versus ...')
    
    #Display the computer's choice
    randomNumber = random.randint(1,3)  #random number pick functio
    if randomNumber == 1:   #if the randomNumber stored = 1
        computerMove = 'r'      # assign it to computer move 'r'
        print('ROCK')
    elif randomNumber == 2:   #if randomNumber = 2
        computerMove = 'p'      # assign it to 'p'
        print('PAPER')
    elif randomNumber == 3:   # if its 3
        computerMove = 's'      #assign it to 's'
        print('SCISSOR')

    #Display the results
    if playerMove == computerMove:  # if player's pick = computer
        print('It is a TIE!')       # print this
        ties = ties + 1                     # adds to state variable
    elif playerMove == 'r' and computerMove == 's':    #if player pickrs 'r', and computer
        print('Player Wins!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r': 
        print('Player Wins!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('Player Wins!')
        wins = wins + 1
    else:
        print('Player Loses')
        losses = losses + 1
        
    if wins == 3:
        print(" VICTORY ! ") #at 3 wins, exit the loop with message 'VICTORY'
        break                   
        
    elif losses == 3:
        print(" GAME OVER :(") #at 3 losses, exit the loop with message 'GAME OVER'
        break
        