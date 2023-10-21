#!/usr/bin/env python
# coding: utf-8

# # Part 1 : Python Basics

# ## What is Python ?
Python is a clear and powerful object-oriented programming language, comparable to Perl, Ruby, or Java. 
Python is a programming language that combines features of C and Java. Features:-
Easy to Learn
High Level Language
Interpreted Language
Platform Independent 
Procedure and Object Oriented
Huge Library
Scalable

Application for Python:-
Web Application - Django, Pyramid, Flask, Bottle
Desktop GUI Application – Tkinter
Console Based Application
Games and 3D Application
Mobile Application
Scientific and Numeric
Data Science
Machine Learning - scikit-learn and TensorFlow
Data Analysis - Matplotlib, Seaborn
Business Application
# ## Identifier
An identifier is a name having a few letters, numbers and special characters _ (underscore). 
It should always start with a non-numeric character. 
It is used to identify a variable, function, symbolic constant, class etc. 
Ex : - 
	X2
	PI
	Sigma
	matadd
	full_name
Python is case sensitive programming language.
	d is not equal to D
	t is not equal to T
	FARUK is not equal to faruk
	FaruK is not eqaul to Faruk
# ## Keywords or Reserved Words:-

# In[1]:


# Python language uses the following keywords which are not available to users to use them as identifiers.
import keyword
print(keyword.kwlist)


# ## Variable
In Python, a variable is considered as tag that is tied to some value. Python considers value as objects. 
e.g. a = 10          Since value 10 becomes unreferenced object, 
                     it is removed by garbage collector.
     a = 20                

Rules:-
Every variable name should start with alphabets or underscore (_).
No spaces are allowed in variable declaration.
Except underscore ( _ ) no other special symbol are allowed in the middle of the variable declaration
A variable is written with a combination of letters, numbers and special characters _ (underscore)
No Reserved keyword
# ## Operators
An operator is a symbol that performs an operation.

Types of Operator:-
Arithmetic Operators                           
Relational Operators / Comparison Operators    
Logical Operators                             
Assignment Operators                                            
Bitwise Operators                              
Membership Operators                          
Identity Operators                             
# In[2]:


# Arithmetic Operators:-

# Addition
# print(4+2)
a = 4
b = 2
total = a + b
print(total)

# Subtraction
#print(8-2)
a = 4
b = 2
total = a - b
print(total)

# Multiplication
#print(4*2)
a = 6
b = 3
value = a * b
print(value)

# Divison
#print(4/2)
a = 4
b = 2
value = a / b
print(value)
print(type(value))

# Modulus
#print(5%2)
a = 5
b = 2
value = a % b
print(value) 

# Exponent
#print(5**2)
a = 5
b = 2
value = a**b
print(value)

# Floor Division Positive
#print(5//2)
a = 5
b = 2
value = a//b
print(value)

# Floor Division Negative
#print(-5//2)
a = -5
b = 2
value = a//b
print(value)


# In[3]:


# Relational Operators / Comparison Operators:- 

#print(5<2)
a = 5
b = 2
value = a < b
print(value)

#print(5>2)
a = 5
b = 2
value = a > b
print(value)

#print(5<=2)
a = 5
b = 2
value = a <= b
print(value)

#print(5>=2)
a = 5
b = 2
value = a >= b
print(value)

#print(5==2)
a = 5
b = 2
value = a == b
print(value)

#print(5!=2)
a = 5
b = 2
value = a != b
print(value)


# In[4]:


# Logical Operators-                             
#Logical and
a = 5
b = 2
c = 3
d = 200

print("******* Logical and *******")
print(a>b and a>c)
print(a>b and a<c)
print(a<b and a>c)
print(a<b and a<c)
print(a>b and c)
print(a>b and c and d)
print(a<b and c)
print(a<b and c and d)

#Logical or
print("******* Logical or *******")
print(a>b or a>c)
print(a>b or a<c)
print(a<b or a>c)
print(a<b or a<c)
print(a>b or c)
print(a>b or c or d)
print(a<b or c)
print(a<b or c or d)

