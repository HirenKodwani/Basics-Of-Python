
#ALL CODES Written while learning and performing experiments with various features of PYTHON:
"""These are Refered as Notes"""


name=input("what is the name :")
print("its your lucky day",name)
age= int(input("Whats your age :",))  
if(age>19 and age<69):

    print("You are an Adult as your age is",age)
elif(age>79):
    print("Marega kya Buddhe bsdk")
elif(age==18 or age==19): 
     print("Liacence le lo pehle ")
     
else:
    print("Pogo dekh jaa ke bache")    

price=float(input("Whats you Budget? :"))  
print ("so your budget is",price)
print (age==price) #operator
print(not(age==69))
print(type(name))

print ("Hiren Kodwani", end ="is a great person of age",)#to join 2 lines in a single print function

a=int(input("Give the first number",))
b=int(input("Give second number",))
print("sum is :",a+b)

a=int(input("Give the side of the square" ))
print("Area of Square is:",4*a)


a=float(input("Give the first Decimal No:"))
b=float(input("Give the second decimal No:"))
sum=a+b
print("Average of the numbers is :",sum/2)

a=int(input("Enter the first no:"))
b=int(input("Enter the second no:"))
print(a>=b)

#Strings
str_welcome="Thank you for Using Hiren's software."
str_comeagain="please Visit Again."
print (str_welcome+" ",str_comeagain)#Concatination with space in between
print(len(str_comeagain))#Length of String
ch = str_welcome[16]
print(ch)#character in a String
print(str_welcome[1])
print(str_comeagain*3)#To print a string multiple times

#Slicing of a String in between
print(str_comeagain[1:6])
#Slicing can be done backwards aswell
print(str_comeagain[-5:-6])
print(str_comeagain.split())#Functions in Strings
str_comeagain[slice(1,6)]#another way of slicing

str.index(str_comeagain.count("A"))#functions of strings to count no of any element in string and Indexing

str_name=(input("Input Your Name")) 
print(len(str_name)) #no of charater in name 


a=float(input("Enter the Number :"))
rem=a % 2
if (rem ==2):
    print("Number is a Even No")
    
else:
    print("Number is a ODD no")#to check odd or even
    
    
a=input("Enter the first no:")
b=input("enter the second no:")
c=input("Enter the third no:")

if(a>b>c or a>c>b):
    print("First no is the GOAT")
    
elif(b>a>c or b>c>a):
    print("Second no the GOAT")

else:
    print("Third is the GOAT")# To Find greatesr no from 3 no



a = float(input("Enter the Number"))
rem = a % 7
if (rem==0):
    print("number is multiple of 7")
else:
    print("Number is not a multiple of 7")   # To fine if the number is multiple of 7 
    
    
#Lists(arrays) in Phython    
hiren_ages = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
print(hiren_ages)
print(len(hiren_ages))
print(hiren_ages[18])
hiren = ["Hiren Kodwani","age 19","Sex: Male",]
print(hiren[2])
print(hiren_ages[5:9])#Slicing in Lists
print(hiren.sort(reverse=True))
hiren.insert(3,"Marital Status:Not Married")#to insert any element at any position in the list
print(hiren)
print(hiren_ages.remove(15))
print(hiren_ages.pop(1))#Deleating element from the list
print(hiren_ages)
del hiren_ages(5,9)#Deleating element from the list using keyword
print(hiren_ages)


#Tupples
hirenkodwani = (1,635413,88,4435,5468,)
print(hirenkodwani[3])
print(type(hirenkodwani))
print(hirenkodwani [1:3])
print(hirenkodwani.__contains__)#Address of tupple


movie1 = input("Enter your 1st favpurite movie:")
movie2 = input("Enter your 2nd favourite movie:")
movie3 = input("Enter your 3rd favourite movie:")
movies = (movie1,movie2,movie3)
print ("Your Favourite Movies are :",movies)#to store fav movies in a list

hirenkodwani+=(movies)
print(hirenkodwani)#Concatination in Tupples


student_grade = ("C","D","A","A","B","B","A")
print (student_grade.count("A")) #count no of A in student grades tupple


student_gradelist = ["C","D","A","A","B","B","A"]
student_gradelist.sort()
print(student_gradelist)#to sort grades of students



