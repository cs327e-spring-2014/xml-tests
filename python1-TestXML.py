#!/usr/bin/env python3

# -------------------------------
# projects/XML/TestXML.py
# Copyright (C) 2014
# Noel Thomas
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
import XML
from XML import xmlSolve, xmlRead, xmlPrint, find_rootPos

# --------
# TestXML
# --------
    
class TestXML (unittest.TestCase):
   
    # ----
    # read
    # ----
    
    #normal
    def test_read1(self):
        r = io.StringIO("<A><B><C></C></B></A>")
        b = xmlRead(r)
        self.assertTrue(b == "<A><B><C></C></B></A>")
        
    #multiple lineage with same names   
    def test_read2(self):
        r = io.StringIO("<A><B><B></B></B></A>")
        b = xmlRead(r)
        self.assertTrue(b == "<A><B><B></B></B></A>")
        
    #new line character    
    def test_read3(self):
        r = io.StringIO("<A>\n<B>\n<C></C>\n</B>\n</A>")
        b = xmlRead(r)
        self.assertTrue(b == "<A><B><C></C></B></A>")
    
    # -----
    # print
    # -----
    
    #count is three
    def test_print1(self):
        w = io.StringIO()
        a = [3,5,7]
        xmlPrint(w, 3, a)
        self.assertTrue(w.getvalue() == "3\n3\n5\n7\n")
    
    #count is four
    def test_print2(self):
        w = io.StringIO()
        a = [8,17,33,45]
        xmlPrint(w, 4, a)
        self.assertTrue(w.getvalue() == "4\n8\n17\n33\n45\n")
    
    #count is one
    def test_print3(self):
        w = io.StringIO()
        a = [1]
        xmlPrint(w, 1, a)
        self.assertTrue(w.getvalue() == "1\n1\n")
    
    #count is zero
    def test_print4(self):
        w = io.StringIO()
        a = []
        xmlPrint(w, 0, a)
        self.assertTrue(w.getvalue() == "0\n")
    
    # --------
    # rootPos
    # --------
    
    #root name is used as a child 
    def test_rootPos1(self):
        q = "<B></B><C></C><A></A></A><B></B>"
        lst = []
        n = 0
        s = ""
        a = len("<A>")
        r = "A"
        num = find_rootPos(q,lst,n,s,a,r)
        self.assertTrue(num == 28)
    
    #root name is used as a grandchild    
    def test_rootPos2(self):
        q = "<B></B><C><A></A><B></B></C></A><B></B>"
        lst = []
        n = 0
        s = ""
        a = len("<A>")
        r = "A"
        num = find_rootPos(q,lst,n,s,a,r)
        self.assertTrue(num == 35)
    
    #root name is not used inside the tree    
    def test_rootPos3(self):
        q = "<B></B><C></C></A><B></B>"
        lst = []
        n = 0
        s = ""
        a = len("<A>")
        r = "A"
        num = find_rootPos(q,lst,n,s,a,r)
        self.assertTrue(num == 21)
        
    # ------
    # solve
    # ------
    
    #same name used more than once    
    def test_solve1(self):
        r = io.StringIO("<A><B></B><C><B></B></C></A><B></B>")
        w = io.StringIO()
        xmlSolve(r, w)
        self.assertTrue(w.getvalue() == "2\n2\n4\n")
    
    #normal
    def test_solve2(self):
        r = io.StringIO("<A><B></B><C></C></A><B></B>")
        w = io.StringIO()
        
        XML.wrdList[:] = []
        XML.levelList[:] = []
        XML.posList[:] = []
        XML.tracker = 0
        XML.level = 0
        XML.position = -1
        XML.count = 0
        
        xmlSolve(r, w)
        self.assertTrue(w.getvalue() == "1\n2\n")
    
    #multiple lineage
    def test_solve3(self):
        r = io.StringIO("<A><D></D><B><C></C><E></E></B></A><B><E></E><C></C></B>")
        w = io.StringIO()
        
        XML.wrdList[:] = []
        XML.levelList[:] = []
        XML.posList[:] = []
        XML.tracker = 0
        XML.level = 0
        XML.position = -1
        XML.count = 0
        
        xmlSolve(r, w)
        self.assertTrue(w.getvalue() == "1\n3\n")
    
    #multiple lineage with different order inside the pattern
    def test_solve4(self):
        r = io.StringIO("<A><B><C><D><E><F></F><G></G></E></D></C></B></A><D><E><G></G><F></F></E></D>")
        w = io.StringIO()
        
        XML.wrdList[:] = []
        XML.levelList[:] = []
        XML.posList[:] = []
        XML.tracker = 0
        XML.level = 0
        XML.position = -1
        XML.count = 0
        
        xmlSolve(r, w)
        self.assertTrue(w.getvalue() == "1\n4\n")
    
    #no pattern
    def test_solve5(self):
        r = io.StringIO("<A><B></B><C></C><D><B></B></D></A><B><C></C></B>")
        w = io.StringIO()
        
        XML.wrdList[:] = []
        XML.levelList[:] = []
        XML.posList[:] = []
        XML.tracker = 0
        XML.level = 0
        XML.position = -1
        XML.count = 0
        
        xmlSolve(r, w)
        self.assertTrue(w.getvalue() == "0\n")
    
print("TestXML.py")
unittest.main()
print("Done.")
