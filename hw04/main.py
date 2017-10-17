class Shape(object):
    '''形状'''
   
    def area(self):
        pass
 
         
class Rectangle(Shape):
    '''矩形'''
    def __init__(self, width=0, height=0):
        super().__init__()
        self.width = width
        self.height = height
         
    
    def area(self):
        return self.width * self.height
         
         
class Square(Rectangle):
    '''正方形'''
    def __init__(self, side=0):
        super().__init__(side, side)
         
         
         
class Ellipse(Shape):
    '''椭圆形'''
    pi = 3.1415926535
    def __init__(self, a=0, b=0):
        super().__init__()
        self.a = a
        self.b = b
         
   
    def area(self):
        return self.a * self.b * self.pi
         
         
class Circle(Ellipse):
    '''圆形'''
    def __init__(self, r=0):
        super().__init__(r, r)
