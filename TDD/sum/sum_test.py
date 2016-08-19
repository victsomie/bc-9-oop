import unittest

from my_sum import my_sum

class MySumTest(unittest.TestCase):

	def setUp(self):
		self.numbers = [10, 15, 20, 50, 2, 3, 1, 40, 7, 23]

	def test_non_numbers(self):
		self.assertRaise(TypeError, my_sum(5, 5), msg = "Integers required")
		self.assertRaise(my_sum(5, 5), "invalid")
		
	def test_sum_of_digits(self):
		#Below are doc strings
		'''
		Test sum of digits /numbers
		'''
		# result = my_sum(5,10)
		# self.assertEqual(result, 15)
		self.assertEqual(my_sum(10, 15), 25)
		self.assertEqual(my_sum(20, 50), 70)
		self.assertEqual(my_sum(2, 3), 5)
		self.assertEqual(my_sum(1, 40), 41)
		self.assertEqual(my_sum(7, 23), 30)

		#Test with a message
		self.assertEqual(
			my_sum(30, 70), 
			100,
			msg='5 factorial should be 120')

if __name__ == '__main__':
	unittest.main()

