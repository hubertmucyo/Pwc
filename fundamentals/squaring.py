#A compilation of exercises on file square.py 

class square:

    def __init__(self,size=0):
            self._size=size
        
    def area(self):
        return self._size**2

    @property
    def size(self):
       return self._size
    
    def size(self,value):
        if type(value) is not int:
            raise TypeError("size must be an intege")
        elif value<0 :
            raise ValueError("size must be >=0")
        else:
            self._size=value
    
obj = square(21)
obj.area()
obj.size(21)