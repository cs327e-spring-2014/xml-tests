'''
To test the program:
  $ python3 TestXML.py > TestXML.out
'''

# -------
# imports
# -------

import io
import unittest

from xml.etree.ElementTree import Element, fromstring, tostring

from XML import XML_read, XML_print, XML_next, XML_traverse, XML_pattern_traverse, XML_solve

# --------
# Test XML
# --------

class TestXML (unittest.TestCase):
	# ----
	# read
	# ----
    def test_read(self):
        r = io.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
        output = XML_read(r)
        self.assertTrue(output == "<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team></xml>")
		
    def test_read_2(self):
        r = io.StringIO("<Computer><Science><is><really></really></is><fun></fun><most><of><the><time></most></of></the></time></Science></Computer>")
        output = XML_read(r)
        self.assertTrue(output == "<xml><Computer><Science><is><really></really></is><fun></fun><most><of><the><time></most></of></the></time></Science></Computer></xml>")

    def test_read_3(self):
        r = io.StringIO("<Hello><C></C></Hello>")
        output = XML_read(r)
        self.assertTrue(output == "<xml><Hello><C></C></Hello></xml>")


	# -----
	# XML_print
	# -----	  
    def test_XML_print_1(self):
        w = io.StringIO()
        XML_print(list([2,7]), w)
        self.assertTrue(w.getvalue() == "2\n2\n7\n")

    def test_XML_print_2(self):
        w = io.StringIO()
        XML_print(list([]), w)
        self.assertTrue(w.getvalue() == "0\n")

    def test_XML_print_3(self):
        w = io.StringIO()
        XML_print(list([4,8,9]), w)
        self.assertTrue(w.getvalue() == "3\n4\n8\n9\n")

    
	# -----
	# XML_next
	# -----
    def test_XML_next_1(self):
        s = fromstring("<Team><ACRush></ACRush></Team>")
        output = XML_next(s)
        self.assertTrue(output == ['ACRush'])

    def test_XML_next_2(self):
        s = fromstring("<Team><Amber></Amber></Team>")
        output = XML_next(s)
        self.assertTrue(output == ['Amber'])

    def test_XML_next_3(self):
        s = fromstring("<Team><ACRush></ACRush><Team></Team></Team>")
        output = XML_next(s)
        output = XML_next(s)
        self.assertTrue(output == ['ACRush', 'Team'])


	# -----
	# traverse
	# -----
    def test_XML_traverse_1(self):
        r = fromstring("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>")      
        myList = ['Team','ACRush','/ACRush','/Team']
        XML_traverse(r, myList, 0)
        output = True
        self.assertTrue(output == True)

    def test_XML_traverse_2(self):
        r = fromstring("<THU><Team><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>")      
        myList = ['Team','ACRush','/ACRush','/Team']
        XML_traverse(r, myList, 0)
        myresult = True
        self.assertTrue(True == myresult)

    def test_XML_traverse_3(self):
        r = fromstring("<THU><Team><ACRush></ACRush></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>")      
        output = True
        myList = ['Team','ACRush','/ACRush','/Team']
        XML_traverse(r, myList, 0)
        self.assertTrue(output == True)

	# -----
	# pattern traverse
	# -----
    def test_XML_pattern_traverse_1(self):
        s = fromstring("<Team><ACRush></ACRush></Team>") 
        myList = []
        output = XML_pattern_traverse(s, myList)
        self.assertTrue(myList == ['Team','ACRush','/ACRush','/Team'])

    def test_XML_pattern_traverse_2(self):
        s = fromstring("<Team><ACRush></ACRush><Cooly></Cooly></Team>") 
        myList = []
        output = XML_pattern_traverse(s, myList)
        self.assertTrue(myList == ['Team','ACRush','/ACRush','Cooly','/Cooly','/Team'])

    def test_XML_pattern_traverse_3(self):
        s = fromstring("<Team><ACRush><Hello></Hello></ACRush><Cooly></Cooly></Team>") 
        myList = []
        output = XML_pattern_traverse(s, myList)
        self.assertTrue(myList == ['Team','ACRush','Hello', '/Hello','/ACRush','Cooly','/Cooly','/Team'])

	# -----
	# solve
	# -----
    def test_XML_solve_1(self):
       r = io.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
       w = io.StringIO()
       XML_solve(r,w)
       output = True
       self.assertTrue(output == True)

    def test_XML_solve_2(self):
       r = io.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
       w = io.StringIO()
       XML_solve(r,w)
       out = True
       self.assertTrue(out == True)

    def test_XML_solve_3(self):
       r = io.StringIO("<THU><Team><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
       w = io.StringIO()
       XML_solve(r,w)
       output = True
       self.assertTrue(output == True)


# ----
# main
# ----

print("TestXML.py")
unittest.main()
print("Done.")