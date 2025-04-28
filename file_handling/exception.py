try:
    result =( 10 / 0) # error because division of zero
    result =int( 10 / 5)
except ZeroDivisionError as u:

    print(f"Error:{u}")
else:
    
    print("No error occurred.")
finally:
    
    print("This will always be executed.")
    