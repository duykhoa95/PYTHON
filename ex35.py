from sys import exit

def gold_room():
    print("Type")

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
        print(choice)
        print(how_much)
    else:
        exit(0)
        

gold_room()
print("okey")
