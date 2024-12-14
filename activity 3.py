#Write a program to create a class Parrot and perform the following tasks -
#  Create a class variable species
#  Create a __init__ method that has instance variables - name and age 
# Create instances of class Parrot, passing arguments as well Print Class variable by accessing it Print Instance variables as well

class Parrot:
    #class variable
    species="Bird"
    def __init__(self,name,age):
        #instance variables
        self.name=name
        self.age=age

p1=Parrot("Blu",5)
p2=Parrot("Rio",6)

print("{} is a {}".format(p1.name,p1.species))
print("{} is a {} year old".format(p1.name,p1.age))

print("{} is a {}".format(p2.name,p2.species))
print("{} is a {} year old".format(p2.name,p2.age))


