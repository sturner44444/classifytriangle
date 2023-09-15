# Test Triangle Classification

import unittest
import triangleclassification

class TestTriangleClass(unittest.TestCase):

#Test is_valid_triangle

    def test_valid(self):
        self.assertIs(triangleclassification.is_valid_triangle(1,2,3),True)
        self.assertIsNot(triangleclassification.is_valid_triangle(3,6,13),True)
        self.assertIs(triangleclassification.is_valid_triangle(1,2,10),False)
        self.assertIsNot(triangleclassification.is_valid_triangle(10,10,10),False)

# Test type_of_triangle
        
    def test_type(self):
        self.assertEqual(triangleclassification.type_of_triangle(1,1,1), "Equilateral")
        self.assertNotEqual(triangleclassification.type_of_triangle(5,10,15), "Equilateral")
        self.assertEqual(triangleclassification.type_of_triangle(1,1,2), "Isosceles")
        self.assertNotEqual(triangleclassification.type_of_triangle(3,3,3), "Isosceles")
        self.assertEqual(triangleclassification.type_of_triangle(1,3,4), "Scalene")
        self.assertNotEqual(triangleclassification.type_of_triangle(5,5,10), "Scalene")

# Test is_right_triangle

    def test_right(self):
        self.assertEqual(triangleclassification.is_right_triangle(3,4,5), "Is a right triangle.")
        self.assertNotEqual(triangleclassification.is_right_triangle(7,7,7), "Is a right triangle.")
        self.assertEqual(triangleclassification.is_right_triangle(3,4,6), "Not a right triangle.")
        self.assertNotEqual(triangleclassification.is_right_triangle(5,12,13), "Not a right triangle.")

if __name__=='__main__':
    unittest.main()

    
        
        
        
    
        
