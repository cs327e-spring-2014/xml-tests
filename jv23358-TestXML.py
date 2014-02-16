import unittest

from xml.etree.ElementTree import Element, fromstring, tostring
import XML
from StringIO import StringIO

class TestXML(unittest.TestCase):
	def test_getPattern(self):
		s = "<xml><THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n</xml>"
		a = fromstring(s)
		pattern = XML.getPattern(a)
		self.assertTrue(type(pattern) is Element)
		self.assertTrue(pattern.tag == "Team")

	def test_getPattern_noNewLines(self):
		s = "<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team></xml>"
		a = fromstring(s)
		pattern = XML.getPattern(a)
		self.assertTrue(type(pattern) is Element)
		self.assertTrue(pattern.tag == "Team")

	def test_getPattern_chopped(self):
		s = "<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>\n<Team>\n\t<Cooly></Cooly>\n</Team></xml>"
		a = fromstring(s)
		pattern = XML.getPattern(a)
		self.assertTrue(type(pattern) is Element)
		self.assertTrue(pattern.tag == "Team")

	def test_countChildren(self):
		s = "<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team></xml>"
		a = fromstring(s)
		pattern = XML.getPattern(a)
		patternChildren = 0
		patternChildren = XML.countChildren(pattern)
		self.assertTrue(patternChildren == 1)

	def test_countChildren_noChild(self):
		s = "<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team></Team></xml>"
		a = fromstring(s)
		pattern = XML.getPattern(a)
		patternChildren = 0
		patternChildren = XML.countChildren(pattern)
		self.assertTrue(patternChildren == 0)

	def test_countChildren_grandChildren(self):
		s = "<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly><Amber></Amber></Cooly></Team></xml>"
		a = fromstring(s)
		pattern = XML.getPattern(a)
		patternChildren = 0
		patternChildren = XML.countChildren(pattern)
		self.assertTrue(patternChildren == 2)

	def test_countChildren_multipleChildren(self):
		s = "<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly><Jelly></Jelly></Team></xml>"
		a = fromstring(s)
		pattern = XML.getPattern(a)
		patternChildren = 0
		patternChildren = XML.countChildren(pattern)
		self.assertTrue(patternChildren == 2)

	def test_count(self):
		s = "<xml><THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n</xml>"
		a = fromstring(s)
		pattern = XML.getPattern(a)
		patternChildren = 0
		patternChildren = XML.countChildren(pattern)
		XML.numElements = 0
		XML.numElements = XML.count(a, pattern, patternChildren)
		self.assertTrue(XML.numElements == 13)

	def test_count_depth(self):
		s = "<xml><THU><Team><ACRush><Jelly><Cooly><JiaJia><Ahyangyi><Dragon></Dragon></Ahyangyi></JiaJia></Cooly></Jelly></ACRush></Team></THU><Team><Cooly></Cooly></Team></xml>"
		a = fromstring(s)
		pattern = XML.getPattern(a)
		patternChildren = 0
		patternChildren = XML.countChildren(pattern)
		XML.numElements = 0
		XML.numElements = XML.count(a, pattern, patternChildren)
		self.assertTrue(XML.numElements == 10)

	def test_count_breadth(self):
		s = "<xml><THU><Team></Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly><JiaJia></JiaJia><Ahyangyi></Ahyangyi><Dragon></Dragon></THU></xml>"
		a = fromstring(s)
		pattern = XML.getPattern(a)
		patternChildren = 0
		patternChildren = XML.countChildren(pattern)
		XML.numElements = 0
		XML.numElements = XML.count(a, pattern, patternChildren)
		self.assertTrue(XML.numElements == 8)

	def test_findMatches(self):
		s = "<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team></xml>"
		a = fromstring(s)
		pattern = XML.getPattern(a)
		patternChildren = 0
		patternChildren = XML.countChildren(pattern)
		XML.locations = []
		XML.locations = XML.findMatches(a, pattern, patternChildren)
		self.assertTrue(XML.locations == []) #function only works in conjunction with the count function

	def test_findMatches_guaranteed_match(self):
		s = "<xml><THU><Team></Team></THU><THU></THU></xml>"
		a = fromstring(s)
		pattern = XML.getPattern(a)
		patternChildren = 0
		patternChildren = XML.countChildren(pattern)
		XML.matches = 0
		XML.findMatches(a, pattern, patternChildren)
		self.assertTrue(XML.matches == 0)

	def test_xmlSolve(self):
		r = StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
		w = StringIO()
		XML.xmlSolve(r,w)
		self.assertTrue(w.getvalue() == "2\n2\n7\n")

	def test_xmlSolve_grandChildren(self):
		r = StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly><Amber></Amber></Cooly></Team>")
		w = StringIO()
		XML.xmlSolve(r,w)
		self.assertTrue(w.getvalue() == "1\n7\n")

	def test_xmlSolve_multipleChildren(self):
		r = StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly><Jelly></Jelly></Team>")
		w = StringIO()
		XML.xmlSolve(r,w)
		self.assertTrue(w.getvalue() == "1\n2\n")

	def test_xmlSolve_noAnswer(self):
		r = StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Jesse></Jesse>")
		w = StringIO()
		XML.xmlSolve(r,w)
		self.assertTrue(w.getvalue() == "0\n")

	




print("TestXML.py")
unittest.main()
print("Done.")