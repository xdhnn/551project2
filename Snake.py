# Author: Dingan Li Vamshikrishna Vithoba Challa
# Date: 12/8/2023
# Description: Snake
import Creature
class Snake(Creature.Creature):
    _name = "Snake"
    _symbol = "S"
    _x=0
    _y=0
    def Snakeconstructor(self, name, symbol, x,y):
        self._name = name
        self._id = symbol
        self._x = x
        self._y = y
    def setname(self,name):
        self._name=name
    def setsymbol(self,symbol):
        self._symbol=symbol
    def setx(self,x):
        self._x=x
    def sety(self,y):
        self._y=y
    def getname(self):
        return self._name

    def getsymbol(self):
        return self._symbol

    def getx(self):
        return self._x
    def gety(self):
        return self._y
