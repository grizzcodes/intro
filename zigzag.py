
import time, sys

# 2 variables we are using: 

indent = 0 #How many indented spaces | keeps track of how many indents
indentIncreasing = True #wether indentation is increasing contains a boolean value to see if indent is increasing or decreasing

try:
    while True: #this is the main LOOP
        print('' *indent, end = '') #
        print("********")
        time.sleep(0.1) # Pause for 0.1 second
        
        if indentIncreasing:
            # increase number of spaces
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False
        
        else:
            # Decrease the number of spaces
            indent = indent - 1
            if indent == 0: 
                    # change the direction:
                indentIncreasing = True           
except KeyboardInterrupt:

    sys.exit() 