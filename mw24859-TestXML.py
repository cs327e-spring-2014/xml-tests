#!/usr/bin/env python

# -------------------------------
# projects/xml/XML.py
# Copyright (C) 2014
# Matt Woods, Carvey Leung
# -------------------------------

"""
To test the program:
% python TestXML.py >& TestXML.out
% chmod ugo+x TestXML.py
% TestXML.py >& TestXML.out
"""


import StringIO
import unittest

from xml.etree.ElementTree import Element, fromstring
from XML import xml_read, xml_search, xml_children, xml_print, xml_solve
import XML



class TestXML(unittest.TestCase):

    # ----
    # read
    # ----

    def test_xml_read_1 (self) :
        s = ''
        r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team></THU><Team><Cooly></Cooly></Team>")
        xml_read(r)
        self.assertTrue(type(s) == str)

    def test_xml_read_2 (self) :
        xml = fromstring("<Team></Team>")
        r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team></THU><Team><Cooly></Cooly></Team>")
        xml_read(r)
        self.assertTrue(type(xml) == Element)

    def test_xml_read_3 (self) :
        p = fromstring("<THU></THU>")
        r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team></THU><Team><Cooly></Cooly></Team>")
        xml_read(r)
        self.assertTrue(type(p) == Element)


    
    # ------
    # search
    # ------

    def test_xml_search_1 (self) :
        XML.index = 1
        l = []
        xml = fromstring("<xml><a></a></xml>")
        p = fromstring("<a></a>")
        d = ["a"]
        xml_search(xml, p, d, l)
        self.assertTrue(l[0] == 2)
        self.assertTrue(len(l) == 1)

    def test_xml_search_2 (self) :
        XML.index = 1
        l = []
        xml = fromstring("<xml><a><dog></dog></a></xml>")
        p = fromstring("<a></a>")
        d = ["a"]
        xml_search(xml, p, d, l)
        self.assertTrue(l[0] == 2)
        self.assertTrue(len(l) == 1)

    def test_xml_search_3 (self) :
        XML.index = 1
        l = []
        xml = fromstring("<xml><a></a><dog></dog></xml>")
        p = fromstring("<dog></dog>")
        d = ["dog"]
        xml_search(xml, p, d, l)
        self.assertTrue(l[0] == 3)
        self.assertTrue(len(l) == 1)

    # --------
    # children
    # --------

    def test_xml_children_1 (self) :
        index = 1
        l = []
        length = 1
        i = fromstring("<xml><a></a></xml>")
        p = fromstring("<xml><a></a></xml>")
        d = ["xml","a"]
        xml_children(i, p, index, length, d, l)
        self.assertTrue(l[0] == 1)
        self.assertTrue(len(l) == 1)

    def test_xml_children_1 (self) :
        index = 1
        l = []
        length = 1
        i = fromstring("<xml><a></a></xml>")
        p = fromstring("<xml><a></a></xml>")
        d = ["xml","a"]
        xml_children(i, p, index, length, d, l)
        self.assertTrue(l[0] == 1)
        self.assertTrue(len(l) == 1)

    def test_xml_children_1 (self) :
        index = 1
        l = []
        length = 1
        i = fromstring("<xml><a></a></xml>")
        p = fromstring("<xml><a></a></xml>")
        d = ["xml","a"]
        xml_children(i, p, index, length, d, l)
        self.assertTrue(l[0] == 1)
        self.assertTrue(len(l) == 1)

    # -----
    # print
    # -----

    def test_xml_print_1 (self) :
        w = StringIO.StringIO()
        l = [3, 4, 5]
        xml_print(l, w)
        self.assertTrue(w.getvalue() == "3\n3\n4\n5")

    def test_xml_print_2 (self) :
        w = StringIO.StringIO()
        l = [7, 20, 398]
        xml_print(l, w)
        self.assertTrue(w.getvalue() == "3\n7\n20\n398")

    def test_xml_print_3 (self) :
        w = StringIO.StringIO()
        l = [9, 90, 178, 999]
        xml_print(l, w)
        self.assertTrue(w.getvalue() == "4\n9\n90\n178\n999")

    # -----
    # solve
    # -----

    def test_xml_solve_1 (self) :
        r = StringIO.StringIO("<xml><a></a></xml><RUN></RUN>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertTrue(w.getvalue() == "0")

    def test_xml_solve_2 (self) :
        r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertTrue(w.getvalue() == "2\n2\n7")

    def test_xml_solve_3 (self) :
        r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team></THU><Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertTrue(w.getvalue() == "1\n2")

print "TestXML.py"
unittest.main()
print "Done"
