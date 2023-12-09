# Author: Dingan Li Vamshikrishna Vithoba Challa
# Date: 12/8/2023
# Description: Field Inhabitant
class FieldInhabitant(object):
    _name=""
    _symbol=""

    def constructor(self,name,symbol):
        self._name=name
        self._id=symbol

    def setname(self,name):
        self._name=name
    def setsymbol(self,symbol):
        self._symbol=symbol
    def getname(self):
        return self._name
    def getsymbol(self):
        return self._symbol
