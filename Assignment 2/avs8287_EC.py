# Anena Sims
# 10/18/2017
# 1001138287
# Code compiled and executed in Mac terminal using python ./avs8287_EC.py
# Assignment 2: RPN Calculator using Python

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
def processRPN(stack, token):			        # FUNCTION: Evaluates #'s & performs operations
  if(token.isdigit() == True):         		# When you find a # add it to stack
    stack.push(token)                 
  if(token == '+'):                     	# Perform operation on last 2 #'s on stack & pop
    numb1 = float(stack.pop())                 
    numb2 = float(stack.pop())           		# Push result onto stack (same process for all ops.)
    stack.push(numb2 + numb1)				
  if(token == '-'):
    numb1 = float(stack.pop())           
    numb2 = float(stack.pop())
    stack.push(numb2 - numb1)				      # NOTE: When - you perform #2-#1
  if(token == '*'):							
    numb1 = float(stack.pop())                     
    numb2 = float(stack.pop())
    stack.push(numb2 * numb1)				      # NOTE: When / you perform #2/#1
  if(token == '/'):
    numb1 = float(stack.pop())                     
    numb2 = float(stack.pop())
    stack.push(numb2 / numb1)

# path.join()-combines getcwd() & file name, getcwd()-confirms path is current working dir
with open(os.path.join(os.getcwd(), "input_RPN.txt"), 'r') as file:   
  content = file.read()
data = content.split('\n')                 	# Parse data into lines at every new line char
for line in data:                          	# Loop through the parsed line
  elements = line.split(' ')              	# Parse the line into tokens at every space char
  stack = Stack()
  for token in elements:                  	# Loop through the parsed tokens
    processRPN(stack, token)			         	# Call function to process token & stack
  result = int(stack.pop())
  print result

############################################### BONUS ##############################################
def processOperator(rpn, stack, token):             
  if((stack.stackLen() - 1) < 0):                   # Add first op of exp. to stack
    stack.push(token)
    return
  else:
    top = stack.items[stack.stackLen() - 1]         
    if(top == '('):                                 # All ops have higher precedence than (
      stack.push(token)
      return
    if((token == '*' or token == '/') and (top == '+' or top == '-')): 
      stack.push(token)                  # * & / have higher precedence 
      return
    else:                                
      rpn.append(top)                    # Pop the top op & app it to rpn result
      pop = stack.pop()
      processOperator(rpn, stack, token) # Recurse until stack is empty or op is pushed

def processStack(rpn, stack, top):       
  if(top == '('):                        # Found ( return
    return
  if(stack.stackLen() == 0):             # Last token of stack, pop and app to rpn exp.
    rpn.append(top)
    return
  else:                                  # Recurse until top of stack = ( or stack empty
    rpn.append(top)
    top = stack.pop()
    processStack(rpn, stack, top)

with open(os.path.join(os.getcwd(), "input_RPN_EC.txt"), 'r') as file:    # Open file and save data
  content = file.read()
data = content.split('\n')               # Parse data into lines at every new line char
for line in data:                        
  elements = line.split(' ')             # Parse the line into tokens at every space char
  rpn = []
  stack = Stack()
  for token in elements:                 
    if(token.isdigit() == True):         # Add # to rpn exp.
      rpn.append(token)
    if(token == '('):                    # Add ( to the stack
      stack.push(token)
    if(token == ')'):                    
      top = stack.pop()
      processStack(rpn, stack, top)      # Call function to pop stack till ( on top
    if(token == '+' or token == '-' or token == "*" or token == '/'):   
      processOperator(rpn, stack, token) 
  if(stack.stackLen > 0):                # At end of line add remaining stack to rpn exp.
    top = stack.pop()
    processStack(rpn, stack, top)
  stack = Stack()
  for value in rpn:                      # Print the rpn exp.
    print value,
    processRPN(stack, value)			       # Call function to process rpn token & stack
  print ""
  result = int(stack.pop())
  print result

