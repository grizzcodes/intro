import random	# import the random module to get the .randint function
import pprint # module that makes a pretty print

def getAnswer(answerNumber):	#defines the getAnswer() function with given variable answerNumber (not a parameter yet)
	if answerNumber == 1:			# when random_value argument is passed, answer_Number = parameter
		return 'terrible'
	elif answerNumber == 2:
		return 'not bad'
	elif answerNumber == 3:
			return 'moderate'
	elif answerNumber == 4:
			return 'good'
	elif answerNumber == 5:
			return 'amazing'
 
random_value = random.randint(1,5) #  random_value is assigned the .randint function the variable (which picks a random number)
random_answer = getAnswer(random_value)	# getAnswer() gets called, and passes argument random_value to its newly defined function
# random_answer variable stores the defined function getAnswer
print(random_answer) #print out the random_answer variable containing the getAnswer function that passes argument random_value to the function

# OR

print(getAnswer(random.randint(1,5))) # shorten version of the last three lines

print("")

#  --------------------------------

def hello(*antyhing):
	print('Hi' + str(antyhing))
 
hello("momo", "alec")

print("")

#  --------------------------------

def a():
	print('a() starts')
	b()
	d()
	print('a() returns')

def b():
	print('b() starts')
	c()
	print('b() returns')

def c():
	print('c() starts')
	print('c() returns')

def d():
	print('d() starts')	
	print('d() returns')

a()

print("")

#  --------------------------------

def groceries(): #runs down to this function
	egg = 99 # egg set to 99
	bacon() # new local scope is created, and set to 
	print(egg)	# this gets printed after bacon() returns

def bacon():
	ham = 100 # new ham variable set to 100
	egg = 0 	
	print(egg)	#prints out first before returning bacon()
 
groceries() #this function gets called

# MULTIPLE LOCAL SCOPES can be created at the same time.

#  --------------------------------

def spam():
	global eggs
	eggs = 'spam'
 
eggs = 'global'
spam()
print(eggs)

print("")

# --------------------------------

def print_info(name, age, gender):
	print('Name: ', name)
	print('Age: ', age)
	print('Gender: ', gender)
	
	return

n = 'Alec'
a = 23
g = 'male'

print_info(n,a,g)

print("")

def foo(name, department, salary = 1500):
	print(' Name:', name)
	print('Salary: ', salary)
	print("Department: ", department)

name = 'John'
department = 'IT'

foo(department, name)

print("")

#  --------------------------------

def outer_func(num):	# outside function with paramete num
	def inner_func(num):  # nested within out_func (isolated function)
		return num + 1      # cannot be accessed outside the outer_func scope
	num_1 = inner_func(num)	# inner_func stored in num_1
	print(num, num_1)	# prints out the list of the nym 
# inner_func (4) => can't be called, because not defined 
outer_func (4)

def spam(divideBy):
	try:
		return 20 / divideBy
	except ZeroDivisionError:
		print('Damn you asked for 0')

print(spam(2))
print(spam(0))
print(spam(4))
print(spam(3))

print("")

# --------------------------------

week = { 1: "monday", # define state variables of week as dictionairy
    	2: "tuesday",
        3: "wednesday",
        4: "thursday",
        5: "friday",
        6: "saturday",
        7: "sunday"
    }

def daysWeek(x):			#define the days of the Week 
    if 1 < x < 6:		#input of number between -\0-6
        print(week[x]) #print state variable, and its list[] value 
    else:
        print("Error")
        
daysWeek(5)

print("x")

print("")

#Prompt: function name collatz(number) with number parameter
	#if number is even, print the number
	# if number is odd, print the number

try:	#detecting whether the type 

	def collatz(number):
		if (int(number) % 2 == 0):
			print(int(number))
		elif (int(number) % 2 == 1):
			print(int(number) * 2 + 1)
   
	number = input()
	collatz(number)
 

except ValueError:	# raise this error to make sure the right value is used
    print("Error: right the type")


word = 'alec'


print(hash('sha256'))
print("")

	
data = [] # empty array

for x in range(8): # for loop of x values in a range of 0-4
	data.append((x, {0: 0, 1: 1})) # appends data in 0-7 columns, each with f

print(pprint.pformat(data, width = 25))
print("")
print(pprint.pformat(data))