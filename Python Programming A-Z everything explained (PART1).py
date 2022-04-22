#!/usr/bin/env python
# coding: utf-8

#          
#        

# ## `First 'Hello World' code`

# In[1]:


"Hello World"  # Just type hello word as shown and you'll get the output


# ##  `Variable: Is a reserved memory space that can hold a value.`

# In[4]:


age = 14 # for example you can assign "age" value and it will stored in the memory


# In[7]:


age  # When you'll type age you'll get the appropriate value


# ## `Assigning variable for multiple project`

# In[10]:


person1, person2, person3 = ('Ram','Shyam','Radhe')  #here different variable are assigned different names so accordingly we wil get the results


# In[11]:


person1 #when we search for particular assign variable, will get the assigned result


# ## `Data types and Ints`

# In[13]:


#Till now we deal with numbers and alphabet they were known as strings

age1 = 14
age2 = 21
age3 = 19
#Here we will learn how to add/mutiply/subs them


# In[15]:


age1 + age2 # quite simle we just have to assign variables and operators between them for getting the results


# ## `Strings`

# In[16]:


FName = "Rishabh"
SName = "Tiwari"  # Here we will add the alpha as sh0wn in the example


# In[19]:


FullName = FName + SName


# In[21]:


FullName # This is how we can write the full name


# In[25]:


# In above we are getting proble of the space in the name so we can fix it by adding ' ' this between the add sign

FullName = FName + ' ' + SName 


# In[26]:


FullName


# In[27]:


# Now for finding any word from the given long paragram by specifying the exact position

Example = "Rishabh tfnndvndjvckjbhh jdbcdbvci  jkdbcvedb dcksvkj kdjvkd" 

# We want to know word at 10 postion in given example so for that we will do in this way


# In[28]:


Example[10]  # Always[] this to specify the position in the any random variable.


# In[29]:


# Always remember the counting in the python is done fromm 0 to n digit.


# In[31]:


# Now find out the whole bunch of the word by specifying the positions

Example[0:7] #Remember always take one digit extra at the end to find the suitable output


# 
# ## `Placeholders - If you want to send a birthday invitation to many people the this can play a crucial role in it and it will make  the things to easy going.`

# In[4]:


birthday = "Hello %s, you're invited to my birthday"


# In[3]:


print(birthday%("Rishu"))


# In[35]:


# If you want to add full name on the birthday invitation then use %s twice a time

birthday = "Hello %s %s you're invited to my birthday"


# In[36]:


print(birthday%("Rishabh",'Tiwari'))


# In[39]:


# If you want to send  to too many people then use the coding in this way as i instruted

birthday = "Hello %s, you're invited to my birthday"
arr = ("Bob","Ram","Ash","Rishu") #person who are to be invited
for i in arr:
    print(birthday%(i))


# ## `List of functions and arrays`

# In[46]:


Slist = ["milk","chips","chocolate","juice","paneer"] # Shopping List and in this we want to know our our third number of item and always list items on box bracket else it in round bracket it will become tuple which is not editable


# In[41]:


Slist[3]


# In[45]:


# If we want to replace any of listed item with other then we don't need to write whole thing we just need to do in this way

Slist[3] = "Powder"


# In[47]:


Slist # Now we can check the updated list


# In[48]:


# We can use the 'del' function to delete or add the items

del Slist[3]  # Deleting the 3rd item from our list


# In[49]:


Slist #Now check the updated list


# In[52]:


# If we want to count the list then we can use 'len' function 

len(Slist)


# In[62]:


# If we want to update the list we can use the 'append' function 

Slist.append("Juice") #For adding the 'juice in the list


# In[63]:


Slist #Check the updated list


# In[66]:


# As we used append function too many times so that's why our list have too much of juice in list and we can delete them

del Slist[5:]  #We deleted from 5 onwards till ennd


# In[67]:


Slist


# In[70]:


# Another 'Min' and 'Max' function we can use for example

Num = 12,13,46,545,453  #We have given list and we have to find min and max out of it


# In[72]:


max(Num)  #For finding max out of list


# In[74]:


min(Num)  #For finding min out of list


# ## `Dictionaries - In this we provide keys and their values. So we can easily under the any values of any assigned keys. I know just by reading it will be very difficult to understand. So for that i'll illustrate you with examples.`

