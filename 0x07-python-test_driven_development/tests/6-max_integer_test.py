#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def text_max_integer(self):
        self.assertEqual(max_integer([3, 4, 5, 6, 7, 8, 9]), 9)

    def test_recurring_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
    
    def test_list_with_bools(self):
        self.assertEqual(max_integer(["True", "False", "True"]), "True")
    
    # def test_empty_list(self):
    #     self.assertEqual(max_integer([]))

    def test_list_of_floats(self):
        self.assertEqual(max_integer([1.0, 7.9, 13.0, 130.5]), 130.5)
    
    def test_list_of_chars(self):
        self.assertEqual(max_integer(['a', 'c', 't', 'o', 'p']), 't')

    # def test_dict_in_list(self):
    #     with self.assertRaises(TypeError):
    #         max_integer([{1, 2, 3}, 8, 9])
    #         Traceback (most recent call last):
    #         File "<pyshell#5>", line 1, in <module>
    #             max_integer([{1, 2, 3}, 8, 9])
    #         File "<pyshell#1>", line 10, in max_integer
    #             if list[i] > result:
    #         TypeError: '>' not supported between instances of 'int' and 'set'
    
    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)
    
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -8, -78, -100, -5]), -1)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([9, 13, -12, 90, -100]), 90)
    
if __name__ == '__main__':
    unittest.main()