#Logical not
print("******* Logical not *******")
print(not(a<b))
print(not(a>b))


# In[5]:


# Assignment operators
a = 10
b = 20
m = 15

y = a + b
print(y)

m+=10
print(m)

m-=10
print(m)

m*=10
print(m)

m/=10
print(m)

m%=10
print(m)

m**=2
print(m)

m//=10
print(m)
                                     


# In[6]:


# Bitwise Operators                              
a = 10  #0000 1010
b = 15  #0000 1111

print('~a = ', ~a)
print('a&b = ', a&b)
print('a|b = ', a|b)
print('a^b = ', a^b)
print('a<<2 = ', a<<2)
print('a>>2 = ', a>>2)


# In[7]:


# Membership Operators                          
# in
st1 = "Welcome to dubai Habibi"
print("to" in st1)

st2 = "Welcome to dubai Habibi"
print("top" in st2)

st3 = "Welcome to dubai Habibi"
print("srk" in st3)

# not in

print("to" not in st1)

print("top" not in st2)

print("srk" not in st3)


# In[8]:


# Identity Operators
# is
a = 10
b = 10
print(a is b)

a = 10
b = '10'
print(a is b)

# is not
a = 10
b = 10
print(a is not b)

a = 10
b = '10'
print(a is not b)


# ### Operator Precedence and Associativity
The computer scans an expression which contains the operators from left to right and performs only one operation at a time. 
The expression will be scanned many times to produce the result. 
The order in which various operations are performed is known as hierarchy of operations or operator precedence. 
Some of the operators of the same level of precedence are evaluated from left to right or right to left. 
This is referred to associativity.

Sequence of operations:-
    
Parentheses                                ()
Exponentiation                             **
Unary Plus, Unary Minus, Bitwise Not       +, -, ~
Multiplication                             *
Division, Floor Division, Modulus          /, //, %
Addition                                   +
Subtraction                                -
Bitwise Left Shift, Bitwise Right Shift    <<, >>
Bitwise AND                                &
Bitwise XOR                                ^
Relational Operators                       >, >=, <, <=, ==, !=
Assignment Operators                       =, %=, /=, //=, -=, +=, *=, **=
Identity Operators                         is, is not
Membership Operators                       in, not in
Logical NOT                                not
Logical OR                                 or
Logical AND                                and
# In[9]:


# ex.
value = (1+1)*2**4//3+4-1  #Parentheses
        #2*2**4//3+4-1     #Exponentiation
        #2*16//3+4-1       #Multiplication
        #32//3+4-1         #Division, Floor Division, Modulus
        #10+4-1            #Addition 
        #14-1              #Subtraction
        #13
value        


# ## Datatype
Datatype represents the type of data stored into a variable or memory.

Type of Data type :-
Built-in Data type-
1.None Type
2.Numeric Types 
3.Sequences Types 
4.Sets Types 
5.Mappings Types 

User Defined Data type :-
1.Array
2.Class
3.Module
# ### Built-in Datatype

# ### 1.None Type
None datatype represents an object that doesn’t contain any value.
# ### 2.Numeric Type / Number
Following are the Numeric Data type:-
a.Int
b.Float
c.Complex  
# #### a.Int
Int – The int datatype represents an integer number. An integer number without any decimal point or fraction part. 
In Python, It is possible to store very large integer number as there is no limit for the size of an int datatype.
Ex:- 
20, 10, -50, -1002
y = 10
pin_code = 564512
# #### b.Float
Float – The float data type represents floating point numbers. 
A floating point number is a number that contains a decimal point.
Ex:- 
25.56, 10.5, -45.69, -0.8
price = 25.56
run_rate = -0.8
value = 5.1e5
# #### c.Complex
Complex – A complex number is a number that is written in the form of a + bj or a + bJ. Where,
a = Real Part of the number
b = Imaginary part of the number
j or J = Square root value of -1
a and b may contain integer or float number.
Ex:- 5+7j, 0.8+2j
com = 5+7j
# ### 3.Bool type
The bool datatype represents boolean value True or False. 
Python internally represents True as 1 and False as 0.
Ex:- True, False
True + True = 2
True – False = 1
# ### 4.Sequence Type
Following are sequence type:- 
a.String
b.List
c.Tuple
d.Range
# a.String
String – String represents group of characters. 
         Strings are enclosed in double quotes or single quotes. 
         The str data type represents a String.

