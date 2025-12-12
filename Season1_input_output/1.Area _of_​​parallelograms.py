'''
This program was developed by Mohammad Rasool Azizi
Fall 2025

This program calculates the area of a parallelogram by taking
the height and base values.
'''

def show_parallelogram_ascii() -> None:
    '''
    Docstring for show_parallelogram_ascii
    
    This function show a sample parallelogram for better understanding with user.
    '''
    print("\n\n     Parallelogram    ", end="\n\n")
    print(' ' * 5 + '-' * 20)
    print(' ' * 4 + '/|' + ' ' * 18 + '/')
    print(' ' * 3 + '/ |' + ' ' * 17 + '/')
    print(' ' * 2 + '/  | H' + ' ' * 14 + '/')    
    print(' ' * 1 + '/   |' + ' ' * 15 + '/')
    print('-'* 20)
    print(' '* 9 + "B", end="\n\n")

def getting_value() -> tuple:
    '''
    Docstring for getting_value
    
    :return: The base and height values of the parallelogram as tuple type.
    :rtype: tuple
    This function get value of height and base of parallelogram
    from users.
    In End, function return (base, height) values as tuple
    '''
    
    try:
        base = float(input("Enter B (base) of parallelogram value: "))
        height = float(input("Enter H (height) of the parallelogram value: "))
    except ValueError:
        print("you must enter the True numerical value.")
    except Exception as e:
        print(f"You got this Error:\n{e}")
        
    return (base, height)
        
def calculate_area(base: float, height: float) -> float:
    '''
    Docstring for calculate_are
    
    :param base: The base value of parallelogram.
    :type base: float
    :param height: The height value of parallelogram.
    :type height: float
    :return: The result of calculating parallelogram's area by base and height values.
    :rtype: float
    '''
    
    return base * height
    
def show_result(base: float, height: float, area: float) -> None:
    '''
    Docstring for show_result
    
    :param base: The base value of the parallelogram.
    :type base: float
    :param height: Height value of the parallelogram.
    :type height: float
    :param area: Area value of the parallelogram.
    :type area: float
    
    This function Show the result and all information and shape of parallelogram in Terminal.
    '''
    print("----Result----")
    print(f"B : {base}")
    print(f'H : {height}')
    print(f"Area : {area}")
    
    
def main():
    show_parallelogram_ascii()
    b,h = getting_value()
    a = calculate_area(b, h)
    show_result(b, h, a)
    
if __name__ == "__main__":
    main()