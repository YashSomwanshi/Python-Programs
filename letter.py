# Strings are Immutable Which means it does not change after using the functions but it creates a new function.



letter = '''  
Dear Name, 
You are selected! 
Date 
        '''

# a=input("Enter Name")
# b=input("Enter Date")

a=letter.replace("Name","yash").replace("Date","25th Spetember 3040")
# b=a.replace("Date","19")

print(a)