#! /usr/bin/env python3

# ---------------------
# TestXML.py
# Tests the functions in XML.py
# ---------------------

"""
Testing this program:
  % python3 kenon-TestXML.py >& kenon-TestXML.out
"""

# -----
# importin n stuff
# -----

import io
import unittest

from XML import xml_eval, xml_read, xml_write, xml_search_recur, xml_scan_recur, xml_solve, idx

from xml.etree.ElementTree import Element, fromstring, tostring

class TestXML (unittest.TestCase) :

  # ----
  # read
  # ----
  def test_read1 (self) :
    s = ""
    r = io.StringIO(s)
    a = ["<Team></Team>", "<Team></Team>"]
    b = xml_read (r, a)
    self.assertTrue(b == False)
 
  def test_read2 (self) :
    s = "<Team></Team><Team></Team>"
    r = io.StringIO(s)
    a = ["<Team></Team>", "<Team></Team>"]
    b = xml_read (r, a)
    self.assertTrue(b == True)
    
  def test_read3 (self) :
    s = "<Team><cooly></cooly></Team><Apple></Apple>"
    r = io.StringIO(s)
    a = ["<Team></Team>", "<Team></Team>"]
    b = xml_read (r, a)
    self.assertTrue(b == True)
    
    
  # ----
  # write
  # ----
  def test_write1 (self) :
    a = [2, 2, 7]
    s = "3\n2\n2\n7" 
    w = io.StringIO()
    xml_write(w, a)
    d = w.getvalue()
    self.assertTrue(d == s) 

  def test_write2 (self) :
    a = [3, 5, 7]
    s = "3\n3\n5\n7" 
    w = io.StringIO()
    xml_write(w, a)
    d = w.getvalue()
    self.assertTrue(d == s) 

  def test_write3 (self) :
    a = [2, 2, 55, 9, 20]
    s = "5\n2\n2\n55\n9\n20" 
    w = io.StringIO()
    xml_write(w, a)
    d = w.getvalue()
    self.assertTrue(d == s) 

  # ----
  # eval
  # ----
  def test_eval1 (self) :
    a = [fromstring("<Team><cooly><rek></rek></cooly></Team>"), fromstring("<rek></rek>")]
    w = xml_eval(a)
    self.assertTrue(w[0] == 3)
    self.assertTrue(len(w) == 1)

  def test_eval2 (self) :
    a = [fromstring("<Team><cooly><rek></rek></cooly></Team>"), fromstring("<cooly><rek></rek></cooly>")]
    w = xml_eval(a)
    self.assertTrue(w[0] == 2)
    self.assertTrue(len(w) == 1)

  def test_eval3 (self) :
    a = [fromstring("<Team><cooly><rek></rek></cooly></Team>"), fromstring("<apple></apple>")]
    w = xml_eval(a)
    self.assertTrue(len(w) == 0)

  # ----
  # search cannot have tests due to the construction of the code.
  # However, eval tests it fairly well, since it basically acts as a wrapper
  # ----
  
  # ----
  # scan
  # ----
  
  def test_scan1 (self) :
    a = [fromstring("<Team><cooly><rek></rek></cooly></Team>"), fromstring("<rek></rek>")]
    try:
      xml_scan_recur(a[0],a[1])
      # Designed to fail this test
      self.assertTrue(False)
    except:
      self.assertTrue(True)
  
  def test_scan2 (self) :
    a = [fromstring("<Team><cooly><rek></rek></cooly></Team>"), fromstring("<Tear></Tear>")]
    try:
      xml_scan_recur(a[0],a[1])
      # Designed to fail this test
      self.assertTrue(False)
    except:
      self.assertTrue(True)
  
  def test_scan3 (self) :
    a = [fromstring("<Team><cooly><rek></rek></cooly></Team>"), fromstring("<cooly><rek></rek></cooly>")]
    try:
      xml_scan_recur(a[0],a[1])
      # Designed to pass this test
      self.assertTrue(True)
    except:
      self.assertTrue(False)
  
  # ----
  # solve
  # ----
  def test_solve1 (self) :
    a =  "<Team><cooly><rek></rek></cooly></Team><rek></rek>"
    r = io.StringIO(a)
    w = io.StringIO()
    xml_solve(r, w)
    self.assertTrue(w.getvalue() == "1\n3")    

  def test_solve2 (self) :
    a =  "<Team><cooly><rek></rek></cooly></Team><cooly><rek></rek></cooly>"
    r = io.StringIO(a)
    w = io.StringIO()
    xml_solve(r, w)
    self.assertTrue(w.getvalue() == "1\n2")    

  def test_solve3 (self) :
    a =  "<Team><cooly><rek></rek></cooly></Team><ter></ter>"
    r = io.StringIO(a)
    w = io.StringIO()
    xml_solve(r, w)
    self.assertTrue(w.getvalue() == "0")    

# ----
# main
# ----

print("kenon-TestXML.py")
unittest.main()
print("Done")
