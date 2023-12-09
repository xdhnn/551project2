# Author: Dingan Li Vamshikrishna Vithoba Challa
# Date: 12/8/2023
# Description: game Engine
import random
import Veggie
import Captain
import Rabbit
import Snake
class GameEngine:
    __NUMBEROFVEGGIES=30
    __NUMBEROFRABBITS=5
    __HIGHSCOREFILE="highscore.data"
    __x=0     #height and length of field
    __y=0
    def constructor(self):
        self.__field = []
        self.__rabbit = []
        self.__vegetable = []
        self.__captain  =None
        self.__score =0

    def intro(self): #print intro
        print("Welcome to Captain Veggie!\nThe rabbits have invaded your garden and you must harvest\nas many vegetables as possible before the rabbits eat them\nall! Each vegetable is worth a different number of points\nso go for the high score!\n\nThe vegetables are:")
        for i  in self.__vegetable:
            print(i[1]+":",i[0],i[2],"points")
        print("\nCaptain Veggie is V, and the rabbits are R's.\n\nGood luck!")

    def initVeggies(self):
        __Veggie=Veggie.Veggie
        first = 1
        while True:
            try:
                if first == 1:
                    filename = input("Please enter the name of the vegetable point file: ")
                    first = 0
                file = open(filename)
                text = file.read()
                break
            except:
                filename = input(filename + " does not exist! Please enter the name of the vegetable point file: ")
        text = text.split("\n")
        for i in range(len(text)):
            text[i] = text[i].split(",")
        text[0][1] = int(text[0][1])
        text[0][2] = int(text[0][2])
        for i in range(1, len(text)):
            text[i][2] = int(text[i][2])
        self.__vegetable=text[1::]
        self.__x=text[0][1]
        self.__y = text[0][2]
        for i in range(self.__x):
            line=[]
            for j in range(self.__y):
                line.append(None)
            self.__field.append(line)
        for i in range(self.__NUMBEROFVEGGIES):
            v=random.randint(0,len(self.__vegetable)-1)
            while True:
                x = random.randint(0, self.__x - 1)
                y = random.randint(0, self.__y - 1)
                if self.__field[x][y]==None:
                    self.__field[x][y]=self.__vegetable[v][1]
                    break
        file.close()
    def initCaptain(self):
        __Captain=Captain.Captain
        self.__busket = __Captain.getbusket(__Captain)
        while True:
            x = random.randint(0, self.__x - 1)
            y = random.randint(0, self.__y - 1)
            if self.__field[x][y] == None:
                self.__field[x][y] = __Captain.getsymbol(__Captain)
                break
    def initRabbits(self):
        __Rabbit=Rabbit.Rabbit
        for i in range(self.__NUMBEROFRABBITS):
            while True:
                x = random.randint(0, self.__x - 1)
                y = random.randint(0, self.__y - 1)
                if self.__field[x][y]==None:
                    self.__field[x][y]=__Rabbit.getsymbol(__Rabbit)
                    break
    def initSnake(self):
        __Snake = Snake.Snake
        while True:
            x = random.randint(0, self.__x - 1)
            y = random.randint(0, self.__y - 1)
            if self.__field[x][y] == None:
                self.__field[x][y] = __Snake.getsymbol(__Snake)
                break
    def initializeGame(self):
        self.initVeggies(self)
        self.initCaptain(self)
        self.initRabbits(self)
        self.initSnake(self)
    def countVeggies(self): #return count without print
        count=0
        for i in self.__field:
            for j in i:
                if j!=None and j!="V" and j!="R" and j!="S":
                    count+=1
        return count
    def remainingVeggies(self):
        count=0
        for i in self.__field:
            for j in i:
                if j!=None and j!="V" and j!="R" and j!="S":
                    count+=1
        print(count,"veggies remaining. Current score:",self.__score)
        return count
    def printField(self):
        line1=""
        for i in range(self.__y*3+2):
            line1=line1+"#"
        print(line1)
        for i in range(self.__x):
            line="#"
            for j in range(self.__y):
                if self.__field[i][j]==None:
                    line+="   "
                else:
                    line+=" "+self.__field[i][j]+" "
            line+="#"
            print(line)
        print(line1)

    def getScore(self):
        return self.__score
    def moveRabbits(self):
        ribbit=[] #save all location of rabbit
        for i in range(self.__x):
            for j in range(self.__y):
                if self.__field[i][j]=='R':
                    ribbit.append([i,j])
        for i in ribbit:
            move=random.randint(1,8) #random move 8 location
            if  move==1:
                if i[0]!=0:
                    if self.__field[i[0]-1][i[1]]!='R' and self.__field[i[0]-1][i[1]]!='V' and self.__field[i[0]-1][i[1]]!='S':
                        self.__field[i[0] - 1][i[1]]='R'
                        self.__field[i[0]][i[1]] = None
            if  move==2:
                if i[0]!=self.__x-1:
                    if self.__field[i[0]+1][i[1]]!='R' and self.__field[i[0]+1][i[1]]!='V'and self.__field[i[0]+1][i[1]]!='S':
                        self.__field[i[0] + 1][i[1]]='R'
                        self.__field[i[0]][i[1]] = None
            if  move==3:
                if i[1]!=0:
                    if self.__field[i[0]][i[1]-1]!='R' and self.__field[i[0]][i[1]-1]!='V'and self.__field[i[0]][i[1]-1]!='S':
                        self.__field[i[0]][i[1]-1]='R'
                        self.__field[i[0]][i[1]] = None
            if  move==4:
                if i[1]!=self.__y-1:
                    if self.__field[i[0]][i[1]+1]!='R' and self.__field[i[0]][i[1]+1]!='V'and self.__field[i[0]][i[1]+1]!='S':
                        self.__field[i[0]][i[1]+1]='R'
                        self.__field[i[0]][i[1]] = None
            if  move==5:
                if i[0]!=0 and i[1]!=0:
                    if self.__field[i[0]-1][i[1]-1]!='R' and self.__field[i[0]-1][i[1]-1]!='V'and self.__field[i[0]-1][i[1]-1]!='S':
                        self.__field[i[0]-1][i[1]-1]='R'
                        self.__field[i[0]][i[1]] = None
            if  move==6:
                if i[0]!=self.__x-1 and i[1]!=0:
                    if self.__field[i[0]+1][i[1]-1]!='R' and self.__field[i[0]+1][i[1]-1]!='V'and self.__field[i[0]+1][i[1]-1]!='S':
                        self.__field[i[0]+1][i[1]-1]='R'
                        self.__field[i[0]][i[1]] = None
            if  move==7:
                if i[0]!=0 and i[1]!=self.__y-1:
                    if self.__field[i[0]-1][i[1]+1]!='R' and self.__field[i[0]-1][i[1]+1]!='V'and self.__field[i[0]-1][i[1]+1]!='S':
                        self.__field[i[0]-1][i[1]+1]='R'
                        self.__field[i[0]][i[1]] = None
            if  move==8:
                if i[0]!=self.__x-1 and i[1]!=self.__y-1:
                    if self.__field[i[0]+1][i[1]+1]!='R' and self.__field[i[0]+1][i[1]+1]!='V'and self.__field[i[0]+1][i[1]+1]!='S':
                        self.__field[i[0]+1][i[1]+1]='R'
                        self.__field[i[0]][i[1]] = None


    def moveCptVertical(self,d):
        captain=[]
        for i in range(self.__x):
            for j in range(self.__y):
                if self.__field[i][j] == 'V':
                    captain=[i, j]
        if d==1: #move up
            if captain[0] == 0:
                print("You can't move that way!")
            elif self.__field[captain[0]-1][captain[1]]=='R':
                print("Don't step on the bunnies!")
            elif self.__field[captain[0]-1][captain[1]]=='S':
                print("Don't step on the snake!")
            elif self.__field[captain[0]-1][captain[1]]==None:
                self.__field[captain[0] - 1][captain[1]]='V'
                self.__field[captain[0]][captain[1]]=None
            else:
                for i in self.__vegetable:
                    if i[1]==self.__field[captain[0]-1][captain[1]]:
                        print("Yummy! A delicious",i[0])
                        self.__score+=i[2]
                        self.__busket.append(i[0])
                        self.__field[captain[0] - 1][captain[1]] = 'V'
                        self.__field[captain[0]][captain[1]] = None
        if d==0: #move down
            if captain[0] == self.__x-1:
                print("You can't move that way!")
            elif self.__field[captain[0]+1][captain[1]]=='R':
                print("Don't step on the bunnies!")
            elif self.__field[captain[0]+1][captain[1]]=='S':
                print("Don't step on the snake!")
            elif self.__field[captain[0]+1][captain[1]]==None:
                self.__field[captain[0] + 1][captain[1]]='V'
                self.__field[captain[0]][captain[1]]=None
            else:
                for i in self.__vegetable:
                    if i[1]==self.__field[captain[0]+1][captain[1]]:
                        print("Yummy! A delicious",i[0])
                        self.__score+=i[2]
                        self.__busket.append(i[0])
                        self.__field[captain[0] + 1][captain[1]] = 'V'
                        self.__field[captain[0]][captain[1]] = None
    def moveCptHorizontal(self,d):
        captain=[]
        for i in range(self.__x):
            for j in range(self.__y):
                if self.__field[i][j] == 'V':
                    captain=[i, j]
        if d==1: #move left
            if captain[1] == 0:
                print("You can't move that way!")
            elif self.__field[captain[0]][captain[1]-1]=='R':
                print("Don't step on the bunnies!")
            elif self.__field[captain[0]][captain[1]-1]=='S':
                print("Don't step on the snake!")
            elif self.__field[captain[0]][captain[1]-1]==None:
                self.__field[captain[0]][captain[1]-1]='V'
                self.__field[captain[0]][captain[1]]=None
            else:
                for i in self.__vegetable:
                    if i[1]==self.__field[captain[0]][captain[1]-1]:
                        print("Yummy! A delicious",i[0])
                        self.__score+=i[2]
                        self.__busket.append(i[0])
                        self.__field[captain[0]][captain[1]-1] = 'V'
                        self.__field[captain[0]][captain[1]] = None
        if d==0: #move right
            if captain[1] == self.__y-1:
                print("You can't move that way!")
            elif self.__field[captain[0]][captain[1]+1]=='R':
                print("Don't step on the bunnies!")
            elif self.__field[captain[0]][captain[1]+1]=='S':
                print("Don't step on the snake!")
            elif self.__field[captain[0]][captain[1]+1]==None:
                self.__field[captain[0]][captain[1]+1]='V'
                self.__field[captain[0]][captain[1]]=None
            else:
                for i in self.__vegetable:
                    if i[1]==self.__field[captain[0]][captain[1]+1]:
                        print("Yummy! A delicious",i[0])
                        self.__score+=i[2]
                        self.__busket.append(i[0])
                        self.__field[captain[0]][captain[1]+1] = 'V'
                        self.__field[captain[0]][captain[1]] = None
    def moveCaptain(self):
        move=input("Would you like to move up(W), down(S), left(A), or right(D):") #get input
        if move!='w' and move!='W' and move!='s' and move!='S' and move!='a' and move!='A' and move!='d' and move!='D' :
            print(move,"is not a valid option")
        if move=='w'or move=='W':
            self.moveCptVertical(self, 1)
        if move=='s'or move=='S':
            self.moveCptVertical(self, 0)
        if move=='a'or move=='A':
            self.moveCptHorizontal(self, 1)
        if move=='d'or move=='D':
            self.moveCptHorizontal(self, 0)

    def moveSnake(self):
        snake = [] #find snake
        for i in range(self.__x):
            for j in range(self.__y):
                if self.__field[i][j] == 'S':
                    snake = [i, j]
        captain = [] #find captain
        for i in range(self.__x):
            for j in range(self.__y):
                if self.__field[i][j] == 'V':
                    captain = [i, j]
        if captain[0]>snake[0]: #move to caption
            if self.__field[snake[0] + 1][snake[1]] == None:
                self.__field[snake[0] + 1][snake[1]] = 'S'
                self.__field[snake[0]][snake[1]] = None
                return
            elif self.__field[snake[0] + 1][snake[1]] == 'V':
                string="snake loses"
                for i in range(5): #remove last 5 veggie
                    for j in self.__vegetable:
                        if len(self.__busket) == 0:
                            break
                        if j[0] == self.__busket[-1]:
                            string+=", "+j[0]
                            self.__score -= j[2]
                            self.__busket.pop()
                            break
                print(string)
                self.__field[snake[0]][snake[1]] = None
                self.initSnake(self)
                return
        if captain[0]<snake[0]: #move to caption
            if self.__field[snake[0] - 1][snake[1]] == None:
                self.__field[snake[0] - 1][snake[1]] = 'S'
                self.__field[snake[0]][snake[1]] = None
                return
            elif self.__field[snake[0] - 1][snake[1]] == 'V':
                string = "snake loses"
                for i in range(5): #remove last 5 veggie
                    for j in self.__vegetable:
                        if len(self.__busket) == 0:
                            break
                        if j[0] == self.__busket[-1]:
                            string+=", "+j[0]
                            self.__score -= j[2]
                            self.__busket.pop()
                            break
                print(string)
                self.__field[snake[0]][snake[1]] = None
                self.initSnake(self)
                return
        if captain[1]>snake[1]: #move to caption
            if self.__field[snake[0] ][snake[1]+ 1] == None:
                self.__field[snake[0] ][snake[1]+ 1] = 'S'
                self.__field[snake[0]][snake[1]] = None
                return
            elif self.__field[snake[0]][snake[1]+ 1] == 'V':
                string = "snake loses"
                for i in range(5): #remove last 5 veggie
                    for j in self.__vegetable:
                        if len(self.__busket) == 0:
                            break
                        if j[0] == self.__busket[-1]:
                            string+=", "+j[0]
                            self.__score -= j[2]
                            self.__busket.pop()
                            break
                print(string)
                self.__field[snake[0]][snake[1]] = None
                self.initSnake(self)
                return
        if captain[1]<snake[1]: #move to caption
            if self.__field[snake[0]][snake[1] - 1] == None:
                self.__field[snake[0]][snake[1] - 1] = 'S'
                self.__field[snake[0]][snake[1]] = None
                return
            elif self.__field[snake[0]][snake[1] - 1] == 'V':
                string = "snake loses"
                for i in range(5): #remove last 5 veggie
                    for j in self.__vegetable:
                        if len(self.__busket) == 0:
                            break
                        if j[0] == self.__busket[-1]:
                            string+=", "+j[0]
                            self.__score -= j[2]
                            self.__busket.pop()
                            break
                print(string)
                self.__field[snake[0]][snake[1]] = None
                self.initSnake(self)
                return

    def gameOver(self):
        print("GAME OVER!\nYou managed to harvest the following vegetables:") #print result
        for i in self.__busket:
            print(i)
        print("Your score was:",self.__score)
    def highScore(self): #write score to data
        name=input("Please enter your three initials to go on the scoreboard: ")
        print("HIGH SCORES\nName	Score")
        try:
            file = open(self.__HIGHSCOREFILE)
        except:
            file =open(self.__HIGHSCOREFILE, 'w')
            file.write(name[0:3]+","+str(self.__score)+" ")
            print(name[0:3],"		",self.__score)
            file.close()
            return
        text=file.read()
        text=text.strip()
        text=text.split()
        for i in range(len(text)):
            text[i]=text[i].split(",")
            text[i][1]=int(text[i][1])
        text.append([name[0:3],self.__score])
        for i in range(len(text)):
            for j in range(i,len(text)):
                if text[i][1]>text[j][1]:
                    num=text[i][1]
                    text[i][1]=text[j][1]
                    text[j][1]=num
                    name2 = text[i][0]
                    text[i][0] = text[j][0]
                    text[j][0] = name2
        for i in range(len(text)):
            print(text[len(text)-1-i][0], "		", text[len(text)-1-i][1])
        string=''
        for i in text:
            string+=i[0]+","+str(i[1])+" "
        file.close()
        file = open(self.__HIGHSCOREFILE, 'w')
        file.write(string)
        file.close()

