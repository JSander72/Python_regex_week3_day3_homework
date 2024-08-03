import re

def verify_names(names):
    """
    Verify if each name in the list matches the given regular expression pattern.
    If a name matches, it is printed; otherwise, an error message is printed.
    """
    pattern = re.compile(r'^[A-Z][a-z]+(?: [A-Z][a-z]+)*$')

    for name in names:
        if pattern.match(name):
            print(name)
        else:
            print("Invalid name")

# List of names to test the function
names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", 
         "Jordan Alexander Williams", "Madonna", "programming is cool"]

verify_names(names)
