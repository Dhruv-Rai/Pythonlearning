# String Formatting in Python
letter = "hey my name is {} and i am from {}"
country="India"
name="Dhruv"
print(letter.format(name,country))
print(f"hey my name is {name} and i am from {country}")
print(f"We use f-Strings like this:hey my name is {{name}} and i am from {{country}}") # if you want to show raw f-sting in output.
price=49.0999
txt=f"For only {price:.2f} dollars"
print(txt)
#print(txt.format(price=49.0999))
print(type(txt))