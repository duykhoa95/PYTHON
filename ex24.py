

print ("----- test")

poem="""
\tone sheep
two sheep
three sheep
\tand \n done!
"""

print("-------------")
print(poem)
print("--------------")

one = 10-9
print(f"This should be one: {one}")
def fomula(input):
	bike = input * 100
	mote = bike /100
	car  = mote/100
	return bike, moto, car

start_input = 10000
bike,moto,car = fomula(start_input)

# one way to format a string
print("With a staring point of: {}".format(start_input))
#  it's just like with an f"" string
print(f"We'd have {bike} bike, {moto} motos, and {car} car.")

start_input /=10

list_test = fomula(start_input)
print("=> {} bikes, {} moto, and {} cars".format(*list_test))