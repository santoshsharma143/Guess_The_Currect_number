import random
num=random.randint(1,100)
a=-1
attemps=0
while(a !=num):
    a=int(input("Guess the number : "))
    if(a<num):
        print("Think more higher number ")
        attemps +=1
    else:
        print("Think more lower number ")
        attemps +=1   
print(f"You Guessed the {num} in {attemps} attemps")