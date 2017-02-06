import unittest 
import cases
class Testcase (unittest.TestCase):
	def test_string(self):
		self.assertEqual(cases.case('example'), True)
	def test_int(self):
		self.assertEqual(cases.case(4), True)
	def test_list(self):
		self.assertEqual(cases.case(['a',2]), True)
	def test_dict(self):
		self.assertEqual(cases.case({'a':2 }), True)
	def test_float(self):
		self.assertEqual(cases.case(0.75), True)
	def test_even(self):
		self.assertEqual(cases.case(4), True)
	def test_odd(self):
		self.assertEqual(cases.case(9), True)
	def test_zero(self):
		self.assertEqual(cases.case(0), True)
	def test_greaterthanzero(self):
		self.assertEqual(cases.case(2), True)
	def test_lessthanzero(self):
		self.assertEqual(cases.case(-1), True)
	

if __name__ == '__main__':

	unittest.main()