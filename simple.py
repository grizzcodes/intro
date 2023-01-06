import sys


for x in ['0','1','2','3','4','5']: # for the value x in the array:
	if (int(x) % 2 == 0):   # if the integer x's remainder = 0
		print(x)    # print it

## make sure to define the argument passed (int(x)) for x

for x in [1,2]:
    print(x)
    for j in range(0,2):
        print(j)

print("Hey man! was good")
print(" I'm Boochie, and am " + str(int(44)) + " years old")    #including in the string text an int variable

print(" Wbu? Write your name down")

name = input()  #requires user to put their input, will be stored as an input

print("Nice to meet u " + name) 
print("you have " + str(len(name)) + " letters in your name") #if you put str(int)-> will get error for trying to convert a letter to int
# sys.exit()

while True:
    age = input("How old are you?") 
    if age.isdigit():  # isdigit() method for evaluating if input is str/int
        print("dope ! you'll be " + str(int(age) + 1) + " in about a year or so right?") 
        year = 2022 - int(age)
        print ('You were also probably born in ' + str(int(year)) + ' !') 
        sys.exit()
        
    else:
        print("thefak is this gibberish, try again with number")
        
  
  







# year = input()

# age = 2022 - int(year)

# if age <= 21:
    
#     print("Sheesh, you still young fool")

# elif age == 22:
#     print("Ayt you startin to get old, do some shit")

# elif age >= 23 and age <= 79:
#     print("Bro what you doinnn, grind g")

# elif age > 80 and age < 110:
#     print("brah you about to die soon")

# else:
#     print("Make sure you have the year written in 4 numbers.. ie: 1999")
    