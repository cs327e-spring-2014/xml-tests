#!/usr/bin/env python3

# -------------------------------
# Copyright (C) 2014
# Anthony Oliveri, Derek Perez
# -------------------------------

"""
To test the program:
    % python TestXML.py > TestXML.out
    % chmod ugo+x TestXML.py
    % TestXML.py > TestXML.out
"""

# -------
# imports
# -------

import io
import unittest
import xml.etree.ElementTree as ET
import XML

from XML import xml_read, xml_eval, xml_print, xml_solve, xml_patternExists

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        reader = io.StringIO("<one><two><three><four></four><five></five></three></two><ten><nine></nine><eight></eight><three><four></four><five></five></three></ten></one>\n<three><four></four><five></five></three>")
        writer = io.StringIO()
        xml_solve(reader, writer)
        self.assertTrue(writer.getvalue() == "2\n3\n9\n\n")

    def test_solve_2 (self) :
        reader = io.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>\n<Team><Cooly></Cooly></Team>")
        writer = io.StringIO()
        xml_solve(reader, writer)
        self.assertTrue(writer.getvalue() == "2\n2\n7\n\n")

    def test_solve_3(self):
        reader = io.StringIO("<a><b><c><d><e><f></f></e></d></c></b> <z><c><d><e></e><f></f></d><g></g></c></z> </a>\n<c><d><e></e><f></f></d><g></g></c>")
        writer = io.StringIO()
        xml_solve(reader, writer)
        self.assertTrue(writer.getvalue() == "1\n8\n\n")


    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        XML.TAG_INDEX = 0

        treeReader = io.StringIO("<one><two><three><four></four><five></five></three></two><ten><nine></nine><eight></eight><three><four></four><five></five></three></ten></one>")
        tree = ET.fromstring("<tree>" + treeReader.read() + "</tree>")
        patternReader = io.StringIO("<three><four></four><five></five></three>")
        pattern = ET.fromstring(patternReader.read())

        matches = xml_eval(tree, pattern, [])
        self.assertTrue(matches == [3, 9])

    def test_eval_2 (self) :
        XML.TAG_INDEX = 0

        treeReader = io.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>")
        tree = ET.fromstring("<tree>" + treeReader.read() + "</tree>")
        patternReader = io.StringIO("<Team><Cooly></Cooly></Team>")
        pattern = ET.fromstring(patternReader.read())

        matches = xml_eval(tree, pattern, [])
        self.assertTrue(matches == [2, 7])

    def test_eval_3 (self) :
        XML.TAG_INDEX = 0

        treeReader = io.StringIO("<a><b><c><d><e><f></f></e></d></c></b> <z><c><d><e></e><f></f></d><g></g></c></z></a>")
        tree = ET.fromstring("<tree>" + treeReader.read() + "</tree>")
        patternReader = io.StringIO("<c><d><e></e><f></f></d><g></g></c>")
        pattern = ET.fromstring(patternReader.read())

        matches = xml_eval(tree, pattern, [])
        self.assertTrue(matches == [8])


    # ----
    # patternExists
    # ----

    def test_patternExists_1(self):
        treeReader = io.StringIO("<three><four></four><five></five></three>")
        tree = ET.fromstring(treeReader.read())
        patternReader = io.StringIO("<three><four></four><five></five></three>")
        pattern = ET.fromstring(patternReader.read())

        self.assertTrue(xml_patternExists(tree, pattern))

    def test_patternExists_2(self):
        treeReader = io.StringIO("<three><four></four><five></five><six></six></three>")
        tree = ET.fromstring(treeReader.read())
        patternReader = io.StringIO("<three><four></four><five></five></three>")
        pattern = ET.fromstring(patternReader.read())

        self.assertTrue(xml_patternExists(tree, pattern))

    def test_patternExists_3(self):
        treeReader = io.StringIO("<three><four></four><five><six></six></five></three>")
        tree = ET.fromstring(treeReader.read())
        patternReader = io.StringIO("<three><four></four><five></five></three>")
        pattern = ET.fromstring(patternReader.read())

        self.assertTrue(xml_patternExists(tree, pattern))

    def test_patternExists_4(self):
        treeReader = io.StringIO("<three><six><four></four><five></five></six></three>")
        tree = ET.fromstring(treeReader.read())
        patternReader = io.StringIO("<three><four></four><five></five></three>")
        pattern = ET.fromstring(patternReader.read())

        self.assertTrue(not xml_patternExists(tree, pattern))

    def test_patternExists_5(self):
        treeReader = io.StringIO("<Team><Cooly></Cooly></Team>")
        tree = ET.fromstring(treeReader.read())
        patternReader = io.StringIO("<Team><Cooly></Cooly></Team>")
        pattern = ET.fromstring(patternReader.read())

        self.assertTrue(xml_patternExists(tree, pattern))

    def test_patternExists_6(self):
        treeReader = io.StringIO("<THU><Team><Cooly></Cooly></Team></THU>")
        tree = ET.fromstring(treeReader.read())
        patternReader = io.StringIO("<Team><Cooly></Cooly></Team>")
        pattern = ET.fromstring(patternReader.read())

        self.assertTrue(not xml_patternExists(tree, pattern))

    def test_patternExists_7(self):
        treeReader = io.StringIO("<a><b><c><d><e><f></f></e></d></c></b></a>")
        tree = ET.fromstring(treeReader.read())
        patternReader = io.StringIO("<c><d><e></e><f></f></d><g></g></c>")
        pattern = ET.fromstring(patternReader.read())

        self.assertTrue(not xml_patternExists(tree, pattern))

    def test_patternExists_8(self):
        treeReader = io.StringIO("<a><c><d><e></e><f></f></d><g></g></c></a>")
        tree = ET.fromstring(treeReader.read())
        patternReader = io.StringIO("<c><d><e></e><f></f></d><g></g></c>")
        pattern = ET.fromstring(patternReader.read())

        self.assertTrue(not xml_patternExists(tree, pattern))

    def test_patternExists_9(self):
        treeReader = io.StringIO("<c><d><e></e><f></f></d><g></g></c>")
        tree = ET.fromstring(treeReader.read())
        patternReader = io.StringIO("<c><d><e></e><f></f></d><g></g></c>")
        pattern = ET.fromstring(patternReader.read())

        self.assertTrue(xml_patternExists(tree, pattern))




    # ----
    # read
    # ----

    def test_read_1 (self) :
        reader = io.StringIO("<outer1><inner1></inner1><inner2></inner2></outer1><outer2><inner3></inner3></outer2>")
        tree = xml_read(reader)
        treeStr = ET.tostring(tree, "unicode")
        self.assertTrue(treeStr == "<xml><outer1><inner1 /><inner2 /></outer1><outer2><inner3 /></outer2></xml>")

    def test_read_2 (self) :
        reader = io.StringIO("<a><b><c></c><d></d><e></e></b></a>")
        tree = xml_read(reader)
        treeStr = ET.tostring(tree, "unicode")
        self.assertTrue(treeStr == "<xml><a><b><c /><d /><e /></b></a></xml>")

    def test_read_spacing (self) :
        reader = io.StringIO("<one>   <two>        </two> </one>")
        tree = xml_read(reader)
        treeStr = ET.tostring(tree, "unicode")
        self.assertTrue(treeStr == "<xml><one>   <two>        </two> </one></xml>")

    def test_read_newlines(self):
        reader = io.StringIO("<one>   <two>   \n\n     </two> \n</one>")
        tree = xml_read(reader)
        treeStr = ET.tostring(tree, "unicode")
        self.assertTrue(treeStr == "<xml><one>   <two>   \n\n     </two> \n</one></xml>")

    def test_read_tabs(self):
        reader = io.StringIO("<one>   \t<two>   \t     </two> \n</one>")
        tree = xml_read(reader)
        treeStr = ET.tostring(tree, "unicode")
        self.assertTrue(treeStr == "<xml><one>   \t<two>   \t     </two> \n</one></xml>")

    def test_read_multipleTrees(self):
        reader = io.StringIO("<one><two></two></one>\n<red><blue><green></green></blue></red>")
        tree = xml_read(reader)
        treeStr = ET.tostring(tree, "unicode")
        self.assertTrue(treeStr == "<xml><one><two /></one>\n<red><blue><green /></blue></red></xml>")


    # -----
    # print
    # -----

    def test_print_1 (self) :
        writer = io.StringIO()
        xml_print(writer, [2, 7])
        self.assertTrue(writer.getvalue() == "2\n2\n7\n\n")

    def test_print_2 (self) :
        writer = io.StringIO()
        xml_print(writer, [1])
        self.assertTrue(writer.getvalue() == "1\n1\n\n")

    def test_print_3 (self) :
        writer = io.StringIO()
        xml_print(writer, [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        self.assertTrue(writer.getvalue() == "11\n10\n1\n2\n3\n4\n5\n6\n7\n8\n9\n0\n\n")

    def test_print_corner(self):
        writer = io.StringIO()
        xml_print(writer, [])
        self.assertTrue(writer.getvalue() == "0\n\n")

# ----
# main
# ----

print("TestXML.py")
unittest.main()
print("Done.")
