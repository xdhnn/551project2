# Author: Dingan Li Vamshikrishna Vithoba Challa
# Date: 12/8/2023
# Description: Captain
import Creature

class Captain(Creature.Creature):
    _name = "Captain"
    _symbol = "V"
    _x=0
    _y=0
    __busket = []
    def Captainconstructor(self, name, symbol, x,y):
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
    def setbusket(self,busket):
        self.__busket=busket
    def getname(self):
        return self._name

    def getsymbol(self):
        return self._symbol

    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def getbusket(self):
        return self.__busket
    def addVeggie(self,Veggie):
        self.__busket.append(Veggie)