#def average(a=9,b=1):
    #print("The average is ",((a+b)/2))
#average(5)
#def name(fname,mname='John',lname='Whatson'):
 #   print("Hello", fname,mname,lname)
#name("Amy","Agarwal","whatson")    
# Order in which arguments are passed does not matters
def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum = sum + i
        #print("Average is: ",sum / len(numbers))
        return sum / len(numbers)
#average(4,6)
#average(b=9)
c= average(5,6,7,1)
print(c)

def name(**name):
    print(type(name))
    print("Hello",name["fname"],name["mname"],name["lname"])

name(mname="buchanan", lname="Barnes",fname="James")