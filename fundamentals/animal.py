#This is an example that uses inheritance, getter, setter, namespaces, etc

class animal:

    def __init__(self,birthtype,appearance,blooded):
        self.__birthtype = birthtype
        self.__appearance = appearance
        self.__blooded = blooded
    
    @property
    def birthtype(self):
        return self.__birthtype
        
    @birthtype.setter
    def birthtype(self):
        self.__birthtype = birthtype

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self):
        self.__appearance= appearance

    @property
    def blooded(self):
        return self.__blooded
    
    @blooded.setter
    def blooded(self):
        self.__blooded=blooded

    def __str__(self):
        return "The {} is {} it is {} it is {}".format(type(self).__name__,self.birthtype,self.appearance,self.blooded) 

class mammal(animal):

    def __init__(self,birthtype="alive",appearance="hair",blooded="warm",nurseyoung="yes"):
        self.__nurseyoung=nurseyoung
        animal.__init__(self, birthtype, appearance, blooded)

    @property
    def nurseyoung(self):
        return self.__nurseyoung

    @nurseyoung.setter
    def nurseyoung(self):
        self.__nurseyoung= nurseyoung

    def __str__(self):
        return super.__str__(mammal)+" and it is {} they nurse their young ".format(self.nurseyoung)

class reptile(animal):
    def __init__(self,birthtype="in an egg",appearance="scales",blooded="cold"):
        animal.__init__(self, birthtype, appearance, blooded)


animal1=animal("alive","physical","warm")
print(animal1)
mammal1=mammal()
print(mammal1)
reptile1=reptile()
print(reptile1)
