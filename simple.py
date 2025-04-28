def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    return x/y

def division(x,y):
    return x%y

print("Choose any operator you want to use :")
print("1.addition")
print("2.subtract")
print("3.multiply")
print("4.division")
print("5.modules")
operator =int(input("select operator you chioce from 1 to 5:"))
if operator == 6:
    print("invalid operator")

x =int(input("Enter number : "))
y =int(input("Enter number : "))

if operator == 1:
    print(x+y)
    
elif operator == 2:
    print(x-y)
    
elif operator == 3:
    print(x*y)
    
elif operator == 4:
    print(x/y)
    
elif operator == 5:
    print(x%y)
        
    
else :
    print("there is no answer")                