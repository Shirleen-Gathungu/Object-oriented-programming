# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr



class Circle:
    def __init__(self,radius):
        self.radius=radius 
    
    def area(self):
        calculate_area=3.142*(self.radius)*(self.radius)
        return(f"The area is {calculate_area} centimetres square")

    def circumference(self):
        calculate_circumeference=2*(self.radius)*3.142
        return(f"The circumference is {calculate_circumeference} centimetres")
      
# Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4a

class Square:
    def __init__(self,side):
        self.side=side

    def area(self):
        calculate_area=(self.side)*(self.side)
        return(f"The area is {calculate_area} metres square")
    def perimeter(self):
        calculate_perimeter=(self.side)*4
        return(f"The perimeter is {calculate_perimeter} metres")

# Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using the formula A=wl
# It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)

class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    
    def area(self):
        calculate_area= (self.width)*(self.length)

        return(f"The area is {calculate_area} metres square")
    
    def perimeter(self):
        calculate_perimeter=2*((self.width)+(self.length))
        return(f"The perimeter is {calculate_perimeter} metres")


# Class Sphere
# A Sphere Instance accepts the radius of the sphere (r)
# It has a method to calculate the surface area (A) using the formula A=4πr2
# It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)

class Sphere:
    def __init__(self,radius):
        self.radius=radius
    
    def surface_area(self):
        calculate_surface_area= 4*3.142*(self.radius)*(self.radius)
        return(f"The surface_area is {calculate_surface_area} centimetres square")

    def volume(self):
        calculate_volume=4/3*(3.142*(self.radius)*(self.radius)*(self.radius))

        return(f"The volume is {calculate_volume} centimetres square")