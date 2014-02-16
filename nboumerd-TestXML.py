# -------------------------------
# projects/xml/TestXML.py
# -------------------------------

# -------
# imports
# -------

import io
import unittest

from XML import xml_traverse, xml_read, xml_eval, xml_print, xml_solve, xml_find_pairs, xml_return_eval_string, xml_compare
from xml.etree.ElementTree import Element, fromstring
# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # traverse
    # ----
    def test_traverse_1 (self) :
        s = "<parent><child></child></parent>"
        x = fromstring(s)
        l = xml_traverse(x)
        self.assertTrue(l == "<parent><child></child></parent>")
    def test_traverse_2 (self) :
        s = "<parent></parent>"
        x = fromstring(s)
        l = xml_traverse(x)
        self.assertTrue(l != "")
        self.assertTrue(l == "<parent></parent>")
    def test_traverse_3 (self) :
        s = "<parent><child><grandchild></grandchild></child></parent>"
        x = fromstring(s)
        l = xml_traverse(x)
        self.assertTrue(l != "")
        self.assertTrue(l == "<parent><child><grandchild></grandchild></child></parent>")

    # ----
    # find_pairs
    # ----
    def test_find_pairs_1 (self) :
        s = "<xml><parent1><child1></child1></parent1><parent2><child2></child2></parent2></xml>"
        a =  xml_find_pairs(s)
        i, j = a
        self.assertTrue(type(i) is Element)
        self.assertTrue(type(j) is Element)
        self.assertTrue(xml_traverse(i) == xml_traverse(fromstring("<parent1><child1></child1></parent1>")))
        self.assertTrue(xml_traverse(j) == xml_traverse(fromstring("<parent2><child2></child2></parent2>")))
    def test_find_pairs_2 (self) :
        s = "<xml><parent1></parent1><parent2></parent2></xml>"
        a =  xml_find_pairs(s)
        i, j = a
        self.assertTrue(type(i) is Element)
        self.assertTrue(type(j) is Element)
        self.assertTrue(xml_traverse(i) == xml_traverse(fromstring("<parent1></parent1>")))
        self.assertTrue(xml_traverse(j) == xml_traverse(fromstring("<parent2></parent2>")))
    def test_find_pairs_3 (self) :
        s = "<xml><parent1><child1><grandchild1></grandchild1></child1></parent1><parent2></parent2></xml>"
        a =  xml_find_pairs(s)
        i, j = a
        self.assertTrue(type(i) is Element)
        self.assertTrue(type(j) is Element)
        self.assertTrue(xml_traverse(i) == xml_traverse(fromstring("<parent1><child1><grandchild1></grandchild1></child1></parent1>")))
        self.assertTrue(xml_traverse(j) == xml_traverse(fromstring("<parent2></parent2>")))

    # ----
    # read
    # ----
    def test_read_1 (self) :
        r = io.StringIO(unicode("<parent1><child1><grandchild1></grandchild1></child1></parent1><parent2><child2></child2></parent2>"))
        s = xml_read(r)
        self.assertTrue(s == "<xml><parent1><child1><grandchild1></grandchild1></child1></parent1><parent2><child2></child2></parent2></xml>")
    def test_read_2 (self) :
        r = io.StringIO(unicode("<parent1><child1></child1></parent1><parent2><child2></child2></parent2>"))
        s = xml_read(r)
        self.assertTrue(s == "<xml><parent1><child1></child1></parent1><parent2><child2></child2></parent2></xml>")
    def test_read_3 (self) :
        r = io.StringIO(unicode("<parent1></parent1><parent2></parent2>"))
        s = xml_read(r)
        self.assertTrue(s == "<xml><parent1></parent1><parent2></parent2></xml>")
    # ----
    # compare
    # ----
    def test_compare_1 (self) :
        a = [fromstring("<parent1><child1><grandchild1></grandchild1></child1></parent1>"), fromstring("<child1><grandchild1></grandchild1></child1>")]
        i,j = a
        b = xml_compare(i, j)
        self.assertTrue(b == False)
    def test_compare_2 (self) :
        a = [fromstring("<apple><apple></apple><orange><peach><orange><peach></peach></orange></peach></orange><orange><peach></peach></orange></apple>"), fromstring("<orange><apple></apple></orange>")]
        i,j = a
        b = xml_compare(i, j)
        self.assertTrue(b == False)
    def test_compare_3 (self) :
        a = [fromstring("<apple><apple></apple><orange><apple></apple></orange></apple>"), fromstring("<apple></apple>")]
        i,j = a
        b = xml_compare(i, j)
        self.assertTrue(b == True)
    # ----
    # eval
    # ----
    def test_eval_1 (self) :
        a = [fromstring("<parent1><child1><grandchild1></grandchild1></child1></parent1>"), fromstring("<child1><grandchild1></grandchild1></child1>")]
        i,j = a
        list = []
        occur = [0]
        xml_eval(i, j, 0, occur, list, j.tag)
        self.assertTrue(occur[0] == 1)
        self.assertTrue(list[0] == 2)
        self.assertTrue(j.tag == "child1")
    def test_eval_2 (self) :
        a = [fromstring("<apple><apple></apple><orange><peach><orange><peach></peach></orange></peach></orange><orange><peach></peach></orange></apple>"), fromstring("<orange><peach></peach></orange>")]
        i,j = a
        list = []
        occur = [0]
        xml_eval(i, j, 0, occur, list, j.tag)
        self.assertTrue(occur[0] == 3)
        self.assertTrue(list == [3,5,7])
        self.assertTrue(j.tag == "orange")
    def test_eval_3 (self) :
        a = [fromstring("<apple><apple></apple><orange><apple></apple></orange></apple>"), fromstring("<apple></apple>")]
        i,j = a
        list = []
        occur = [0]
        xml_eval(i, j, 0, occur, list, j.tag)
        self.assertTrue(occur[0] == 3)
        self.assertTrue(list== [1,2,4])
        self.assertTrue(j.tag == "apple")
    def test_eval_4 (self) :
        a = [fromstring("<peach><orange><apple></apple></orange></peach>"), fromstring("<peach><apple></apple></peach>")]
        i,j = a
        list = []
        occur = [0]
        xml_eval(i, j, 0, occur, list, j.tag)
        self.assertTrue(occur[0] == 0)
        self.assertTrue(list == [])
        self.assertTrue(j.tag == "peach")

    # ----
    # return_eval_string
    # ----
    def test_return_eval_string_1 (self) :
        i = fromstring("<parent1><child1><grandchild1></grandchild1></child1></parent1>")
        j = fromstring("<child1><grandchild1></grandchild1></child1>")
        s = xml_return_eval_string(i,j)
        self.assertTrue(type(s) is str)
        self.assertTrue(s == "1"+"\n"+"2")
    def test_return_eval_string_2 (self) :
        i = fromstring("<peach><orange><apple></apple></orange></peach>")
        j = fromstring("<peach><apple></apple></peach>")
        s = xml_return_eval_string(i,j)
        self.assertTrue(type(s) is str)
        self.assertTrue(s == "0")
    def test_return_eval_string_3 (self) :
        i = fromstring("<purple><red><blue></blue><black></black></red><black></black></purple>")
        j = fromstring("<red><blue></blue><black></black></red>")
        s = xml_return_eval_string(i,j)
        self.assertTrue(type(s) is str)
        self.assertTrue(s == "1"+"\n"+"2")

    # -----
    # print
    # -----
    def test_print_1 (self) :
        w = io.StringIO()
        xml_print(w,unicode("1\n5"))
        self.assertTrue(w.getvalue() == "1\n5\n")
    def test_print_2 (self) :
        w = io.StringIO()
        xml_print(w, unicode("2\n3\n8"))
        self.assertTrue(w.getvalue() == "2\n3\n8\n")
    def test_print_3 (self) :
        w = io.StringIO()
        xml_print(w, unicode("5\n4\n19\n35\n7"))
        self.assertTrue(w.getvalue() == "5\n4\n19\n35\n7\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r =io.StringIO(unicode("<parent1><child1><grandchild1></grandchild1></child1></parent1><child1><grandchild1></grandchild1></child1>"))
        w = io.StringIO()
        xml_solve(r, w)
        self.assertTrue(w.getvalue() == "1\n2\n")
    def test_solve_2 (self):
        r=io.StringIO(unicode("<Fruit><bluberry></bluberry><orange><clementine></clementine><bluberry><bluberry></bluberry></bluberry></orange></Fruit><bluberry></bluberry>"))
        w = io.StringIO()
        xml_solve(r, w)
        self.assertTrue(w.getvalue() == "3\n2\n5\n6\n")
    def test_solve_3 (self) :
        r =io.StringIO(unicode("<apple><apple></apple><orange><peach><orange><peach></peach></orange></peach></orange><orange><peach></peach></orange></apple><orange><peach></peach></orange>"))
        w = io.StringIO()
        xml_solve(r, w)
        self.assertTrue(w.getvalue() == "3\n3\n5\n7\n")


# ----
# main
# ----

print("TestXML.py")
unittest.main()
print("Done.")
