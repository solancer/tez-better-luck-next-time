
import random

price1 =100
wins1  =5

price2 = 50
wins2  = 10

price3 = 10
wins3  = 100

Price4 = 5
wins4  = 200

Draws = 5000

quotaprice1 = 0
quotaprice2 = 0
quotaprice3 = 0
quotaprice4 = 0

for x in range(0, 3000):
    luckyNum = int(random.random() * 10000000)%Draws
    print(luckyNum)
    if(luckyNum<wins1):
        if(quotaprice1<wins1):
            quotaprice1=quotaprice1+1
            print(str(luckyNum)+"Prize1 "+str(quotaprice1))
        else:
            print("FO")
    elif(luckyNum<(wins1+wins2)):
        if(quotaprice2<wins2):
            quotaprice2=quotaprice2+1
            print(str(luckyNum)+"Prize2 "+str(quotaprice2))
        else:
            print("Betterlucknexttime")

    elif(luckyNum<(wins1+wins2+wins3)):
        if(quotaprice3<wins3):
            quotaprice3=quotaprice3+1
            print(str(luckyNum)+"Prize3 "+str(quotaprice3))
        else:
            print("Betterlucknexttime")
    
    elif(luckyNum<(wins1+wins2+wins3+wins4)):
        if(quotaprice4<wins4):
            quotaprice4=quotaprice4+1
            print(str(luckyNum)+"Prize4 "+str(quotaprice4))
        else:
            print("Betterlucknexttime")


print (quotaprice1, quotaprice2, quotaprice3, quotaprice4)
