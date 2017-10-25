# Anena Sims
# 10/18/2017
# 1001138287
# Code compiled and executed in Mac terminal using python ./avs8287_EC.py
# RPN Calculator using Python

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
def processRPN(stack, token):			    # FUNCTION: Evaluates #'s & performs operations
  if(token.isdigit() == True):         		# When you find a # add it to stack
    stack.push(token)                 
  if(token == '+'):                     	# Perform operation on last 2 #'s on stack & pop
    numb1 = int(stack.pop())                 
    numb2 = int(stack.pop())           		# Push result onto stack (same process for all ops.)
    stack.push(numb2 + numb1)				
  if(token == '-'):
    numb1 = int(stack.pop())           
    numb2 = int(stack.pop())
    stack.push(numb2 - numb1)				# NOTE: When - you must perform #2-#1
  if(token == '*'):							
    numb1 = int(stack.pop())                     
    numb2 = int(stack.pop())
    stack.push(numb2 * numb1)				# NOTE: When / you must perform #2/#1
  if(token == '/'):
    numb1 = int(stack.pop())                     
    numb2 = int(stack.pop())
    stack.push(numb2 / numb1)
  
with open('input_RPN.txt', 'r') as file:    # Open file and save data
  content = file.read()
data = content.split('\n')                 	# Parse data into lines at every new line char
for line in data:                          	# Loop through the parsed line
  elements = line.split(' ')             	# Parse the line into tokens at every space char
  stack = Stack()
  for token in elements:                 	# Loop through the parsed tokens
    processRPN(stack, token)				# Call function to process token & stack
  result = stack.pop()
  print result
print '\nExtra Credit\n'

############################################### BONUS ##############################################
def processOperator(rpn, stack, token):             # Add ops to stack according to precedence
  if((stack.stackLen() - 1) < 0):                   # When stack is empty add token
    stack.push(token)
    return
  else:
    top = stack.items[stack.stackLen() - 1]         # The item at the top of the stack
    if(top == '('):                                 # When ( is @ top of stack add token
      stack.push(token)
      return
    if((token == '*' or token == '/') and (top == '+' or top == '-')): # When * or / come after + or -
      stack.push(token)
      return
    else:                                # Else pop & app top to rpn exp & loop until able to 
      rpn.append(top)                    # push token to stack
      pop = stack.pop()
      processOperator(rpn, stack, token)

def processStack(rpn, stack, top):       # Pop & app top of stack until ( or end of stack  
  if(top == '('):                        # Found ( return
    return
  if(stack.stackLen() == 0):             # Last token of stack, pop and app to rpn exp.
    rpn.append(top)
    return
  else:                                  # Else keep popping & appending until conditions met
    rpn.append(top)
    top = stack.pop()
    processStack(rpn, stack, top)

with open('input_RPN_EC.txt', 'r') as file:   # Open file and save data
  content = file.read()
data = content.split('\n')               # Parse data into lines at every new line char
for line in data:                        # Loop through the parsed line
  elements = line.split(' ')             # Parse the line into tokens at every space char
  rpn = []
  stack = Stack()
  for token in elements:                 # Loop through the parsed tokens
    if(token.isdigit() == True):         # When you find a # add it to rpn exp.
      rpn.append(token)
    if(token == '('):                    # When you find a ( add it to the stack
      stack.push(token)
    if(token == ')'):                    # When you find a ) call function to process
      top = stack.pop()
      processStack(rpn, stack, top)
    if(token == '+' or token == '-' or token == "*" or token == '/'):   # Call function to process
      processOperator(rpn, stack, token)
  if(stack.stackLen > 0):                # When no more tokens add remaining stack to rpn exp.
    top = stack.pop()
    processStack(rpn, stack, top)
  stack = Stack()
  for value in rpn:                      # Print the rpn exp. per instructions
    print value,
    processRPN(stack, value)			 # Call function to process rpn token & stack
  print ""
  result = stack.pop()
  print result

