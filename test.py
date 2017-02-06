import unittest 
import cases
class Testcase (unittest.TestCase):
	def test_string(self):
		self.assertEqual(cases.case('example'), True)
	def test_int(self):
		self.assertEqual(cases.case(4), True)

if __name__ == '__main__':

	unittest.main()