# In[75]:


student = {"bob":23,"ram":34,"shyam":21,"krishna":3,"tom":43}  #Here we assigned different values and keys of bob:14. here value is their names and keys are their age. And in dictionary we always open it with curl bracket.


# In[76]:


student['bob'] #For finding the age of bob


# In[78]:


student['ram']


# ## `Functions in the dictionaries`

# In[86]:


# del function

del student[2] #Here in the dictionary we cannot delete the particular values.


# In[90]:


# If we want we can clear the whole list of the dictionary


student.clear()  


# In[91]:


student #check the list it will be cleared to zero


# In[94]:


# Function for knowing the keys and values.

student = {"bob":23,"ram":34,"shyam":21,"krishna":3,"tom":43}

student.keys() #for finding the keys


# In[95]:


student.values() #for finding the values


# In[97]:


#Function for updating on dictionary to other

student2 = {"isha":26,"gopi":53}

student.update(student2)


# In[98]:


student #updated list of the students


# ## `Tuples : We cannot 'add' or delete' in the tuple but we can slice and and know  the location of the values.`

# In[99]:


Tup = ('Raju',23,55,53,'Shyam','Radhe')

del Tup[2] #We cannot delete the tuple


# In[100]:


Tup[2]  #We can locate the values


# In[102]:


Tup[0:4] #We can slice the tuple from particular self defined path


# ## `Basics of if/else statements` 

# In[107]:


# Lets print some easy and basic codes


if 12>32:                                # In this we put if and else statement to print our output
    print("My name is bob")
else:
    print("My name is Rishabh Tiwari")


# ## `Relational Operators`

# In[109]:


4>2 # It will tell us weither it is true or false


# In[110]:


2>4


# In[111]:


21>=34


# In[112]:


21>=12


# In[113]:


21>=21


# In[117]:


4!=5          # 4 is not equal to "!" used to for "is not".


# In[116]:


4!=4


#    ## `Nested  if/else`

# In[120]:


# Lets make code for eligibilty of facebook user for using facebook

Myage = 18                                              # Assume my age is 18
if age>15:
     print("You're eligible for using the facebook")    # If am over 15 then i'll eligible for facebook
Myname = "Rishu"                                        # Assume my name is Rishu
if Myname =="Rishu":
      print("You're eligible and you'll get special privillages")    # We assign one more conditon that my must be Rishu for getting special privillages
else:
    print("You're not elligible for facebook")


# ## `Elif`

# In[2]:


# Elif is the third kind of the function which we can use with if and else.

day = "Monday"                                   # Assume day is monday
if day == "Monday":
    print("It's a very sunny day")
elif day == "Tuesday":
    print("It's a very hot day")
else:
    print =("It's a rainy day")


# ## `Logical operators`

# In[6]:


# In the logical operator we will check 'or' logic in the coding.

Myage = 25
Myname = "Rishu"
if Myage== 25 or Myname == Rishu:
    print("The logical opertor is successfully done")
else:
    print("Logical operator fail to satisfy")


# ## `For loops`

# In this code is done again and again untill condtion is being become false and loops stops.

# In[7]:


for i in range(0,5):             # for  example printing no. from 0 - 4
    print(i)


# In[8]:


Slist = ["Cake","Coffee","Milk","Curd","Banana"]
for i in Slist:
    print(i)


# In[12]:


Slist = ["Cake","Coffee","Milk","Curd","Banana"]
for i in Slist:
    print(i)


# In[13]:


# For listing number 0-10 with interval of 2 we code in following way:

for i in range(0,11,2):
    print(i)


# ## `While loop`

# In[14]:


# printing number from 5 to 9 using while loop

Num = 5
while Num <10:
    print(Num)
Num = Num+1


# ## `Nested for loop`

# In[26]:


# Printing 0 to 5 numbers  5 times

for i in range(0,4):      #Command for print is 4 times
    for a in range(0,3):  #Command for range of printing between 0-2
        print(a)
        


# ## `Pass, Break and Continue`

# In[3]:


counter = 0
while counter<100:
    if counter == 4:
        break
counter = counter+1
# This code is for breaking the function at the specified digit use this in the python you'll get the results.   


# In[ ]:


