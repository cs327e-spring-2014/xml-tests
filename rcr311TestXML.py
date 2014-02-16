#!/usr/bin/env python3

# -------------------------------
# projects/xml/TestXML.py
# -------------------------------

"""
To test the program:
% python TestXML.py >& TestXML.out
% chmod ugo+x TestXML.py
% TestXML.py >& TestXML.out
"""

# -------
# imports
# -------

import io
import unittest
import sys
from xml.etree.ElementTree import Element, fromstring, tostring

from XML import compare, traverse, traversePattern, patternLister, listMaker, solve

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # compare
    # ----

    def test_compare_1 (self) :
        tree1 =("itemTag")
        tree2 = ("itemTag")
        compare(tree1, tree2)
        self.assertTrue(tree1 == tree2)
        self.assertTrue(type(tree1) == str)
        self.assertTrue(type(tree2) == str)

    def test_compare_2 (self) :
        tree1 =("hello")
        tree2 = ("goodbye")
        compare(tree1, tree2)
        self.assertFalse(tree1 == tree2)
        self.assertTrue(type(tree1) == str)
        self.assertTrue(type(tree2) == str)

    def test_compare_3 (self) :
        tree1 =("nothing")
        tree2 = ("Nothing")
        compare(tree1, tree2)
        self.assertFalse(tree1 == tree2)
        self.assertTrue(type(tree1) == str)
        self.assertTrue(type(tree2) == str)
        
    # ----
    # traverse
    # ----

    def test_traverse_1 (self) :
        xmlRoot = fromstring("<a><b></b></a>")
        xmlPattern = fromstring("<a><b></b></a>")
        self.assertTrue(type(xmlRoot) == Element)
        self.assertTrue(type(xmlPattern) == Element)
        self.assertTrue((type(xmlRoot.tag) == str))

    def test_traverse_2 (self) :
        xmlRoot = fromstring("<d><b></b></d>")
        xmlPattern = fromstring("<r><b></b></r>")
        self.assertTrue(type(xmlRoot) == Element)
        self.assertTrue(type(xmlPattern) == Element)
        self.assertTrue((type(xmlRoot.tag) == str))

    def test_traverse_3 (self) :
        xmlRoot = fromstring("<happy><no></no></happy>")
        xmlPattern = fromstring("<project><close></close></project>")
        self.assertTrue(type(xmlRoot) == Element)
        self.assertTrue(type(xmlPattern) == Element)
        self.assertTrue((type(xmlRoot.tag) == str))

    # -----
    # traversePattern
    # -----

    def test_traversePattern_1 (self) :
        xmlRoot = fromstring("<one><two></two></one>")
        xmlPattern = fromstring("<one><two></two></one>")
        self.assertTrue(type(xmlRoot) == Element)
        self.assertTrue(xmlRoot.tag == xmlPattern.tag)

    def test_traversePattern_2 (self) :
        xmlRoot = fromstring("<one><five></five></one>")
        xmlPattern = fromstring("<one><two></two></one>")
        self.assertTrue(type(xmlRoot) == Element)
        self.assertTrue(xmlRoot.tag == xmlPattern.tag)

    def test_traversePattern_3 (self) :
        xmlRoot = fromstring("<one><five></five></one>")
        xmlPattern = fromstring("<ONE><two></two></ONE>")
        self.assertTrue(type(xmlRoot) == Element)
        self.assertFalse(xmlRoot.tag == xmlPattern.tag)

    # -----
    # patternLister
    # -----

    def test_patternLister_1 (self) :
        PatternList = []
        xmlPattern = fromstring("<one><two></two></one>")
        self.assertTrue(type(PatternList) == list)
        self.assertTrue(type(xmlPattern) == Element)

    def test_patternLister_2 (self) :
        PatternList = 0
        xmlPattern = fromstring("<ONE><two></two></ONE>")
        self.assertFalse(type(PatternList) == list)
        self.assertTrue(type(xmlPattern) == Element)

    def test_patternLister_3 (self):
        PatternList = ["one", "two"]
        xmlPattern = fromstring("<one><two></two></one>")
        self.assertTrue(type(PatternList) == list)
        self.assertTrue(type(xmlPattern) == Element)

    # -----
    # listMaker
    # -----

    def test_listMaker_1 (self) :
        m = fromstring("<one><two></two></one>")
        xmlList = []
        self.assertTrue(type(xmlList) == list)
        self.assertTrue(type(m) == Element)

    def test_listMaker_2 (self) :
        m = ("<one><two></two></one>")
        xmlList = []
        self.assertTrue(type(xmlList) == list)
        self.assertTrue(type(m) == str)

    def test_listMaker_3 (self) :
        m = fromstring("<oNe><two></two></oNe>")
        xmlList = []
        self.assertTrue(type(xmlList) == list)
        self.assertTrue(type(m) == Element)

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        SystemInput = fromstring("<one><two></two></one>")
        SystemOutput = (sys.stdout)
        self.assertTrue(type(SystemInput) == Element)

    def test_solve_2 (self) :
        SystemInput = fromstring("<yes><two></two></yes>")
        SystemOutput = (sys.stdout)
        self.assertTrue(type(SystemInput) == Element)

    def test_solve_3 (self) :
        SystemInput = fromstring("<yes></yes>")
        SystemOutput = (sys.stdout)
        self.assertTrue(type(SystemInput) == Element)
        
# ----
# main
# ----

print("TestXML.py")
unittest.main()
print("Done.")
