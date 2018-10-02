"""This module contains two simple functions, one to print the user name, and other to
tell the user age after 25 years."""

def hello_user():
    """This function prompts the user for his/her name,
and then prints the name greeting the user."""
    name = input("Please enter your name: ")
    return "Hello my dear "+name

def after_25():
    """This function tells the user his/her age after 25 years."""
    age = eval(input("Please enter your age rounded: "))
    return "Your age after 25 years is "+str(age+25)
