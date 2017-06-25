from sys import argv

script, filename = argv

txt = open(filename)

print ("Here's your file: %r" % filename)
print(txt.read())

print("Type your file again, please: ")
filename_again = raw_input(">> ")

while filename_again != filename:
	filename_again = raw_input("Wrong name !!@ Again >> ")
	
txt_again = open(filename_again)
print(txt_again.read())

txt.close()
txt_again.close()
print("------end-ex15")

print("We are going to erase %s" %filename)
raw_input("If it not okey, hit Ctrl+C - If okey, hit y:")

print ("Openning file .. for Writing..")
target = open(filename, 'w')# open file just for writing
print(" Truncating the file.. See ya:v")
target.truncate()
print("Now I am gona ask you for 3 lines !")

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print("I am gonna write these lines to file...")

target.write(line1)
target.write(line2)
target.write(line3)
print("close it ..")

target.close()

raw_input("Do you wanna Reading it? ")
target = open(filename,"r")
print("Here we have output !")
print(target.read())
target.close()
