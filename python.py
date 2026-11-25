"""a=10
print(a)"""


"""print(bool(1.0))"""


"""a=6j
print(a)"""

"""
a='Good_Morining'
print(a)"""

"""List """
'''a=[10,20,30,True,"Hello"]
a.append(10)
print(a)
a.remove(10)
print(a)'''

'''import keyword
print(keyword )'''


"""#tuple#    (,)
a=(10,)
print(a,type(a))

#set#   no duplicate sets are allowed
a={1,2,3}
print(a)

#dictonary#    
a={'a':10,'b':20}
a['c']=30
print(a)"""

'''a={'a':[10,20,30],'b':40}
print(a['a'][1])'''
'''
a={'a':[10,20,30],'b':40}
print(a['a'][-2])'''

'''a="Hello"
print(a[2:3+1:1])'''

'''a="GoodMorning"
print(a[7:10+1:1])'''

'''a="GoodMorning"                                       #
print(a[-5:10+1+2])'''

'''a="Hello"
print(a[3:1:-1])
print(a[-2:-5:-1])
print(a[::-1])'''

'''a="Good Morning"'''
'''print(a[1:5+1:2])'''

"mn"
'''print(a[5::3])'''
'''print(a[-7::3])
print(a[-5::3])'''

'''print(a[10:4-1:-3])'''

'''a=int(input("Enter the number:"))
print(a,type(a))'''

'''a=list(input("Enter the number"))
print(a,type(a))'''

'''a=eval(input("enter"))
print(a,type(a))'''

'''a=int(input("enter"))

if a%2==0:
    print("even")
else:
    print("odd")
    '''

'''a = eval(input("enter the list: "))
if len(a) == 5:
    print("yes")
else:
    print("no")'''

'''ch = input("Enter: ")

if "A" <= ch <= "Z":
    print("Upper")
elif "a" <= ch <= "z":
    print("Lower")
else:
    print("not an alpha")'''

'''us=input("enter:")
if us=="manu":
    pw=input("enter:")
if pw=="manu@98":
    print("sucussfull login")
else:
    print("incorrect pw")'''

#looping statements:

'''i=1
while i<=100:
    print(i)
    i+1'''
#print numbers from 1-50

'''i=1
while i<=50:
    if i%2==0:
        print(i)
    i+=1'''
#how to reverse a number

'''n=int(input("enter a number:"))
rev=0
while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
    print(rev)'''
#for loop
'''for i in range(1,100):
    print(i)'''
'''for i in range(1,100):
        print(i,"even")'''
'''l={10,20,30,40,80,9-0}
for i in l:
    print(i)'''
'''
s=input("enter:")
out=""
for i in s:
    if "A"<=i<="Z":
        out+=chr(ord(i)+32)
    elif "a"<=i<="Z":
        out+=chr(ord(i)-32)
    else:
        out+=i
print(out)'''

'''s=input("enter:")
rev=""
for i in s:
    rev=i+rev
print(rev)'''
#nested for loop

'''for i in range (1,6):
    print("*")'''
'''for i in range (1,6):
    for j in range (1,6):
        print("*",end="")
        print()'''
'''print("*")
print("**")
print("***")
print("****")'''

#htr
'''a="Happy birthday"
print(a[-4:-7:-1])'''
#function is a block of code 
#function:
#with argumentwith return

'''def convert(s):
    out = ""
    for i in s:
        if "a" <= i <= "z":
            out += chr(ord(i) - 32)
        else:
            out += i
    return out

print(convert(input("Enter a string: ")))'''
#for printing the output 
'''def convert(s):
    out = ""
    for i in s:
        if "a" <= i <= "z":
            out += chr(ord(i) - 32)
        else:
            out += i
    print(out)
    return 10


(convert(input("Enter a string: ")))'''

'''def convert():
    s = input("Enter text: ")
    out = ""

    for i in s:
        if "a" <= i <= "z":
            out += chr(ord(i) - 32)
        else:
            out += i

    return out

print(convert())'''

'''class college:
    cname="GCEM"
    cloc="hoodi"
s1=college()
print(college.cname)
college.cname="GCEM"
print(s1.cname)
print(college.cname)

print("changing college location")
s1.cloc="bangalore"
print(s1.cloc)
print(college.cloc)'''

#constructor
#for the repated menthod we use constructors 
'''class college:
    def __init__(self,name,mobile,usn):
        self.name=name
        self.mobile=mobile
        self.usn=usn
    def display(self):
        print(self.name)
        print(self.mobile)
        print(self.usn)


s1=college("manu",1234567890,"1GD25CS078")
s2=college("suprith",9876543210,"1GD25CS149")

s1.display()
s2.display()'''

'''class college:
    def __init__(self,name,mobile,usn):
        self.name=name
        self.mobile=mobile
        self.usn=usn
    def display(self):
        print(self.name)
        print(self.mobile)
        print(self.usn)
    def change_name(self,new_name):
        self.name=new_name
    def change_mobile(self,new_mobile):
        self.mobile=new_mobile


s1=college("manu",1234567890,"1GD25CS078")
s2=college("suprith",9876543210,"1GD25CS149")
s1.change_name("MRP")
s1.change_mobile(8861399851)


s1.display()
s2.display()
s1.change_name("MRP")
s1.display()
s1.change_mobile(8861399851)
s1.display()'''

#generative AI:
#Generative AI is a kind of artificial intelligence that creates new content—such as
#  text, images, music, video, or computer code
