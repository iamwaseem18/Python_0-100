n : int = 5 #This is a new way of telling python that n is an integer

# Now when i use n. here the python will automatically give me all the integer methods

name : str = "Waseem"

#Let us see how it works for functions

def sum(a:int, b:int) -> int:
    return(a+b)
sum(3,4) 

#This will make your program readable


from typing import List, Tuple, Union

#List of Integers 

numbers: List[int] = [1,2,3,4,5]

#Tuple of a integer and strng

person : Tuple[str, int] = ("Waseem", 23)

#Union type for variables that can hold multiple types

identifier: Union[int, str] = "Was123"