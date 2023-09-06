i=int(input("Enter the number: "))
while(i<38):
    i=int(input("Enter the number: "))
    print(i)
print("Done with the loop")
count=5
while(count>0):
    print(count)
    count=count-1
else:
    print("I an inside else")
# emulating do while- loop body at least emulates 1 time even if condition is false
i=0
while True:
  i=i+1
  if(i%100==0):
    break
    
