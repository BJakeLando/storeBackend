# Variables

name = "Brandon"
last_name = "Landers"
age = 36
price = 12.31
found = False

print(name)
print(last_name)

print(name + last_name)  # string concatenated
print(21 + 21)  # sum

# print(21 + name) TYPE ERROR

# math operands

# if statements
if age < 100:
    print("Don't worry you are still young")
    print("Inside the if")
    print("Inside the if")

elif age == 100:
    print("Congrats on the century")
else:
    print("sorry, you are getting old buddy...")


def test():
    print("I'm a function")


def say_hello(name):
    print("Hello there, " + name)


def sum(num1, num2):
    return num1 + num2


test()

say_hello("Bart")

result = sum(21, 21)
print("the result of the sum is: " + str(result))
