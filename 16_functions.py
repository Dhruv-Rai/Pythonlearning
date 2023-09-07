def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)  
def isGreater(a,b): # PASS does not throws an error if nothing is defined
    if(a>b):
     print("First is greater")
    else:
       print("Second is Greater")
a=9
b=8
#gmean=(a*b)/(a+b)
#print(gmean)
calculateGmean(a,b)
c=8
d=7
#gmean2=(c*d)/(c+d)
#print(gmean2)
calculateGmean(c,d)