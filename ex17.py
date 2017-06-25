from sys import argv
from os.path import exists # to usse exists(filename)

script, file1, file2 = argv

print("Copying from %s to %s" %(file1,file2))

#file_in = open(file1)
# data= file_in.read()
data = open(file1).read()

print ("The Input file is %d bytes long ." %len(data))

print ("Does the Output exists? %r" %exists(file2))

raw_input("Hit Ctrl+C to abort! or Hit y to Continues: ")

file_out = open(file2,'w')
file_out.write(data)

print("All Done")

file_out.close()