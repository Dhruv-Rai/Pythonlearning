tup=(6,23,29,37,"Dhruv",True) # when parenthesis it a tuple and square bracket is a list
 # id you are making 1 value tuple you have to have a comma at the end (1,)
 # Operation are same as list only difference is that u cannot change tuple
print(type(tup),tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
if "Dhruv" in tup:
    print("Yes Dhruv is present in Tuple")
tup2 =tup[1:4] #Range of Index
print(tup2)
countries=("Spain","Italy","India","Japan","Germany")
temp=list(countries)
temp.append('Russia')   #Add 
temp.pop(3)             #Remove
temp[2]="Finland"       #Change Item
contries=tuple(temp)
print(contries)
country=("Pakistan","Afghanistan","Bangladesh","SriLanka")
country2=("India","China","Nepal","Vietnam")
southeastAsia=country+country2
print(southeastAsia)
tuple1=(0,1,2,31,2,3,1,3,2,3)
#res=tuple1.count(3) #Counts the number of char mentioned in the tuple
#res=tuple1.index(3,4,8) # resturn the first occurance of the element
res=len(tuple1)
print("Count of 3 in tuple1 is:",res)
