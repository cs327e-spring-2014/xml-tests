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

import XML
from XML import xml_assign_id, xml_potentials, xml_check, xml_matches, xml_print, xml_search
from xml.etree.ElementTree import Element, fromstring, tostring

# -------
# TestXML
# -------

class TestXML (unittest.TestCase) :
    # -----------------
    # xml_assign_id
    # -----------------
    
    def test_xml_assign_id (self) :
        XML.id_num = 1
        s = "<A><B><C></C><D></D></B></A>"
        a = fromstring(s)
        self.assertTrue(type(a) == Element)
        c = xml_assign_id(a)
        self.assertTrue(type(c) == Element)
        self.assertTrue(c.text == "1")
        self.assertTrue(c.find("B").text == "2")
        self.assertTrue(c.find("B").find("C").text == "3")
        self.assertTrue(c.find("B").find("D").text == "4")
        
    def test_xml_assign_id_2 (self) :
        XML.id_num = 1
        s = "<A><B><C></C></B><D><E></E></D></A>"
        a = fromstring(s)
        self.assertTrue(type(a) == Element)
        c = xml_assign_id(a)
        self.assertTrue(type(c) == Element)
        self.assertTrue(c.text == "1")
        self.assertTrue(c.find("B").text == "2")
        self.assertTrue(c.find("B").find("C").text == "3")
        self.assertTrue(c.find("D").text == "4")
        self.assertTrue(c.find("D").find("E").text == "5")
        
    def test_xml_assign_id_3 (self) :
        XML.id_num = 1
        s = "<A><B><C></C><D></D></B><E><F></F></E></A>"
        a = fromstring(s)
        self.assertTrue(type(a) == Element)
        c = xml_assign_id(a)
        self.assertTrue(type(c) == Element)
        self.assertTrue(c.text == "1")
        self.assertTrue(c.find("B").text == "2")
        self.assertTrue(c.find("B").find("C").text == "3")
        self.assertTrue(c.find("B").find("D").text == "4")
        self.assertTrue(c.find("E").text == "5")
        self.assertTrue(c.find("E").find("F").text == "6")
       
    def test_xml_assign_id_4 (self) :
        XML.id_num = 1
        s = "<A><B><C></C><D></D></B><E><F><G></G></F><H></H></E></A>"
        a = fromstring(s)
        self.assertTrue(type(a) == Element)
        c = xml_assign_id(a)
        self.assertTrue(type(c) == Element)
        self.assertTrue(c.text == "1")
        self.assertTrue(c.find("B").text == "2")
        self.assertTrue(c.find("B").find("C").text == "3")
        self.assertTrue(c.find("B").find("D").text == "4")
        self.assertTrue(c.find("E").text == "5")
        self.assertTrue(c.find("E").find("F").text == "6") 
        self.assertTrue(c.find("E").find("F").find("G").text == "7")     
        self.assertTrue(c.find("E").find("H").text == "8")
        
    def test_xml_assign_id_5 (self) :
        XML.id_num = 1
        s = "<A><B><C></C><A></A></B><E><F><A></A></F><H></H></E></A>"
        a = fromstring(s)
        self.assertTrue(type(a) == Element)
        c = xml_assign_id(a)
        self.assertTrue(type(c) == Element)
        self.assertTrue(c.text == "1")
        self.assertTrue(c.find("B").text == "2")
        self.assertTrue(c.find("B").find("C").text == "3")
        self.assertTrue(c.find("B").find("A").text == "4")
        self.assertTrue(c.find("E").text == "5")
        self.assertTrue(c.find("E").find("F").text == "6") 
        self.assertTrue(c.find("E").find("F").find("A").text == "7")     
        self.assertTrue(c.find("E").find("H").text == "8")
                
    # --------------
    # xml_potentials
    # --------------
    
    def test_xml_potentials (self) :
        s = "<A><B><C></C><D></D></B></A>"
        c = fromstring(s)
        t = "<A><B></B></A>"
        p = fromstring(t)
        r = xml_potentials(c, p, [])
        self.assertTrue(type(r) == list)
        self.assertTrue(len(r) == 1)
        self.assertTrue(r[0].tag == "A")
        self.assertTrue(r[0].find("B").tag == "B")
        
    def test_xml_potentials_2 (self) :
        s = "<A><B><C></C></B><A><E></E></A></A>"
        c = fromstring(s)
        t = "<A><B><C></C></B></A>"
        p = fromstring(t)
        r = xml_potentials(c, p, [])
        self.assertTrue(type(r) == list)
        self.assertTrue(len(r) == 2)
        self.assertTrue(r[0].tag == "A")
        self.assertTrue(r[0].find("B").find("C").tag == "C")
        self.assertTrue(r[1].find("E").tag == "E")
    
    def test_xml_potentials_3 (self) :
        s = "<A><B><E></E><D></D></B><E><E></E></E></A>"
        c = fromstring(s)
        t = "<E><Z></Z></E>"
        p = fromstring(t)
        r = xml_potentials(c, p, [])
        self.assertTrue(type(r) == list)
        self.assertTrue(len(r) == 3)
        self.assertTrue(r[0].tag == "E")
        self.assertTrue(r[1].find("E").tag == "E")
        self.assertTrue(list(r[2]) == [])

    # ---------
    # xml_check
    # ---------
    
    def test_xml_check (self) :
        s = "<A><B><C></C><D></D></B></A>"
        c = fromstring(s)
        t = "<A><B></B></A>"
        p = fromstring(t)
        r = xml_check(c, p)
        self.assertTrue(r == True)
        
    def test_xml_check_2 (self) :
        s = "<A><B><C></C></B><B><E></E></B></A>"
        c = fromstring(s)
        t = "<B><C></C></B>"
        p = fromstring(t)
        first_potential = list(c)[0]
        second_potential = list(c)[1]
        potentials = [first_potential, second_potential]
        r = xml_check(potentials[0], p)
        self.assertTrue(r == True)
        r = xml_check(potentials[1], p)
        self.assertTrue(r == False)
        
    def test_xml_check_3 (self) :
        # pattern includes grandchild
        s = "<A><B><E></E><D></D><A></A></B><E><E></E></E></A>"
        c = fromstring(s)
        t = "<A><B><E></E></B></A>"
        p = fromstring(t)
        r = xml_check(c, p)
        self.assertTrue(r == True)
        second_potential = c.find("B").find("A")
        r = xml_check(second_potential, p)
        self.assertTrue(r == False)
       
    def test_xml_check_4 (self) :
        # pattern includes grandchild and false starting point
        s = "<A><B><E></E><D></D><A></A></B><E><E></E></E></A>"
        c = fromstring(s)
        t = "<A><B><E></E></B></A>"
        p = fromstring(t)
        r = xml_check(c, p)
        self.assertTrue(r == True)
        second_potential = c.find("B").find("A")
        r = xml_check(second_potential, p)
        self.assertTrue(r == False)
       
    def test_xml_check_5 (self) :
        s = "<A><B><C></C><A></A></B><A><B><C></C></B></A></A>"
        c = fromstring(s)
        t = "<A><B><C></C></B></A>"
        p = fromstring(t)
        first_potential = list(c)[0]
        F = xml_check(first_potential, p)
        self.assertTrue(F == False)
        
    # -----------
    # xml_matches
    # -----------
    
    def test_xml_matches (self) :
        s = "<A><B><C></C><A></A><D></D></B></A>"
        c = fromstring(s)
        t = "<A><B></B></A>"
        p = fromstring(t)
        l = [c, c.find("B").find("A")]
        r = xml_matches(l, p)
        self.assertTrue(r == [c])
    
    def test_xml_matches_2 (self) :
        s = "<Z><A><B><C></C><A></A><D></D></B></A><D><A><B><C></C></B></A></D></Z>"
        c = fromstring(s)
        t = "<A><B><C></C></B></A>"
        p = fromstring(t)
        l = [c.find("A"), c.find("A").find("B").find("A"), c.find("D").find("A")]
        r = xml_matches(l, p)
        self.assertTrue(r == [ l[0], l[1] ])    
    
    # ---------
    # xml_print
    # ---------
    
    def test_xml_print (self) :
        s = "<A><B><C><D><E><F></F></E></D></C></B></A>"
        c = fromstring(s)
        l = [c, c.find("B"), c.find("B").find("C"), c.find("B").find("C").find("D"), c.find("B").find("C").find("D").find("E"), c.find("B").find("C").find("D").find("E").find("F")]
        for i in l :
            i.text = i.tag
        r = io.StringIO()
        xml_print(l, r)
        self.assertTrue(r.getvalue() == "6\nA\nB\nC\nD\nE\nF")
    
    # ----------
    # xml_search
    # ----------
    
    def test_xml_search (self) :
        i = io.StringIO("<A><B><C></C><A></A><D></D></B></A><A><D></D></A>")
        o = io.StringIO()
        xml_search(i, o)
        self.assertTrue(o.getvalue() == "1\n4")

    def test_xml_search_2 (self) :
        i = io.StringIO("<zap><blam><A><B><C><Z></Z></C><A></A></B></A><B><D></D></B><A><B><C><Z><F></F></Z></C></B><D></D></A></blam></zap><A><B><C><Z></Z></C></B></A>")
        o = io.StringIO()
        xml_search(i, o)
        self.assertTrue(o.getvalue() == "2\n3\n10")

# ----
# main
# ----

print("TestXML.py")
unittest.main()
print("Done.")
