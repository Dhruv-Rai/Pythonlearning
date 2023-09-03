a=50
b=3
print("the value of",a,"+",b,"is:",a+b)
print("the value of",a,"-",b,"is:",a-b)
print("the value of",a,"x",b,"is:",a*b)
print("the value of",a,"/",b,"is:",a/b)
# The conversion of one data type into the another data type is typecasting
# explicit is the type casting that the programmer do whereas the implicit one is done by python itself
string="15"
number=7
string_number=int(string) #throws an error if the string is not a valid interger
sum=string_number+number
print(sum)
# python converts a smaller data type to a larger data type to prevent data loss
c=23
d=6.5
print(c+d)