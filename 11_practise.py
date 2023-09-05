import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=int(time.strftime('%H'))
print(timestamp)
timestamp=int(time.strftime('%M'))
print(timestamp)
timestamp=int(time.strftime('%H'))
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
if(timestamp<12):
   print("Good Morning Sir")
elif(timestamp>12 and timestamp<17):
     print("Good Afternoon Sir")
else:
     print("Good Evening Sir")
    
#needs improvement