def print_none():
	print("func 1")
	
def print_one(var1):
	print("var1:%r"%var1)

def print_two(var1,var2):
	print("var1: %r \t - \t var2: %r" %(var1,var2))

def print_two_again(*var): #var->list
	var1,var2 = var
	print("var1: %r \t - \t var2: %r" %(var1,var2))

print_none()
print_one("funtion 1")
print_two("funtion 2","funtion 2")
print_two_again("funtion 4",4)

print("----end--ex18-----")

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print("You have %d cheese"%cheese_count)
	print("You have %d boxs of crackers \n" %boxes_of_crackers)

print("we can give the funtion members directly")
cheese_and_crackers(20,20)

print("Or, we can use variable from our script")
amount_of_cheese = 10
amount_of_crackers = 15

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do the math inside too")
cheese_and_crackers(1+2,5/2)

print("Or combine two")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+123)
