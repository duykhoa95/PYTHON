from sys import argv
from os.path import exists

script, filename = argv

def print_all(file):
	print(file.read())

def rewind(file):
	file.seek(0) # move the pointer to 'first byte' in the file
	
def print_line(line_count, file):
		print(line_count,file.readline()) #after readline(), the pointer stop
	
# print ("Does the file exists? %r\n" %(exists(filename)))	
#print(f"Does the file exist? {exists(filename)}")
#print(f"Does the file exist? {exists(filename)}")
current_file = open(filename)

print(" Print the whole file: ")
print_all(current_file)

print("Now, let's rewind, kind of like a tape. \n")
rewind(current_file)

print("Let's print three lines: ")

current_line = 1
print_line(current_line, current_file)

current_line = current_line + 1
print_line(current_line,current_file)

current_line += 1
print_line(current_line,current_file)

current_file.close()