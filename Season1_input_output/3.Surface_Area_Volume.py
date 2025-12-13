"""
This program was developed by Mohammad Rasoul Azizi
Fall 2025

This program calculates the surface area and volume of a sphere
based on a user-provided radius.
"""

from math import pi


def get_positive_float(prompt: str) -> float:
    """
    Prompt the user for a positive numeric value and return it.
    """
    while True:
        try:
            value = float(input(f"Enter the {prompt}: "))
            if value <= 0:
                print("The value must be greater than zero. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def show_sphere_ascii() -> None:
    """
    Display a simple ASCII illustration of a sphere and its radius.
    """
    print(r"""
        . - ~ ~ ~ - .
     .'               `.
    /                   \
   |          .__________|
    \            Radius /
     `.               .'
       ` - . ~ ~ . - '
             Sphere
    """)


def calculate_surface_area(radius: float) -> float:
    """
    Calculate and return the surface area of a sphere.
    """
    return 4 * pi * radius ** 2


def calculate_volume(radius: float) -> float:
    """
    Calculate and return the volume of a sphere.
    """
    return (4 / 3) * pi * radius ** 3


def show_result(radius: float, area: float, volume: float) -> None:
    """
    Display the radius, surface area, and volume of the sphere.
    """
    print("----- Result -----")
    print(f"Radius        : {radius}")
    print(f"Surface Area  : {area}")
    print(f"Volume        : {volume}")


def main() -> None:
    """
    Main execution function of the program.
    """
    show_sphere_ascii()
    radius = get_positive_float("radius of the sphere")
    area = calculate_surface_area(radius)
    volume = calculate_volume(radius)
    show_result(radius, area, volume)


if __name__ == "__main__":
    main()
