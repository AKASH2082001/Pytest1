def Area_of_square(sides):
    return sides ** 2

def perimeter_of_rectangle(length,breadth):
    return 2*(length+breadth)

def Area_of_Rectangle(length, breadth):
     return length * breadth


if __name__ == "__main__":
    while True:
        print("select an option")
        print("1. Area of square")
        print("2.Perimeter of Rectangle")
        print("3. Area of Rectangle")
        print("4.Exit")

        choice = int(input("enter the option: "))

        if choice == 1:
            sides = int(input("enter the value of side: "))
            areaofsquare = Area_of_square(sides)
            print(areaofsquare)

        elif choice == 2:


            length = int(input("enter the value og length: "))
            breadth = int(input("enter the value of breadth: "))
            perimeterofrectangle = perimeter_of_rectangle(length, breadth)
            print(perimeterofrectangle)

        elif choice == 3:


            length = int(input("enter the value og length: "))
            breadth = int(input("enter the value of breadth: "))
            areaofrectangle = Area_of_Rectangle(length, breadth)
            print(areaofrectangle)

        elif choice == 4:
            break

        else:
            print("invalid option")




