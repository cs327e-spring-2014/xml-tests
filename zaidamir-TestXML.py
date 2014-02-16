import io
import unittest
from xml.etree.ElementTree import Element, fromstring, tostring

from XML import XML_traverse, XML_solve, XML_num_of_elements, XML_match, XML_printer, element_list


# -------
# TestXML
# -------


class TestXML (unittest.TestCase):
    
    # --------
    # traverse
    # --------
    
    def test_recur_1(self):
        a = ("<x><a><b><c></c></b></a><a><b></b></a></x>")
        a = fromstring(a)
        XML_traverse(a)
        self.assertTrue(len(element_list)  == 6)
    
    def test_recur_2(self):
        b  = ("<xml><w><b></b><c><d></d></c></w><c><d></d></c></xml>")
        b  = fromstring(b)
        XML_traverse(b)
        self.assertTrue(len(element_list) == 13)
    
    def test_recur_3(self):
        c = ("<xml><w><b></b><c><d><r></r><xx></xx></d></c></w><c><d></d></c></xml>")
        c = fromstring(c)
        XML_traverse(c)
        self.assertTrue(len(element_list) == 22)
    
    # -----
    # Solve
    # -----
    
    def test_solve1(self):
        w = io.StringIO()
        r = io.StringIO("<a><b><c></c></b></a><a><b></b></a>")
        self.assertTrue(XML_solve(r,w))
    
    def test_solve2(self):
        w = io.StringIO()
        r = io.StringIO("<a><b><gg></gg><g></g><c></c></b></a><a><b></b></a>")
        self.assertTrue(XML_solve(r,w))
    
    def test_solve3(self):
        w = io.StringIO()
        r = io.StringIO("<a><xx></xx><b><c></c></b></a><a><b><rr></rr></b></a>")
        self.assertTrue(XML_solve(r,w))

    # -----
    # print
    # -----
    
    def test_print_1(self):
        w = io.StringIO()
        z = [1]
        XML_printer(w, 4, [1,2,3,4])
        self.assertTrue(w.getvalue() == "4\n1\n2\n3\n4\n")
    
    def test_print_2(self):
        w = io.StringIO()
        z = [1]
        XML_printer(w, 3, [4,6,7])
        self.assertTrue(w.getvalue() == "3\n4\n6\n7\n")
    
    def test_print_3(self):
        w = io.StringIO()
        z = [1]
        XML_printer(w, 8, [1,2,3,4,8,7,6,5])
        self.assertTrue(w.getvalue() == "8\n1\n2\n3\n4\n8\n7\n6\n5\n")





print("TestXML.py")
unittest.main()
print("Done.")

