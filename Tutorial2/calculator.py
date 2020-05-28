#sample calculator class
class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def add(self):
        return(int(self.num1)+int(self.num2))
        
    def sub(self):
        return(int(self.num1)-int(self.num2)) 
        
    def mul(self):
        return(int(self.num1)*(self.num2))
        
    def div(self):
        return(int(self.num1)/int(self.num2))
a=input('enter the first number')   
b=input('enter the second number')  
calculator=Calculator(a,b)
print(calculator.add())
print(calculator.sub())
print(calculator.mul())
print(calculator.div())
    
    
    
    