# TEST! DON'T SUBMIT THIS VERSION!
# RPN Calculator using Python 

import os                                   # Per TA we are to use this method to handle files

class Stack:                                # CLASS: defines functions for stack operations
  def __init__(stack):                      # Constructor
    stack.items = []
  def stackLen(stack):                      # Gives size of stack (used to find top)
        return len(stack.items)
  def push(stack, token):                   # Push to stack
    stack.items.append(token)
  def pop(stack):                           # Pop from stack
    return  stack.items.pop()

############################################ Assignment 2 ##########################################
def processRPN(stack, token):         # FUNCTION: Evaluates #'s & performs operations
  if(token.isdigit() == True):            # When you find a # add it to stack
    stack.push(token)                 
  if(token == '+'):                       # Perform operation on last 2 #'s on stack & pop
    numb1 = int(stack.pop())                 
    numb2 = int(stack.pop())              # Push result onto stack (same process for all ops.)
    stack.push(numb2 + numb1)       
  if(token == '-'):
    numb1 = int(stack.pop())           
    numb2 = int(stack.pop())
    stack.push(numb2 - numb1)       # NOTE: When - you must perform #2-#1
  if(token == '*'):             
    numb1 = int(stack.pop())                     
    numb2 = int(stack.pop())
    stack.push(numb2 * numb1)       # NOTE: When / you must perform #2/#1
  if(token == '/'):
    numb1 = int(stack.pop())                     
    numb2 = int(stack.pop())
    stack.push(numb2 / numb1)

#path = os.getcwd()
#filepath = os.path.join(path, "input_RPN.txt")
#os.close(fd)
#print(filepath)

with open(os.path.join(os.getcwd(), "input_RPN.txt"), 'r') as file:    # Open file and save data
  content = file.read()
data = content.split('\n')                  # Parse data into lines at every new line char
for line in data:                           # Loop through the parsed line
  elements = line.split(' ')              # Parse the line into tokens at every space char
  stack = Stack()
  for token in elements:                  # Loop through the parsed tokens
    processRPN(stack, token)        # Call function to process token & stack
  result = stack.pop()
  print result
print '\nExtra Credit\n'



  
