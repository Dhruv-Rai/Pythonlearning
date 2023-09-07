for j in range(12):
    if(j==10):
        print("Skip the iteration")
        continue
print("5 X ",j,"=",5*j)
for i in range(12):
    if(i==10):
        break
    print("5 X",i+1,"=",5*(i+1))
print("loop ko chod kar niakl jao")