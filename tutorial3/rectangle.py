#rectangle class with private class variables

class Rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
    def area(self):
        return(self.__length*self.__width)
    
    def permimeter(self):
        return(2*(self.__length+self.__width))
    
    
    
    
rec1=Rectangle(10,5)
print(f'area is {rec1.area()}')
print(f'rectange is {rec1.permimeter()}')