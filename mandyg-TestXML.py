#!/usr/bin/env python3

#----------
# imports
#----------

import unittest
import io
import XML

from xml.etree.ElementTree import Element, tostring, fromstring
from XML import xml_read, xml_findPattern, StoreGlob1, StoreGlob2, xml_print, xml_solve, xml_traverse

#----------
# xml_test
#----------
class TestXML(unittest.TestCase) :
    #-------------
    #
    #-------------
    def test1_read(self):
        r = "<xml><THU><Team><ACRush><Ahyangyi><akid></akid></Ahyangyi><Dragon></Dragon><cat></cat></ACRush><Jelly></Jelly><Cooly></Cooly></Team></THU><Team><Ahyangyi><akid></akid></Ahyangyi><Dragon></Dragon><cat></cat></Team></xml>"
        rtest = fromstring(r)
        totest = xml_read("ElementTree.xml")
        self.assertTrue(rtest.tag == totest.tag)

    def test2_read(self):
        r = "<xml><THU><Team><ACRush><Ahyangyi><akid></akid></Ahyangyi><Dragon></Dragon><cat></cat></ACRush><Jelly></Jelly><Cooly></Cooly></Team></THU><Team><Ahyangyi><akid></akid></Ahyangyi><Dragon></Dragon><cat></cat></Team></xml>"
        rtest = fromstring(r)

        totest = xml_read("ElementTree.xml")
        self.assertTrue(rtest.find("THU").tag == "THU")

    def test3_read(self):
        r = "<xml><THU><Team><ACRush><Ahyangyi><akid></akid></Ahyangyi><Dragon></Dragon><cat></cat></ACRush><Jelly></Jelly><Cooly></Cooly></Team></THU><Team><Ahyangyi><akid></akid></Ahyangyi><Dragon></Dragon><cat></cat></Team></xml>"
        rtest = fromstring(r)
        totest = xml_read("ElementTree.xml")
        self.assertTrue(totest.find(".//akid").tag == "akid")

    def test1_findPattern(self): # Verify that a list is being returned
        xmltree = "<xml><outer><middle><inner></inner></middle></outer></xml>"
        globals1 = StoreGlob1(fromstring(xmltree))
        xml_findPattern(globals1,fromstring(xmltree))
        pattern = globals1.curPattern
        self.assertTrue(type(pattern) is list)

    def test2_findPattern(self): # Verify correct number of elements
        xmltree = "<xml><outer><middle><inner></inner></middle></outer></xml>"
        globals1 = StoreGlob1(fromstring(xmltree))
        xml_findPattern(globals1,fromstring(xmltree))
        pattern = globals1.curPattern
        self.assertTrue(len(pattern) == 4)

    def test3_findPattern(self): # Verify that 2nd element is correct
        xmltree = "<xml><outer><middle><inner></inner></middle></outer></xml>"
        globals1 = StoreGlob1(fromstring(xmltree))
        xml_findPattern(globals1,fromstring(xmltree))
        pattern = globals1.curPattern
        testelement = fromstring("<middle></middle>")
        self.assertTrue(pattern[2].tag == testelement.tag)

unittest.main()
