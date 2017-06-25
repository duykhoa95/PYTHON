# to run this script: add argument to command
# demo: python ex13,1.py [var1] [var2] [var3]

from sys import argv

script, name, live, job = argv

print "the script is called:", script
print "Your first variable is:", name
print "Your second variable is:", live
print "Your third variable is:", job

print "\n-----------test----------\n"
prompt = "> khoa dep trai > "
print ("Hi %s, I'm the %s script !")%(name, script)
print(" I'd like to ask you a few question. ")
print(" Is it okeys, %s") % name

okey = raw_input(prompt)

print("Let me guess ,you in %s?") % live
home = raw_input(prompt)

print("Oh:) Let me try it again:D You are an %s") % job

carrer= raw_input(prompt)

print("Let me guess, you in %s?") % live
home = raw_input(prompt)

print("So, what's programming langguage you like the most, %s?")  % name
langguage = raw_input(prompt)

print("Okey, see ya! \n\n -----------E.N.D-ex13-14----")