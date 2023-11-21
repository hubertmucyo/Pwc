#A compilation of exercises on file square.py 

class square:

    def __init__(self,size=0):
            self.__size=size
        
    def area(self):
        return self.__size**2

    @property
    def size(self):
       return self.__size
    
    def size(self,value):
        if type(value) is not int:
            raise TypeError("size must be an intege")
        elif value<0 :
            raise ValueError("size must be >=0")
        else:
            self.__size=value
    
     def my_print(self):
        if self.__size == 0:
            print()
        else:
            counter = self.__size
            startsize = self.__size
            coun_num = 0
            while self.__size > coun_num:
                while counter > 0:
                    print("#", end="")
                    counter -= 1
                print()
                counter = startsize
                self.__size -= 1