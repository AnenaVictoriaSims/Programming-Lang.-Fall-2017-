import os

def processLine(line): 
	quote = 0
	com = 0
	count = 0

	for token in line:
		rules1 = [token == '{',quote == 0,com == 0]
		rules2 = [token == '}',quote == 0,com == 0]
		rules3 = [token == '"',quote == 0]
		rules4 = [token == '/',com == 0]
		rules5 = [token == '/',com == 2]
		if all(rules1):
			count = count + 1
		if all(rules2):
			count = count - 1
		if all(rules3):
			quote = 1
		if all(rules4):
			print("Com now = 1")
			com = 2
		if all(rules5):
			com = 1
	return count 

# Open file, save data to 'content', close file
with open(os.path.join(os.getcwd(), "input.txt"), 'r') as file:    
	content = file.read()        

count = 0																 # Track the { depth  
track = 0                           
data = content.split('\n')               # Parse data into lines at every new line char
for line in data:  
	track = processLine(line)
	print(count,line)
	count = count + track


 