#Dictionary
dictonary = {"hiren":"is a great person",
 "Rinky" :"Mother of hiren",
 "marks of hiren": {"A+","C-","B","A"}}#nested dictionary

print ("Details of Hiren are:", dictonary)
dictonary["hiren"] = "kodwani"#overwriting in a dictionary
print(dictonary)
#functions in dictionary
print(len(dictonary))#gives no of unique values in a set/dictionary
print(list(dictonary))
mahesh = {"buissnessman": "Watches",
          "property":"land,houses and warehouses"}
print(dictonary.update(mahesh))#addition of new dictionary into old one using "update" function
print(dictonary.keys())
dictonary["hiren"] #Method for Indexing in Dictionary


#Sets: dictionary with unique elemets are called sets
numbers = {0,1,2,3,4,5,6,7,8,9}
values = {7,8,9,10,11,2}
print (type(numbers))
print(numbers.pop())
print(numbers.union(values))
print("All numbers are",numbers.intersection(values))
numbers = numbers,values
print("All of the Numbers are:",numbers)#Concatination in Sets



marks = {}
a = input("enter marks in physics:")
b = input("enter marks in chemistry:")
c = input("enter marks in maths:")
marks.update ({"physics":a})
marks.update({"chemisty":b})
marks.update({"maths":c})
print("Report card of the student is:",marks)

#LOOPS
count = 1
while count <= 100:
    print(count)
    count += 1
    
print ("loop ended")

n = int(input("Enter the number:"))
count = 1
while count <= 10:
    print(n*count)
    count += 1
print ("loop ended")#multiplication of any given number

numbers = [1,4,9,16,25,36,49,64,81,100]
i=0
while  i<=9 :
     print(numbers[i])
     i+=1
print("Loop ended") #to print elements of list using list    

given = (1,4,9,16,25,36,49,64,81,100,)
x =int(input("Enter the number whose address to be found in tupple:"))
i = 0
while  i < len(given):
    
    if(given[i]==x) :
       print("Found the element",i)
       
    elif(given[i]==9):
        print ("Loop broke")
        break#terminates the loop
    elif(i==8):
        print("Skipping this value")
        continue#skipis any element mentioned from the loop
    
    
    else:
        print("Searching...")
    i +=1
    
print("loop ended")#Traversal in a tupple using loop


#For loop
teachers = ["mother","Alakh Pandey","Shradha didi","Khare BC","Pathak sir","Aniket sir"]
for person in teachers:
    print(person)
else:
    print("Loop eneded ") 
    
    
powers = [1,4,9,16,25,36,49,64,81,100]
for numbers in powers:
    if(numbers<=1):
        print("Value in Database is :",numbers)
    elif(numbers>=1):print("Another values in database is:",numbers)
print("loop ended sucessfully")#print values for a list in a systmatic manner

powers = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Number to be found is :"))

for numbers in powers:
    if(numbers==x):
      print("Number is found")
      break
    else:
        print("Searching....")       
print ("loop ended")#to find a number in a tupple using for loop 


#RANGE
r = range(100)
for x in r:
    print("number is:",x)#to print the whole range using for loop
    
#RANGE with conditions
r = range(100,0,-1)
for x in r:
    print("number is:",x)#to print the range putting conditions in range  
print(r.index(2))#Indexing in range
    
r = range(1,11)
n = int(input("Number whose table is neede is :"))
for x in r:
    print("n X x=", x*n)#to print the table of N putting conditions in range 
    

    n = int(input("Number whose factorial sum is to be found is"))
sum = 0
for c in range(1 , n+1):
    print(c)
    sum +=c
print("Sum of all no is :",sum)#to find sum of a range of values using range


n = int(input("Number whose factorial sum is to be found is"))
factorial = 1
for c in range(1 , n+1):
    print(c)
    factorial *=c 
print("Factorial of all no is :",sum)#to find factorial of a range of values using range



#FUNCTIONS
a = int(input("Enter the first no:"))
b = int (input("Enter the second no:"))
def product(a,b): #defining function
    print("Product of 2 no is ",a*b)
    return a*b
multiplication= product (a,b)#definig this way makes the function activate
print(product)#address of function
print ("product of 2 numbers is",multiplication)#gives "none" for non-return functions


def myname():
    print("Hiren Kodwani")
name = myname()#running a function for pinting a name


def average(a,b,c=0,d =8,):#funtions can also have default values but default values can be redifined also
    sum = a+b+c+d
    avg = sum/4
    print(avg)
    return avg
average(582168,4684,6546,684638)#Used this way

def length_list(list):
    print(len(list))
    return len  

a = [1,2,3,4,5,6,7,0]
length_list(a)#function to give length of a list



a = [1,2,3,4,5,6,7,6,8]
b = ["hiren is best" , "he scores good marks ","himanshu is good","he scores less marks than hiren" ]
def elements_list(list):
    print(list)   

elements_list(a)#function to print a list
elements_list(b)



def currency_converter(a):
    product = a*87.01
    print("Current USD to INR rate is",product)
    return product#function to convert USD to INR
    
l = int(input("Enter USD amount to be converted"))
currency_converter(l)    


def number_check(a):
    rem = a%2
    if( rem == 0):
        print ("Number is Even")
    else:
        print("number is odd")
    
b = int(input("Enter the number to be checked:"))
number_check(b)#to check no is odd or event usning function


#RECURSION - Used in place of Loops
def numbers(a):
    if(a==0):
     print("Loop ends here")
    return
    print(a)
    numbers(a-1)#Reaccuring function in a function
    print("Loop Ends here")
numbers(54)

def factorial(f):
    if(f==0 or f==1):
        return 1
    else:    
        return f * factorial(f-1)  #Reoccuring Function in a function
b = 5
print(factorial(b))#to Find Factoral of a number using Recusion

def sum(n):
    if(n == 0):
        print("Ni ho payega")
        return 0 
    else:
        return n +sum(n-1)
        print(n=sum(n-1))   #to calculate sum of n natural number using recursion
b = 54
print(sum(b))

def elements_list(list , idx=0):
    if(idx ==len(list)):
        return
    print(list[idx])
    elements_list(list,idx+1)#Recursive function 
    
teachers = ["mother","Alakh Pandey","Shradha didi","Khare BC","Pathak sir","Aniket sir"]

elements_list(teachers)#Printing all elements of a list using Recursive index function 



#FILES:
f = open("C:/Users/ADMIN/Downloads/demo file.txt")#Accesing file
admit_card= f.read()#Reading the file
print(admit_card)
print(type(admit_card))
f.close

f = open("C:/Users/ADMIN/Downloads/demo file.txt","a")#Accesing file(USE forward slashes!!!)
f.write("I LOVE my parents even though I Dont express them")
f = open("C:/Users/ADMIN/Downloads/demo file.txt","r")
file = f.read()
print("Text in the file is:",file)#Appending (adding text at the end)a file and reading it
f.close

f = open("C:/Users/ADMIN/Downloads/demo file.txt","w+")#Accesing file(USE forward slashes!!!)
f.write("hello everyone my name is Hiren Kodwnai son of Mahesh Kodwani and also son of Rink Kodwani which is MY MOTHER he he he I LOVE my parents even though I Dont express them")
f.close
#Using Truncate function to write in a file

#WITH function
with open("C:/Users/ADMIN/Downloads/demo file.txt","r") as f:
    text = f.read()
    print("Text in the file is:",text)
    #no need to close"with" closes it automatically
with open("C:/Users/ADMIN/Downloads/demo file.txt","a") as f:
    hiren = f.write("This are feeling of Hiren Kodwani")

#Deleating a file:
import os
os.remove("C:/Users/ADMIN/Downloads/Install VALORANT.exe")#Deleating any file from the Computer using pyhton!!! other various functions after os. can also be used for various operations 

with open("C:/Users/ADMIN/Downloads/Practice text.txt","a")as file:#Creates a new file and writes in it
    file.write("Hi Everyone \n we are learning file i/o \n using python. \n I Love to do Programming in Python ")
    
with open("C:/Users/ADMIN/Downloads/Practice text.txt","r") as file:
    text = file.read()
    print("Text in the file is:",text)#And printing the text in the newly created file
    


with open("C:/Users/ADMIN/Downloads/Practice text.txt","a")as file:#Creates a new file and writes in it
    file.write("Hi Everyone \n we are learning file i/o \n using python. \n I Love to do Programming in Python ")
    
with open("C:/Users/ADMIN/Downloads/Practice text.txt","r") as file:
    text = file.read()
    update = text.replace("Python","C++")#To replace elements from file to other
with open("C:/Users/ADMIN/Downloads/Practice text.txt","w") as file:
    file.write(update)
      
      
#ARRYS IN PYTHON:
array =('f',[1,2,3,4,5,6,7,8,9,10])#in python arrys are made usning list with defining data type in array
for a in array:
    print(a)#to print a array in python "for" loop is used



#NUMPY
import numpy as numumy#including nummpy liabrary to the code
hiroo = [20,18,16,15,10,12]
arr = numumy.array(hiroo,dtype=int)#declaring an array using numpy
arr = arr.reshape(2,3)#This transformation of 1D array to multi dimestional array is possible due to numpy liabrary
print(arr)
print(arr.shape)#Gives order of any array
#addition of ultiple arrays
q = numumy.array([[484,568],[638,548]],dtype=int)
w = numumy.array([[478,535],[653,598]],dtype=int)
print(q+w)#adds 2 arrays
print(numumy)#Gives address of numpy liabrary in computer
print(numumy.add(q,w))#adds 2 arrays
print(numumy.sum(q))#Gives sum of all the elements of  array

#Python For Data Science
import numpy as np
import random as rd
#print (array=np.random.random([6,4]))
hire=np.array([[123,684,684],[4,8,9]])
print(hire.size)
print(hire.shape)
print(hire.reshape(3,2))
print(np.sum([[4,8,7],[8,5,9]],axis = 1))#Sum of all elements in an Array


#PANDAS for Data Handling and analysis

import pandas as pandu
table = pandu.read_excel("C:/Users/ADMIN/Downloads/DSAC event flow 6 dec.xlsx")
print(table)#This prints all the data from hthe excel sheet

#Dataframes
f=pandu.DataFrame({"name":["Hiren","Himanshu", "Harshal","Khushi"],"marks":[468,468,354,123]})#Dataframe which is a Data type of Pandas
print(f)#Generated table is Shown here with above data
SandP_Companies = pandu.read_excel("C:/Users/ADMIN/Downloads/S&P 500 Companies (Standard and Poor 500).xlsx")#Importing existing excel sheet using Pandas
S = SandP_Companies.copy(deep=False)#Shallow copy
S = SandP_Companies#Deep Copy
print(SandP_Companies.tail)#last 5 rows 
print(SandP_Companies.head)#First 5 rows
print(SandP_Companies.at[4,"Sector"])
print(SandP_Companies.iat[2,2])#Accesing each cell using functions of Pandas
print(SandP_Companies.dtypes(Exception = []))#Shows the data type of the Data stored in the file or sheet
print(SandP_Companies.select_dtypes(object))#Includes all the objects understood in the excel sheet

#MATPLOTLIB - Data Visulaization
import matplotlib as plt



#Stone Paper Sissor Game
import random as ran

random_chioice= ran.choice([-1,0,1])
#-1 means stone
#0 means paper
#1 means sissor

user = str(input("Write first letter capital \nStoooonnee Paaaappperr Sissor! :"))

if(random_chioice==1 and user == "Stone"):
    print("Computer------->Sissor")
    print("Yaayyy You win")
    
elif(random_chioice==1 and user =="Sissor"):
    print("Computer------->Sissor")
    print("Its a Tiee!!")
elif(random_chioice==1 and user == "Paper"):
    print("Computer------->Sissor")
    print("Better luck next time \nYou Loose")


elif(random_chioice==-1 and user == "Paper"):
    print("Computer------->Stone")
    print("Yaayyy You win")
elif(random_chioice==-1 and user =="Stone"):
    print("Computer------->Stone")
    print("Its a Tiee!!")
elif(random_chioice==-1 and user == "Sissor"):
    print("Computer------->Stone")
    print("Better luck next time \nYou Loose")



elif(random_chioice==0 and user == "Sissor"):
    print("Computer------->Paper")
    print("Yaayyy You win")
elif(random_chioice==0 and user =="Paper"):
    print("Computer------->Paper")
    print("Its a Tiee!!")
elif(random_chioice==0 and user == "Stone"):
    print("Computer------->Paper")
    print("Better luck next time\n You Loose")
else:
    print("Wrong Input ")


#OOP in Python

