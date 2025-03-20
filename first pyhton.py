
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


str_welcome="Thank you for Using Hiren's software."#Strings
str_comeagain="please Visit Again."
print (str_welcome+str_comeagain)#Concatination
print(len(str_comeagain))#Length of String
ch = str_welcome[16]
print(ch)#character in a String
print(str_welcome[1])

#Slicing of a String in between
print(str_comeagain[1:6])
#Slicing can be done backwards aswell
print(str_comeagain[-5:-6])

str.index(str_comeagain.count("A"))#functions of strings

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
    
    
hiren_ages = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
print(hiren_ages)
print(len(hiren_ages))
print(hiren_ages[18])#Lists(arrays) in Phython
hiren = ["Hiren Kodwani","age 19","Sex: Male",]
print(hiren[2])
print(hiren_ages[5:9])#Slicing in Lists
print(hiren.sort(reverse=True))
print(hiren)
print(hiren_ages.remove(15))
print(hiren_ages.pop(5))
print(hiren_ages)#Deleating element from the list

#Tupples
hirenkodwani = (1,635413,88,4435,5468,)
print(hirenkodwani[3])
print(type(hirenkodwani))
print(hirenkodwani [1:3])
print(hirenkodwani.__contains__)#Address of tupple


movie1 = input("Enter your 1st favpurite movie:")
movie2 = input("Enter your 2nd favourite movie:")
movie3 = input("Enter your 3rd favourite movie:")
movies = [movie1,movie2,movie3]
print ("Your Favourite Movies are :",movies)#to store fav movies in a list

student_grade = ("C","D","A","A","B","B","A")
print (student_grade.count("A")) #count no of A in student grades tupple


student_gradelist = ["C","D","A","A","B","B","A"]
student_gradelist.sort()
print(student_gradelist)#to sort grades of students



#dictionary
dictonary = {"hiren":"is a great person",
 "Rinky" :"Mother of hiren",
 "marks of hiren": {"A+","C-","B","A"}#nested dictionary
}
print ("Details of Hiren are", dictonary)
dictonary["hiren"] = "kodwani"#overwriting in a dictionary
print(dictonary)
#functions in dictionary
print(len(dictonary))#gives no of unique values in a set/dictionary
print(list(dictonary))
mahesh = {"buissnessman": "Watches",
          "property":"land,houses and warehouses"}
print(dictonary.update(mahesh))#addition of new dictionary into old one
print(dictonary)
print(dictonary.keys())


#sets: dictionary with unique elemets are called sets
numbers = {0,1,2,3,4,5,6,7,8,9}
values = {7,8,9,10,11,2}
print (type(numbers))
print(numbers.pop())
print(numbers.union(values))
print("All numbers are",numbers.intersection(values))



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


#for loop
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
      
      
