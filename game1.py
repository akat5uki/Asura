import random

class Bots:
    #ID = random.randint(5000,9000)
    def __init__(self):
        self.flag=1
        self.hitPoint = 100
        self.power = random.choice(['air','water','fire','earth'])
        self.ID = random.randint(5000,9000)
        
    def hits(self):
        self.points = random.randint(8,16)
        if self.points<self.hitPoint:
            self.flag = 1
            self.hitPoint -= self.points
        else:
            self.hitPoint = 0
            self.flag = 0
            
    def DoA(self):
        if self.flag==1:
            return 1
        else:
            return 0
            
class User(Bots):
    #ID = random.randint(5000,9000)
    def __init__(self,name):
        self.name = name
        Bots.__init__(self)
        
if __name__=='__main__':
    name = input('Enter your name : ')
    objBot = Bots()
    objUser = User(name)
    if objBot.ID == objUser.ID :
        objBot.ID -= 1
    print("Bot's power : {}".format(objBot.power))
    print("{}'s power : {}".format(objUser.name,objUser.power))
    
    while objBot.DoA()==1 and objUser.DoA()==1:
        turn = random.choice([objBot.ID,objUser.ID])
        if turn == objUser.ID:
            objBot.hits()
            print('{} attacks Bot\t\tUser Life : {}\tBot Life : {}'.format(objUser.name,objUser.hitPoint,objBot.hitPoint))
        else:
            objUser.hits()
            print('Bot attacks {}\t\tUser Life : {}\tBot Life : {}'.format(objUser.name,objUser.hitPoint,objBot.hitPoint))
    if objBot.hitPoint == 0:
        print('*** You Win ***')
    else:
        print('*** You Lost ***')
        
    print('Temperory Bot ID : {}'.format(objBot.ID))
    print('Temperory User ID : {}'.format(objUser.ID))