class Student: #Defining/Declaring Class
   
    school_name ="St. Paul Higher Secondary school"#Class Attribute defined whose data will be avilable in all its objets if printed
   
    def __init__(self,name,age):#Constructor for generating new objects with Reference (here as "Self") should be inclued in all the constructors
       self.name =name#This is a parametrised 
       self.age = age
       print("Admiting a new Student in the Institution:") #Argument in the Constructor which will always run when ever the Constructor will be called 
    def dashbord(self):
        print("Hello Student ",self.name,"\nFrom Institution:",self.school_name)
    def Telling_age(self):
        print("Your Age is =",self.age)

stu = Student("Himanshu","20")#definig Object of the Class Declared
print(stu.name)
print(stu.age)
print(stu.school_name)
stu.dashbord()

stu1 = Student("Hiren Kodwani", "19")#Declaring another object
stu1.age = 16#Defining new Parameters for New Object
print(stu1.name)
stu1.school_name = "Acropolis Institute"
print(stu1.school_name)
stu1.dashbord()
stu1.Telling_age()
#Destructor using "del" keyword
del stu.name
print(stu.name)#This will give an error as the object or Attribute is deleated by the destructor


#Creating a Student Class to store name and marks with a method to calculate average score from marks

class student():  
    def __init__(self,name,mark1,mark2,mark3):
        self.name = name
        self.marks_maths =int (mark1)
        self.marks_phy = int(mark2)
        self.marks_chem = int(mark3)
       
    def average(self,name,mark1,mark2,mark3):
        sum = mark1+mark2+mark3
        print("The Averge Score of ",self.name,"Student is:",sum/3)
    
Hiren = student("Hiren Kodwani",38,68,95)
Hiren.average("Hiren Kodwani",38,68,95)    


#Database of Accounts using OOP in python with different Attributes and Methods of Debit,Credit and showing the balance in the account
class Account():      
    
    def __init__(self,Balance,Account_no):
        self.Bal = int(Balance)
        self.acc = Account_no
        print(Account_no,"Has a Blance of",Balance)
        
    
    def Debit(self,amount):
        self.Bal  += amount
        print("Current Balance for Account no:",self.acc,"\nIs:",self.Bal)
               
    def Credit (self,amount):
        self.Bal -=amount
        print("Current Balance for Account no:",self.acc,"\nIs:",self.Bal)
         
    def Balance(self):
        print("Current Balance for Account no:",self.acc,"\nIs:",self.Bal)
        
        
acc1 = Account(684,"68768dw45846")
acc1.Debit(48)
acc1.Credit(8)
acc1.Balance#Invoking the method from the class

#Access Specifying in Python(public/private)

class Student: #Defining/Declaring Class
   #PRIVATE attribute
    __school_name ="St. Paul Higher Secondary school"#Declaring any Variable or method with 2"__" before name of that entity makes that PRIVATE
    #PRIVATE Method
    def __dashbord(self):#Declaring any Variable or method with 2"__" before name of that entity makes that PRIVATE
        print("Hello Student ",self.name,"\nFrom Institution:",self.school_name)
        
s1 = Student
print(s1.__school_name)#This will give an error as the data in the class is Declared PRIVATE


#INHERITANCE
class Data():#Base Class
    Company = "Accenture"
    def names():
        print("Hello People...")
        
class Company_data(Data):#Derived Class which is Inherited
    def __init__(self,name):
        self.names = name

Hiren = Company_data("Hiren Kodwani")
print(Hiren.Company)

#Multi-level Inhertance:
class Department_data(Company_data):#This is able to access data from 1st Class aswell 
    def __init__(self,department_name):
        self.department = department_name
        
Himanshu = Department_data("Development")
print(Himanshu.Company)
    
    
#Multiple Inhertance:
class Department_data(Company_data,Data):#This is able to access data from 1st and 2nd class 
    def __init__(self,department_name):
        self.department = department_name
        
Himanshu = Department_data("Development")
print(Himanshu.Company)       


#POLYMORPHISM:

#Operator Overloading:
print(1+5)#Sum
print("Hiren"+" Kodwani")#Concatinatoon
print([684,686,321]+[8468,8464,6846])#Merging of Lists
#Here Operator '+' has many different functions in a same code


#To Find Area and Perimeter of a Circle Usinng OOP and Methods
class Circle():
    def __init__(self,r):
        self.r = r

    def Area(self):
        return 3.14* self.r **2
        
    def Perimeter(self):
        return 2*3.14*self.r

C1 = Circle(5)
print(C1.Area())
print(C1.Perimeter())