counter = 10
while counter<100:
    if counter == 15
    break
    else:
        pass
    print(counter)
    counter = counter+1
    
# This code is for giving condition that if counter ==15 then pass or else print number from 10-100.


# In[ ]:


for i in "PHYTHON":
    if i =="H":
        contniue
        print(i)

# In this code we are checking if the condition of i is being satisfy then i will be "continue" to be printer. Here we are applying "continue" function.        


# ## `Try and Except`

# In[3]:


try:
    if name>3:
        print("Hi")
except:
    print("Python having some error")    #Creating 'try' and 'except' code


# ## `Creating own Function`

# Funtion is used for defining the function name and parameter. If there is no parameter leave that bracket empty.

# In[14]:


def functionname():
    for i in range(0,5):
        print("Hi")


# In[15]:


functionname()


# `This is how we can create our own function and the we can define it's range according to our requirements.`

# In[18]:


def addNum(Rishabh,Tiwari):
    return(Rishabh+Tiwari)
addNum(45,3)


# `Here you can see first we define the alpha and 'return' what we want to do with it, like addition here and then we given command for two numbers 45,3 where we get the result as per our choise.`

# In[19]:


def my(abc,cde):
    return(abc/cde)
my(120,3)


# `Here again i try to guide you with an example that how we can use function to define it in our own requirements. We can name function as per our choise and also we can define our parameters accordingly to it.`

# ## `GLOBAL AND LOCAL VARIABLES`

# In[27]:


total =  10                  #This is a global variable
def multiply(num1,num2):
    total= (num1*num2)       #This is a local variable
    return total


# In[28]:


multiply(100,2)


# ## `ABS AND BOOL`

# `'Abs' are used for coverting the negative values to positive.`
# `'Bool' are used for finding the number 0 or none, as when they come bool will turn to 'false' else it will be 'true' all time.`

# In[29]:


abs(-101)


# In[30]:


abs(-20)


# In[31]:


abs(20)


# In[32]:


bool(0)


# In[33]:


bool(101)


# In[34]:


bool()


# In[35]:


bool(27)


# ## `dir function`

# In[40]:


dir (["abcdef"])   #Here it shows which functions we can use.


# ## `Eval`

# In[48]:


eval(print("Hello"))    #Used for evaluating the function


# In[50]:


eval ("5253+365")   #Used for evaluation


# ## `Stri(), int(), float()`

# `We are going to make a facebook form which basically check weither you're eligible for using facebook or not. In this program we are going to use 'stri','int' and'float' functions.`

# In[107]:


age = input ("age: ")
if int(age)>15:
    print("You're eligible for facebook")
else:
    print("You'r not eligible for facebook")


# ## `Objected oriented programming`

# `Basics of classes`

# In[38]:


class Students:
    def __init__ (self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


# In[40]:


Student1 = Students("ash",26,12)       


# In[41]:


Student1.name


# In[42]:


Student1.age


# In[43]:


Student1.grade


# ## `Functions in Classes`

# In[25]:


class Students:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def displayStudents(self):
        return("Student name is" " "+ self.name +" " "and age is " +str(self.age))


# In[28]:


Stu = Students("Rishabh",26)


# In[29]:


Stu.displayStudents()


# ## `Classes Attribute`

# In[47]:


class Students:
    def __init__ (self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    
Student1 = Students("Rishu",25,12)
Student2 = Students("Bob",30,12)


# In[49]:


hasattr(Student1,"age")  #This attribute is used for checking the truthness.


# In[51]:


getattr(Student2,"grade") #This attribute is used for getting any specific item like "Grade","Name,"Age".


# In[52]:


delattr(Student1,"grade") #This attribute is for deleting the any specific item.


# In[55]:


Student1.age


# In[57]:


Student1.grade


# `As we already deleted the grade attribute that's why now it is showing error.`

# In[59]:


hasattr(Student1,"grade") #We can check like this also.


# ## `Inheritance`

# `In this we will make two classes 'parent' and 'child' and we will interlinked them with the functions.`

# In[102]:


class parent:
    counter=10                                               
    def __init__ (self):
        print("Class initialized")
    def parentfunc(self):
        print("Parent function is initialized")
    def setcounter(self,num):
        parent.counter = num
    def showcounter(self):
        print(str(parentcounter))
class child(parent):
    def __init__(self):
        print("Child function is being intialized")
    def childfunc(self):
        print("Child function is being is intialized")


# In[103]:


c = child()                        #for finding the child function


# In[104]:


c.childfunc()                      #for finding the child function


# In[105]:


c.parentfunc()                     #for finding the parent function  


# In[106]:


c.counter                          #for finding the counter


# In[107]:


c.setcounter(20)                   #for setting up the counter


# ## `Random Module`

# `Randint : It genertae random number between defined range.`

# In[112]:


import random


# In[115]:


print(random.randint(0,10))


# `Above example show how we can print random number between the defined range.`

# ## `Let's make a Guessing Game`

# In[ ]:


import random
CompGuess = random.randint(0,100)
while True:
    UserGuess = int(input("Guess the number between 0-100: "))
    if UserGuess>CompGuess:
        print("Guess lesser number")
    elif UserGuess<CompGuess:
        print("Guess higher number")
    else:
        print("Congratulations you guessed the correct number")
    


# ## `Creating a file`

# `Go to notepad and make a file in it and save it in the PC.`

# ## `Reading the file`

# `Now open the file which you created using the notepad.`

# In[9]:


file1 = open("C:\\Users\\rishu\\OneDrive\\Desktop\\mytestfile.txt","r")  # Always remember put double slash in the path section


# In[8]:


file1.read()


# ## `Writing the file`

# `In this we have to write in the file we have created by using the write function and then afterwards we read the same.`

# In[12]:


f = open("mytestfile","w")`


# In[14]:


f.write("I have to check weither my text are added in the list or not \nlet's see the result")


# In[15]:


f.close()


# In[16]:


f = open("mytestfile","r")


# In[17]:


f.read()


# ## `Appending the file`

# `Here we will append the file using the append funnction and lastly we will check weither file is being appended or not,`

# In[24]:


f = open("C:\\Users\\rishu\\OneDrive\\Desktop\\mytestfile.txt","a")


# In[25]:


f.write("\n In this we are checking by appending the file")


# In[26]:


f = open("C:\\Users\\rishu\\OneDrive\\Desktop\\mytestfile.txt","a+")


# `"+a" this function gives a outcome of reading and writing the file both.`

# In[29]:


f.write("\n In this we are checking the appending of the file")


# In[32]:


f = open("C:\\Users\\rishu\\OneDrive\\Desktop\\mytestfile.txt")


# In[33]:


f.read()


# ## `Shuffle and choise`

# `For generating random item from the list we have generated.`

# In[66]:


import random
food = ["Grapes","Banana","Maggi","Milk","Bread"]
print(random.choice(food))


# In[74]:


# For shuffling the list we use the shuffle.

import random
food = ["Grapes","Banana","Maggi","Milk","Bread"]
random.shuffle(food)


# In[75]:


food


# `You can see that how the list is being shuffled.`

# ## `Sys Module`

# `Sys module is same as giving an input and getting appro[priate output accordingly. This module is just for information in actually we are not going to use it much.`

# In[88]:


import sys

inputStatement = sys.stdin.readline()
'This sentence going we are going to print'


# In[89]:


sys.stdout.write("This we are going to write")


# In[91]:


sys.version


# ## `Time module`

# `In the time module we are going to know the time for execution of our code.`

# In[93]:


import time
time.time()


# In[107]:


time.asctime()


# In[122]:


import time
def numbers(max):
    time1 = time.time()
    for i in range(0,max):
            print(i)
    time2= time.time()
    print(str(time2-time1))


# In[126]:


numbers(50)  # This program will show actual time of running the code


# In[129]:


time.asctime()


# In[141]:


tup = (1995,10,7,9,30,0,5,0,0) # format (year,month,day,hour,min,seconds,day of week and lastly day=1,night=0)
                               # for writting your birthday and time


# In[142]:


time.asctime(tup)


# In[143]:


time.localtime()


# In[144]:


t = time.localtime()


# In[145]:


year = t[0]


# In[146]:


day = t[2]


# In[147]:


month = t[1]


# In[148]:


print (year)


# In[149]:


print(day)


# In[150]:


print(month)


# `This is how you can take out the time from given local time.`

# `For slowing down the the code wem can use "time.sleep function".`

# In[154]:


for i in range(0,5):
    print(i)
    time.sleep(1) # This will tell give command that how much seconds delay we want in the code.


# ## `Turtle module`

# In[8]:


from mobilechelonian import Turtle

t = Turtle()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)  # This is how you can make any shape in the turtle


# ## `For loop in Turtle`

# In[12]:


from mobilechelonian import Turtle
t = Turtle()
for i in range(0,8):
    t.forward(60)
    t.left(90)   


# In[13]:


from mobilechelonian import Turtle
t = Turtle()
for i in range(1,38):
    t.forward(100)
    t.left(175)


# In[14]:


from mobilechelonian import Turtle
t = Turtle()
for i in range(1,20):
    t.forward(300)
    t.left(150)


# `Everthing is printed above figure as per our instructions.`

# ## `Re Module`

# In[49]:


import re


# In[50]:


dir(re)


# In[54]:


string = "The night is cold and dark"


# In[65]:


re.search("night",string)


# `Here we can search the span location of the particular module called "re".So whenever you are searching for the particular object used re module.`

# In[67]:


m = re.search("night",string)  
print(m)


# In[69]:


start = m.start()
end = m.end()
print(start)


# In[70]:


print(end)


# `This is how  you can search your start and end positon of the particular attribute.`

# In[72]:


string[start:end]


# ## `Crawling the web (Stock)`

# `In web crawling we will extract data from stock website using python programming and use that data accordingly to our need.`

# ### `Crawling of FB STOCK and using it for our use.`

# In[8]:


import re    
import urllib.request


# In[9]:


url = ("https://www.google.com/finance/quote/")


# In[10]:


stock = input ("Enter your stock name: ")


# In[11]:


url = url + stock


# In[12]:


print(url)


# In[13]:


data = urllib.request.urlopen(url).read()


# In[14]:


data1 = data.decode("utf-8")


# In[15]:


print(data1)


# In[122]:


m = re.search('div class="YMlKec fxKbKc"',data1)


# In[19]:


print(m)


# In[20]:


start = m.start()


# In[26]:


end = start + 35


# In[27]:


newString = data1[start:end]


# In[28]:


print(newString)


# In[29]:


m = re.search("YMlKec fxKbKc",newString)


# In[30]:


print(m)


# In[32]:


start = m.end()


# In[33]:


newString2 = newString[start:]


# In[34]:


print(newString2)


# In[35]:


m = re.search('">',newString2)


# In[36]:


start = m.end()


# In[38]:


newString3 = newString2[start:]


# In[39]:


print(newString3)


# In[44]:


print("The value of" " "+ stock +" " "is"" "+ newString3)


# ### `Crawling of GOOGLE STOCK and using it for our purpose`

# In[48]:


import re
import urllib.request


# In[49]:


url = ("https://www.google.com/finance/quote/")


# In[50]:


stock = ("GOOG:NASDAQ")


# In[51]:


url = url + stock


# In[52]:


data = urllib.request.urlopen(url).read()


# In[55]:


data1 = data.decode("utf-8")


# In[56]:


print(data1)


# In[66]:


m = re.search('div class="YMlKec fxKbKc"',data1)


# In[67]:


print(m)


# In[68]:


start = m.start()


# In[76]:


end = m.start() + 35


# In[77]:


data2 = data1[start:end]


# In[78]:


print(data2)


# In[91]:


m = re.search("YMlKec fxKbKc",data2)


# In[92]:


print(m)


# In[94]:


start = m.end()


# In[95]:


data3 = data2[start:]


# In[96]:


print(data3)


# In[98]:


m = re.search(">",data3)


# In[99]:


print(m)


# In[100]:


start = m.end()


# In[101]:


data4 = data3[start:]


# In[102]:


print(data4)


# In[104]:


print("The value of" " " + stock + " " "is" + " " + data4)


# In[105]:


import re
import urllib.request


# `For crawling stock of ALI BABA and printing it for our use.`

# In[106]:


url = "https://www.google.com/finance/quote/"


# In[107]:


stock ="BABA:NYSE"


# In[108]:


url = url + stock


# In[109]:


data = urllib.request.urlopen(url).read()


# In[120]:


data1 = data.decode("utf-8")


# In[121]:


print(data1)


# In[189]:


m = re.search('div class="YMlKec fxKbKc"',data1)


# In[190]:


start = m.start()


# In[191]:


end = m.start() + 33


# In[192]:


data2 = data1[start:end]


# In[193]:


print(data2)


# In[208]:


m = re.search("YMlKec fxKbKc",data2)


# In[209]:


start = m.end()


# In[210]:


data3 = data2[start:]


# In[211]:


print(data3)


# In[212]:


m = re.search('">',data3)


# In[213]:


start = m.end()


# In[214]:


data4 = data3[start:]


# In[215]:


print(data4)


# In[217]:


print("Value for the stock" " " + stock + " ""is" " " + data4)


# ### `Crawling of TWITTER STOCK and using it according to our uses.`

# In[218]:


import re
import urllib.request


# In[219]:


url = "https://www.google.com/finance/quote/"


# In[220]:


stock = "TWTR:NYSE"


# In[221]:


url = url + stock


# In[223]:


data = urllib.request.urlopen(url).read()


# In[224]:


data1 = data.decode()


# In[225]:


print(data1)


# In[226]:


m = re.search('div class="YMlKec fxKbKc"',data1)


# In[227]:


print(m)


# In[228]:


start = m.start()


# In[235]:


end = m.start() + 32


# In[236]:


data2 = data1[start:end]


# In[237]:


print(data2)


# In[238]:


m = re.search('YMlKec fxKbKc">',data2)


# In[239]:


start = m.end()


# In[240]:


data3 = data2[start:]


# In[241]:


print(data3)


# In[242]:


print("The value of stock of" " "+ stock + " " "is" " " + data3)


# ## `Crawling of Web (Weather)`

# `In this we will extract data from the weather website using web crawling`

# In[1]:


import re
import urllib.request


# In[2]:


url = "https://www.weather-forecast.com/locations/"


# In[3]:


location = "Kalyan"


# In[4]:


url = url + location


# In[5]:


data = urllib.request.urlopen(url).read()


# In[10]:


data1 = data.decode("utf-8")


# In[11]:


print(data1)


# In[12]:


m = re.search('<span class="phrase"',data1)


# In[13]:


print(m)


# In[14]:


start = m.start()


# In[36]:


end = m.start() + 127


# In[37]:


data2 = data1[start:end]


# In[38]:


print(data2)


# In[39]:


m = re.search('<span class="phrase">',data2)


# In[40]:


start = m.end()


# In[41]:


data3 = data2[start:]


# In[42]:


print(data3)


# ## `Beautiful soup - Prettify`

# `The prettify() method will turn a Beautiful Soup parse tree into a nicely formatted Unicode string, with a separate line for each tag and each string.`

# In[61]:


from bs4 import BeautifulSoup


# In[64]:


soup = BeautifulSoup("<html><p>asdasdasd<string>Hello<a>hello<html>","html.parser")


# In[65]:


soup.prettify()


# In[69]:


soup


# ### `Drilling Down`

# In[81]:


html_doc = ("<html><body><h2>An Unordered HTML List</h2><ul><li>Coffee</li> <li>Tea</li><li>Milk</li></ulr><h2>An Ordered HTML List</h2><ol><li>Coffee</li><li>Tea</li><li>Milk</li></ol> </body></html>")


# In[82]:


from bs4 import BeautifulSoup     # Importing Beautiful soup


# In[86]:


soup = BeautifulSoup(html_doc,"html.parser")


# In[87]:


soup  #Ugly looking html code


# In[88]:


soup.prettify()


# In[91]:


soup.body()  # It is help to find the body in the html code


# In[94]:


soup.find_all("li")  # So by this we can find out all html list present in whole code


# In[95]:


array = soup.find_all("li")


# In[96]:


array[1]


# `By above ways we can also find the location appropriate arrays in the whole html list.`

# In[124]:


import requests
from bs4 import BeautifulSoup


# In[125]:


data = requests.get('https://www.weather-forecast.com/locations/Mumbai/forecasts/latest')


# In[126]:


soup = BeautifulSoup(data.text,"html.parser")


# In[134]:


print(soup)


# In[135]:


data1 = soup.find('</div><p class="b-forecast__table-description-content"')


# In[136]:


print(data)


# `So above way we can get appropriate output using html code.`

# In[ ]:




