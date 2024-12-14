#Write a program to create a class Parrot and perform the following tasks - 
# Create a class variable species 
# Create a constructor that has instance variables - name and age 
# Create instance methods for this class named sing and dance, making them print a message.
#  Create instances of class Parrot, passing arguments as well
#  Print Class variable by accessing it 
# Print Instance variables as well

class Parrot:
    #class variable
    species="Bird"

    #constructor
    def __init__(self,name,age):
        #instance variable
        self.name=name
        self.age=age
    #instance method
    def sing(self,song):
        print("{} sing song {}".format(self.name,song))

    def dance(self):
        print(self.name,"is now dancing")

p1=Parrot("Blu",10)
p2=Parrot("Rio",5)
print("{} is a {} and is {} years old".format(p1.name,p1.species,p1.age))
p1.sing("Happy")
p1.dance()
print("{} is a {} and is {} years old".format(p2.name,p2.species,p2.age))
p2.sing("Party")
p2.dance()