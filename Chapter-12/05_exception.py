try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e: # Here e is used to show the user that he has done some mistake in entering the input
    print("Please enter an integer value")

# We can even use exception handling to handle different type of error

# try:

# except ZeroDivisionError:
#     #Code

# except TypeError:
#     #code



