# Anena Sims
# 1001138287
# Submitted: 11/09/2017
# Code compiled and executed on Apple OS using python3 ./avs8287_PA3.py
# Assignment 2: RPN Calculator using Python

import os

# Function checks each line for a { or }
def processLine(line):                  
  quote = 0                                       # Track when a quote occurs
  com = 0                                         # Track when a comment symbol occurs
  count = 0                                       # Tracks change in depth

  for token in line:                              # Checks every token in given line
    rules1 = [token == '{',quote == 0,com == 0]   # Found { if no quote or comment symbol found 1st
    rules2 = [token == '}',quote == 0,com == 0]   # Found } "                                     "
    rules3 = [token == '"',quote == 0]            # Found start " if one hasn't been seen yet
    rules4 = [token == '/',com == 0]              # Possible // (this could be a division symbol)
    rules5 = [token == '/',com == 2]              # Found // if a prior / has been found
    if all(rules1):
      count = count + 1                           # Increment count when { found
    if all(rules2):
      count = count - 1                           # Deincrement count when } found
    if all(rules3):
      quote = 1
    if all(rules4):
      com = 2
    if all(rules5):
      com = 1
  return count                                    # Return depth tracker

# Open file, save data to 'content', close file
with open(os.path.join(os.getcwd(), "input.txt"), 'r') as file:    
  content = file.read()        

count = 0                                # Keeps up with the current { depth  
track = 0                                # Tracks the changes in depth
data = content.split('\n')               # Parse data into lines at every new line char
for line in data:                   
  track = processLine(line)              # Send every line of data to processing function
  if(track == -1):
    print(count,line)                    # Print the current line and CURRENT depth
    count = count + track
  else:
    count = count + track
    print(count,line)

