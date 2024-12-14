#Write a program to create a class with name Student and perform the following tasks -
#  Create a class variable grade and name 
# Create a function to print a sentence 
# Create a function to print class variables grade and name
#  Create an object of class Student Call the two functions to execute them

class student:
    grade=10
    name=" Samira "

    def intro1(self):
        print("I am a student")

    def intro2(self):
        print("My name is{} and I study in class{}".format(self.name,self.grade))

st=student()
st.intro1()
st.intro2()