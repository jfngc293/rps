import random
a=int(input("Enter the goddamn score"))
u=0
c=0
for i in range (0,a) :
    print("1.Rock 2.Paper 3,Scissor")
    x=int(input("Enter your option :    "))
    y=random.choice([1,2,3])
    print("You : ",x)
    print("Computer  :",y)
    if (x==1 and y==3):
        u+=1
    elif (x==2 and y==1):
        u+=1
    elif (x==3 and y==2):
        u+=1
    elif  (x==y):
        continue
    else :
        c+=1

if (u>c):
    print("You Win")
else :
    print("Computer win you lose")
print ("Your SCORE  :",u)
print("COMP Score  :",c)
