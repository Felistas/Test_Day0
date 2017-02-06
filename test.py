import unittest 
import cases
class Testcase (unittest.TestCase):
	def test_string(self):
		self.assertEqual(cases.case('Number'), True)

if __name__ == '__main__':

	unittest.main()