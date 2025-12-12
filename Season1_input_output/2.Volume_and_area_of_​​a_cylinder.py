'''
This program was developed by Mohammad Rasool Azizi
Fall 2025

This program calculates the volume and surface area of a cylinder
based on user-provided height and radius.
'''

from math import pi

def take_value(argument: str) -> float:
    """Prompt the user for a positive numeric value and return it."""
    while True:
        try:
            temp = float(input(f"Enter a valid value for {argument}: "))
            if temp < 1:
                print("The value must be positive.\nTry again.")
                continue
            return temp
        except ValueError:
            print("The value must be numeric.\nTry again.")


class Cylinder:
    """
    A simple Cylinder class that stores radius and height
    and calculates surface area and volume.
    """

    def __init__(self, radius: float, height: float) -> None:
        """
        Initialize a Cylinder object.

        :param radius: Radius of the cylinder.
        :type radius: float
        :param height: Height of the cylinder.
        :type height: float
        """
        self.radius = radius
        self.height = height
        
    def show_cylinder(self) -> None:
        """Print an ASCII representation of a cylinder."""
        print("\n\n\t\tCylinder\n\n")
        print('\t\t/-----\\ ')
        print("\t       /    ___\\")
        print('\t       \\     R /')
        print('\t       |\\ ___ /|')
        print("\t       |   |   |")
        print("\t       |   | H |")
        print("\t       |   |   |")
        print("\t       \\   |   /")
        print("\t        \\__|__/", end="\n\n")
        
    def calculate_area(self) -> float:
        """Calculate the surface area of the cylinder."""
        return (2 * pi * self.radius * self.height) + (2 * pi * (self.radius ** 2))       
    
    def calculate_volume(self) -> float:
        """Calculate the volume of the cylinder."""
        return pi * (self.radius ** 2) * self.height
    
    def show_result(self) -> None:
        """Display the cylinder’s radius, height, area, and volume."""
        area = self.calculate_area()
        volume = self.calculate_volume()
        
        print('---- Result ----')
        print(f'R (Radius) : {self.radius}')
        print(f'H (Height) : {self.height}')
        print(f'Area       : {area}')
        print(f'Volume     : {volume}')
        
        
if __name__ == "__main__":
    radius = take_value('Radius')
    height = take_value('Height')
    sample = Cylinder(radius, height)
    sample.show_cylinder()
    sample.show_result()
