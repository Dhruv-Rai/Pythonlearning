# Strings are immutable and when u change then the original do not change but a new version of it is formed
a="!!D hru v!!!"
print(a.upper())
print(a.lower()) #True when all character is lower
print(a.rstrip('!')) #Removes given character by rear
print(a.replace('Dhruv','Harry'))
print(a.split(" "))
blog="dhruv iS The best"
print(blog.capitalize())
str1 ="Welcome To The Console"
print(len(str1))
print(len(str1.center(50)))
print(str1.count("console"))
print(str1.endswith("!!!"))
print(str1.endswith("to", 4,10))
str="he's name is Dan. He is an honest man"
print(str.find('is')) # returns -1 if the string is not found
print(str.index('n')) # index function throws an error if the string is not found
print(str1.isalnum()) # True when entire string conatains only A-Z,a-z,0-9
print(str1.isalpha()) # True when entire string conatains only A-Z,a-z
print(str1.islower()) # True if all the charcter in the string are lower
print(str1.isprintable()) # true if all the character are printable(\n,\ etc is not printable)
print(str1.isspace()) # True only if the String has only spaces
print(str1.istitle()) #  True only if the first letter of the word is capitalized
# isUpper is exactly as islower
print(str1.startswith("Welcome"))
print(str1.title())
