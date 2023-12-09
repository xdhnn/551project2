# Author: Dingan Li Vamshikrishna Vithoba Challa
# Date: 12/8/2023
# Description: Veggie
import FieldInhabitant
class Veggie(FieldInhabitant.FieldInhabitant):
    _name = ""
    _symbol = ""
    __point=0

    def Veggieconstructor(self, name, symbol, point):
        self._name = name
        self._id = symbol
        self.__point = point
    def setname(self,name):
        self._name=name
    def setsymbol(self,symbol):
        self._symbol=symbol
    def setpoint(self,point):
        self.__point=point
    def getname(self):
        return self._name

    def getsymbol(self):
        return self._symbol

    def getpoint(self):
        return self.__point
    def __str__(self):
        print(self._symbol+":",self._name,self.__point,"points")