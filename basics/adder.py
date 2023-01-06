def adding(x,y):
    sum = x + y
    print("The answer is: ", sum)
    return sum

def count(name):
	count = len(name)
	print(count)
 
def substract(a,b):
    result = a - b
    print(f'{a} - {b} is: {result}')
    return result

def equations(number):
    for i in range(1,20,2):
        print(number, i * 2)
