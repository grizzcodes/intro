import random,sys,os,math   # import then name of the module


# for i in range(1,11):
#     print(i)
    
num = 0
while (num <= 20):
    print(num)
    num = num +1

# sys.exit()


for i in range(5):
    print(random.randint(1,10)) #using randint function to get 5 random numbers
    # 6, 3, 5, 10, 1
    
# sys.exit()


secretNumber = random.randint(1,10) #assign a random secret variable
print("hmm I'm thinking of a number rn")

#Ask the player to guess 6 times
for guessesTaken in range(1,7): # looks at how many guesses were taken between
    print('Take a guess my dear.')
    guess = float(input())  # the input gets stored in memory as box named guess
    
    if guess < secretNumber:    #checks in memo
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break #correct guess 
    #FOR loop indent takes all the above in its iteration

if guess == secretNumber:
    print('Jackpot')
    print('The secret number was indeed ' + str(secretNumber))
else:
    print('Nope, the number I was thinking about was ' + str(secretNumber))
    
    
    # RockPaper Scissor Game
    

