def Area_of_square(sides):
    return sides**2

def perimeter_of_rectangle(length,breadth):
    return 2*(length+breadth)

def Area_of_Rectangle(length,breadth):
    return length*breadth

if __name__ == "__main__":
    sides = int(input("enter the value of side: "))
    length = int(input("enter the value og length: "))
    breadth = int(input("enter the value of breadth: "))

    areaofsquare = Area_of_square(sides)
    print(areaofsquare)
    perimeterofrectangle = perimeter_of_rectangle(length,breadth)
    print(perimeterofrectangle)
    areaofrectangle = Area_of_Rectangle(length,breadth)
    print(areaofrectangle)