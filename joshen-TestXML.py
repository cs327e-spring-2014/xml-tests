#!/usr/bin/env python3

# ----------
# TestXML.py
# ----------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.out
"""

# -------
# imports
# -------

import io
import unittest

from XML import xml_buildlist, xml_compare, xml_comparehelper, xml_searchpattern, xml_read, xml_solve, xml_print

from xml.etree.ElementTree import Element, fromstring

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    
    # --------
    # xml_read
    # --------

    def test_read (self) :
        r = io.StringIO("<Team><Cooly></Cooly></Team>")
        b = xml_read(r)
        self.assertTrue("<xml><Team><Cooly></Cooly></Team></xml>")
        
    def test_read_2 (self) :
        r = io.StringIO("<Dragon></Dragon><Colly></Colly>")
        b = xml_read(r)
        self.assertTrue("<xml><Dragon><Cooly></Dragon></Colly></xml>")
        
    def test_read_3(self):
        r = io.StringIO("<Cooly><Team></Team></Cooly>")
        b=xml_read(r)
        self.assertTrue("<Cooly><Team></Team></Team></xml>")

    # ---------
    # xml_solve
    # ---------
        
    def test_solve_1(self):
        r = io.StringIO('<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>\n<Team><Cooly></Cooly></Team>')
        w = io.StringIO()
        xml_solve(r, w)
        self.assertTrue(w.getvalue() == "2\n2\n7\n")
    
    def test_solve_2(self):
        r = io.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>\n<Team><Cooly></Cooly><Dragon></Dragon></Team>" )
        w = io.StringIO()
        xml_solve(r, w)
        self.assertTrue(w.getvalue() == "1\n7\n")
        
    def test_solve_3(self):
        r = io.StringIO("<stuff>\n<what>\n<bees>\n<junk>\n</junk>\n</bees>\n</what>\n</stuff>\n<what><junk></junk></what>")
        w = io.StringIO()
        xml_solve(r,w)
        self.assertTrue(w.getvalue() == "0\n")
    
    def test_solve_4(self):
        r = io.StringIO("<cool>\n</cool>\n<Cool></Cool>")
        w = io.StringIO()
        xml_solve(r,w)
        self.assertTrue(w.getvalue() == "0\n")
    
    def test_solve_5(self):
        r = io.StringIO("<cool>\n</cool>\n<no></no>")
        w = io.StringIO()
        xml_solve(r,w)
        self.assertTrue(w.getvalue() == "0\n")
        
    def test_solve_6(self):
        r = io.StringIO("<never>\n</never>\n<never></never>")
        w = io.StringIO()
        xml_solve(r,w)
        self.assertTrue(w.getvalue() == "1\n1\n")
    
    def test_solve7(self):
        r = io.StringIO("<cool>\n<what>\n<travel>\n</travel>\n</what>\n</cool>\n<travel></travel>")
        w = io.StringIO()
        xml_solve(r,w)
        self.assertTrue(w.getvalue() == "1\n3\n")
        
    def test_solve8(self):
        r = io.StringIO("<cool>\n<what>\n<travel>\n</travel>\n</what>\n</cool>\n<travel></travel>")
        w = io.StringIO()
        xml_solve(r,w)
        self.assertTrue(w.getvalue() == "1\n3\n")

    # -------------
    # xml_buildlist
    # -------------

    def test_buildlist1(self):
        x = fromstring("<xml><THU><Team><ACRush></ACRush><Jelly>" \
                       + "</Jelly><Cooly></Cooly></Team><JiaJia>" \
                       + "<Team><Ahyangyi></Ahyangyi><Dragon></Dragon>"  \
                       + "<Cooly><Amber></Amber></Cooly></Team></JiaJia>" \
                       + "</THU><Team><Cooly></Cooly></Team></xml>")
        L = [i for i in x[0].iter() if i.tag == 'Cooly']
        B = xml_buildlist('Cooly', x)
        for i in B:
            self.assertTrue(i in L)    

        
    # -----------------
    # xml_searchpattern
    # -----------------

    def test_searchPattern_1(self):
        x = fromstring('<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>\n<Team><Cooly></Cooly></Team></xml>')
        v = xml_searchpattern(x)
        self.assertTrue(v == [2,2,7])
        
    def test_searchPattern_2(self):
        x = fromstring('<xml><a><b><e></e><d></d></b></a><b><d></d></b></xml>')
        v = xml_searchpattern(x)
        self.assertTrue(v ==[1,2])
    
    def test_searchPattern_3(self):
        x = fromstring('<xml><red><green><blue></blue><yellow></yellow></green></red><green><yellow></yellow><blue></blue></green></xml>')
        v = xml_searchpattern(x)
        self.assertTrue(v ==[1,2])
        
    def test_searchPattern_4(self):
        x = fromstring('<xml><red><green><blue></blue><yellow></yellow></green></red><green><purple></purple></green></xml>')
        v = xml_searchpattern(x)
        self.assertTrue(v ==[0])
    
    def test_searchPattern_5(self):
        x = fromstring('<xml><cool>\n</cool>\n<no></no></xml>')
        v = xml_searchpattern(x)
        self.assertTrue(v ==[0])
        
    def test_searchPattern_6(self):
        x = fromstring('<xml>"<cool>\n</cool>\n<Cool></Cool>"</xml>')
        v = xml_searchpattern(x)
        self.assertTrue(v ==[0])

    # -----------
    # xml_compare
    # -----------
      
    def test_compare_1(self):
        x = fromstring('<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>\n<Team><Cooly></Cooly></Team></xml>')
        a = x[0][0]
        b = x[1]
        v = xml_compare(a,b)
        self.assertTrue(v == None)

    # ------------------
    # xml_comparehelpter
    # ------------------
        
    def test_compareHelper_1(self):
        x = fromstring('<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>\n<Team><Cooly></Cooly></Team></xml>')
        a = [i for i in x[0][0]]
        b = [j for j in x[0][1][0]]
        v = xml_comparehelper(a,b)
        self.assertTrue(v == False)

    # ---------
    # xml_print
    # ---------
    
    def test_print_1(self):
        w = io.StringIO()
        a = [5, 6, 7, 8]
        xml_print(a, w)
        self.assertTrue(w.getvalue() == "5\n6\n7\n8\n")
        
    def test_print_2(self):
        w = io.StringIO()
        a = [3,5,75,4,3,5]
        xml_print(a, w)
        self.assertTrue(w.getvalue() == "3\n5\n75\n4\n3\n5\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
