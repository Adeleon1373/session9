def greet():
    """"
    Simple function printing hello
    :return 0
    """
    print("Hello")
    return 0

def greet_improved(name):
    """
    More complex greet that takes a name as parameter
    :param name: the name of the person to greet
    :return: None
    """
    print("Hello", name)

greet_improved("John")

def custom_op(x,y):
    """
    Custom op: 10x + y
    :param x: the first number
    :param y: the second number
    :return: number, 10x + y
    """
    result = 10*x + y
    return result

print(custom_op(5,8))
x = custom_op(5,9) #arguments by position!
print(f"the result of custom_op is: {x}")
x = custom_op(y=9, x=5) #arguments by name!
print(f"the result of custom_op is: {x}")
print(custom_op(5,0)) #using default values for y
print(custom_op(0,0)) #default values for both
print(custom_op(0,y=9)) #default value for x

def bond_intro(name):
    print("the name is", name)

def bond_name(first, last):
    return f"{last}, {first} {last}"

print(bond_name("Andre","de Leon"))
bond_intro(bond_name("Andre", "de Leon"))