Ex:- “Hello”, “world”, ‘faruk’
# In[10]:


print(dir(str),end="")


# b.List
List – A list represents a group of elements. A list can store different types of elements which can be modified. 
Lists are dynamic which means size is not fixed. Lists are represented using square bracket [ ].

Ex:-  data = [10, 20, -50, 21.3, 'faruk']
# In[11]:


print(dir(list),end="")


# c.Tuple
Tuple – A tuple contains a group of elements which can be different types. 
It is similar to List but Tuples are read-only which means we can not modify it’s element. 
Tuples are represented using parentheses ( ).

Ex:- data = (10, 20, -50, 21.3, 'faruk')
# In[12]:


print(dir(tuple),end="")


# d.Range
Range – Range represents a sequence of numbers. 
The numbers in the range are not modifiable.

Ex:- rg = range(5) 		0 1 2 3 4 
rg = range(10, 20, 2)	10 12 14 16 18
# In[13]:


print(dir(range),end="")


# ### 4.Sets Types 
A set is an unordered collection of elements much like a set in mathematics. 
The order of elements is not maintained in the sets. 
It means the elements may not appear in the same order as they are entered into the set. 
A set does not accept duplicate elements. 
Sets are unordered so we can not access its element using index.
Sets are represented using curly brackets { }.
Ex:- 
data = {10, 20, 30,  "FARUK", “srk”, 40}
data = {10, 20, 30,  "FARUK", “srk”, 40, 10, 20}
# In[14]:


print(dir(set),end="")


# ### 5.Mapping Type/ dict / Dictionary
A map represents a group of elements in the form of key & value pairs.

Ex:- 
data = {101: ‘Rahul’, 102: ‘Raj’, 103: ‘Simran’ }
data = {‘rahul’:2000, ‘raj’:3000, ‘simran’:8000, }
# In[15]:


print(dir(dict),end="")


# ## Type Conversion
Converting one data type into another data type is called Type Conversion. 
Type of Type Conversion:-
Implicit Type Conversion 
Explicit Type Conversion

Implicit Type Conversion
In the Implicit type conversion, python automatically converts one data type into another data type.
# In[16]:


# Implicit Type Conversion Ex:- 
a = 5
b = 2
value = a / b
print(value)
print(type(value))

x = 10
y = 5.5
total = x + y 
print(total)
print(type(total))

j = "Hello"
k = "Faruk Mulani"
p = j + k
print(p)
print(type(p))

Explicit Type Conversion
In the Cast/Explicit Type Conversion, Programmer converts one data type into another data type.
int (n)
float (n)
complex (n) 
complex (x, y) where x is real part and y is imaginary part
str (n)
list(n)
tuple(n)
bin (n)
oct (n)
hex (n )
# In[17]:


# ex of Explicit Type Conversion:-
# String to Integer
q = 20
u = '10'
print(type(u))
r = q + int(u)
print(r)

# Float to Integer
n1 = 10.36
vn1 = int(n1)
print(vn1)
print(type(vn1))

# Integer to Float
n2 = 10
vn2 = float(n2)
print(vn2)
print(type(vn2))

# Integer to Complex
n3 = 10
vn3 = complex(n3)
print(vn3)
print(type(vn3))

# Integer to String
n4 = 10
vn4 = str(n4)
print(vn4)
print(type(vn4))

# String to Tuple
n5 = "farukmulani"
vn5 = tuple(n5)
print(vn5)
print(type(vn5))

# Tuple to List
n5 = ("Rahul", "pathan", "SRK", "jawan")
vn5 = list(n5)
print(vn5)
print(type(vn5))


# In[ ]:




