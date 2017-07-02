class MyStuff(object):
	def __init__(self):
		self.tangerline = "And print sth"
	
	def run(self):
		print("running")
		
test_class = MyStuff()
test_class.run()
print(test_class.tangerline)

print("-"*20,"--------------test-1")
class Song(object):
	
	def __init__(self,lyrics):
		self.lyrics = lyrics
	
	def print_some_things(self):
		for line in self.lyrics:
			print(line)
			
text1 = Song(["first","second"])
text2 = Song(['abc','xyz'])

text1.print_some_things()
text2.print_some_things()

text3 = Song(12)

print("-"*20,"---------------------test-2")
class Animal(object):
	""" docstring for Animal """
	def __init__(self,genus, age=11,demo=''):
		self.genus = genus
		self.age = age
		self.demo = demo
	
	def foot(self):
		print("Run!")
		
	def say(self):
		print("Say Animal")
		
dog = Animal('Dog',10)
print("Genus: ",dog.genus)
print("Age: ",dog.age)
print(getattr(dog,'genus'))
dog.name = "REX"

cat = Animal('Cat')
print("Name: ", cat.genus)
print("Age: ",cat.age)
print("Demo: ",cat.demo)

# if (not(hasattr(dog, 'name'))):
#     setattr(dog, 'name', 'Rex')

# print("Name: ", dog.name)
# print("Age: ", dog.age)

