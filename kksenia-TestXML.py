import io
import unittest

from XML import read, evaluate, is_pattern, output, solve

class TestXML (unittest.TestCase):

	def test_output(self):
		w = io.StringIO()
		list_match = ('team')
		location_list = ['1']
		output(w,list_match, location_list)
		self.assertTrue(w.getvalue() == '1\n1\n')

	def test_output2(self):
		w = io.StringIO()
		list_match = ('0')
		location_list = []
		output(w,list_match,location_list)
		self.assertTrue(w.getvalue() == '0\n' )

	def test_output3(self):
		w = io.StringIO()
		list_match = ('team', 'team')
		location_list = ['2','7']
		self.assertFalse(w.getvalue() == '0\n')

	def test_ouptput4(self):
		w = io.StringIO()
		list_match = ('team, team, team')
		location_list = ['2','7', '27']
		self.assertFalse(w.getvalue() == '2\n2\n7\n')	
		
	def test_output5(self):
		w = io.StringIO()
		list_match = ('1','1','1','1')
		location_list = ['1,2,3,4']
		output(w,list_match, location_list)
		self.assertTrue(w.getvalue() == '1\n1\n2\n3\n4')			

	def test_output6(self):
		w = io.StringIO()
		list_match = ('team', 'team')
		location_list = ['2','7']
		self.assertFalse(w.getvalue() == '1\n2\n')		

	def test_output(self):
		w = io.StringIO()
		list_match = ('team')
		location_list = ['1']
		output(w,list_match, location_list)
		self.assertTrue(w.getvalue() == '1\n1\n')

	def test_is_pattern(self):
		w = io.StringIO()
		document = '<Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team>'
		pattern = '<27>'
		is_pattern(document, pattern)
		self.assertFalse(w.getvalue(True))

	def test_evaluate(document, pattern, list_match, location_list):
		w = io.StringIO()
		document = 'bibbidy'
		pattern = 'bibbidy'
		list_match = 'bibbidy'
		location_list = [1]
		self.assertTrue(w.getvalue(1))

	def test_evaluate(document, pattern, list_match, location_list):
		w = io.StringIO()
		document = 'bibbidy'
		pattern = 'bibbidy'
		list_match = 'bibbidy'
		location_list = [1]
		self.assertFalse(w.getvalue(0))


	def test_output7(self):
		w = io.StringIO()
		list_match = ('team, Rocket')
		location_list = [' 1, 2']
		output(w,list_match, location_list)
		self.assertTrue(w.getvalue() == '2\n1\n2')

	def test_output8(self):
		w = io.StringIO()
		list_match = ('')
		location_list = ['1']
		output(w,list_match, location_list)
		self.assertFalse(w.getvalue() == '1\n1\n')

	def test_output9(self):
		w = io.StringIO()
		list_match = ('team')
		location_list = ['3, 2, 1']
		output(w,list_match, location_list)
		self.assertFalse(w.getvalue() == '1\n1\n')

	def test_output10(self):
		w = io.StringIO()
		list_match = ('<team>')
		location_list = ['1']
		output(w,list_match, location_list)
		self.assertTrue(w.getvalue() == '1\n1\n')

	def test_output11(self):
		w = io.StringIO()
		list_match = ('team, tea, te')
		location_list = ['3']
		output(w,list_match, location_list)
		self.assertTrue(w.getvalue() == '1\n1\n1\n')


	def test_output12(self):
		w = io.StringIO()
		list_match = ('team')
		location_list = ['1, 2']
		output(w,list_match, location_list)
		self.assertTrue(w.getvalue() == '1\n1\n2')		

	def test_output13(self):
		w = io.StringIO()
		list_match = ('team')
		location_list = ['1']
		output(w,list_match, location_list)
		self.assertFalse(w.getvalue() == '')


print('TestXML.py')
unittest.main()
print('Done')
