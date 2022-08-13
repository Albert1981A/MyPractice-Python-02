
def do():
    print('Hello from Module A')

def do2():
    print('Hello from Module A 2')

# printing " __name__ " will print the name of the module
# If we run Demo1_Module_A it will print "__main__"
# If we run Demo1_Module_B or C or D it will print "Demo1_Module_A"
print(__name__)


# It's important to know if the file is running as "main" or another file is calling and running it
# A way to know if the file run as "main is to write the following:"
if __name__ == "__main__":
    #Run Extra Code ... 
    pass