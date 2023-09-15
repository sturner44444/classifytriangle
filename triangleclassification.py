# Triangle Classification based on sides

# Function definition to check validity
def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

# Function definition for type
def type_of_triangle(a,b,c):
    if a==b and b==c:
        return ('Equilateral')
    elif a==b or b==c or a==c:
        return ('Isosceles')
    else:
        return ('Scalene')

# Function definition for right triangle
def is_right_triangle(a,b,c):
    if a**2+b**2==c**2:
        return ("Is a right triangle.")
    else:
        return ("Not a right triangle.")

# Reading three sides
side_a = float(input("Enter length of side a: "))
side_b = float(input("Enter length of side b: "))
side_c = float(input("Enter length of side c: "))

# Function call and making decision
if is_valid_triangle(side_a, side_b, side_c):
    type_of_triangle(side_a, side_b, side_c)
    is_right_triangle(side_a, side_b, side_c)
    print(type_of_triangle(side_a,side_b,side_c))
    print(is_right_triangle(side_a, side_b, side_c))
else:
    print("Triangle is not possible from given sides.")


