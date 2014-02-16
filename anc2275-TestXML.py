#!/usr/bin/env python3

# -------------------------------
# cs327e-xml/TestXML.py
# Andrea Curo
# Nabil Hossain
# -------------------------------

"""
To test the program:
	% python3 TestXML.py > TestXML.out
	% chmod ugo+x TestXML.py
	% TestXML.py >& TestXML.out
"""
# -------
# imports
# -------

import io
import unittest

import XML
from xml.etree.ElementTree import Element, fromstring

#-------
#TestXML
#-------

class TestXML(unittest.TestCase):
	
	#---------
	# recurse
	#---------

	def test_XML_recurse_0(self):
		e = Element("pi")
		v = XML.XML_recurse(e, e, False)
		self.assertTrue(v)

	def test_XML_recurse_1(self):
		e = Element("pi")
		i = Element("pie")
		v = XML.XML_recurse(e, i, True)
		self.assertTrue(not v)

	def test_XML_recurse_2(self):
		e = Element("pi")
		v = XML.XML_recurse(e, e, True)
		self.assertTrue(not v)

	#--------
	# print
	#--------
	def test_XML_print_0(self):
		w = io.StringIO()
		XML.i = [1,3]
		XML.XML_print(w)
		self.assertTrue(w.getvalue() == "2\n1\n3\n")

	def test_XML_print_1(self):
		w = io.StringIO()
		XML.i = [4,2,1]
		XML.XML_print(w)
		self.assertTrue(w.getvalue() == "3\n1\n2\n4\n")

	def test_XML_print_2(self):
		w =io.StringIO()
		XML.i = [45, 2, 7]
		XML.XML_print(w)
		self.assertTrue(w.getvalue() == "3\n2\n7\n45\n")
	#--------
	# solve
	#--------

	def test_XML_solve_0(self):
		r = io.StringIO("<nope>\n</nope>\n<nothing></nothing>")
		w = io.StringIO()
		XML.XML_solve(r,w)
		self.assertTrue(w.getvalue() == "0\n")

	def test_XML_solve_1(self):
		r = io.StringIO("<junk>\n</junk>\n<junk></junk>")
		w = io.StringIO()
		XML.XML_solve(r,w)
		self.assertTrue(w.getvalue() == "1\n1\n")

	def test_XML_solve_2(self):
		r = io.StringIO("<stuff>\n<junk>\n</junk>\n</stuff>\n<junk></junk>")
		w = io.StringIO()
		XML.XML_solve(r,w)
		self.assertTrue(w.getvalue() == "1\n2\n")

	def test_XML_solve_3(self):
		r = io.StringIO("<stuff>\n<wat>\n<junk>\n</junk>\n</wat>\n</stuff>\n<junk></junk>")
		w = io.StringIO()
		XML.XML_solve(r,w)
		self.assertTrue(w.getvalue() == "1\n3\n")

	def test_XML_solve_4(self):
		r = io.StringIO("<stuff>\n<wat>\n<junk>\n</junk>\n</wat>\n</stuff>\n<wat><junk></junk></wat>")
		w = io.StringIO()
		XML.XML_solve(r,w)
		self.assertTrue(w.getvalue() == "1\n2\n")

	def test_XML_solve_5(self):
		r = io.StringIO("<stuff>\n<wat>\n<bees>\n<junk>\n</junk>\n</bees>\n</wat>\n</stuff>\n<wat><junk></junk></wat>")
		w = io.StringIO()
		XML.XML_solve(r,w)
		self.assertTrue(w.getvalue() == "0\n")

	def test_XML_solve_6(self):
		r = io.StringIO("<junk>\n</junk>\n<Junk></Junk>")
		w = io.StringIO()
		XML.XML_solve(r,w)
		self.assertTrue(w.getvalue() == "0\n")

print("TestXML.py")
unittest.main()
print("Done.")

#;_;
