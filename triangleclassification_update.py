"""Triangle Classification based on sides."""

def is_valid_triangle(a,b,c):
    """Function definition to check validity"""
    is_valid = a+b>=c and b+c>=a and c+a>=b
    return is_valid

def type_of_triangle(a,b,c):
    """Function definition for type"""
    if a==b and b==c:
        return 'Equilateral'
    if a==b or b==c or a==c:
        return 'Isosceles'
    return 'Scalene'

def is_right_triangle(a,b,c):
    """Function definition for right triangle"""
    if a**2+b**2==c**2:
        return "Is a right triangle."
    return "Not a right triangle."

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
