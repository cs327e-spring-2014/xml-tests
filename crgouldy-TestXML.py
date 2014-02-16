# -------
# imports
# -------

import io
import unittest

from XML import *#elementCreate, searchXml, iterElement, compareElement, searchFunction
from xml.etree.ElementTree import Element, fromstring, tostring, tostringlist


# -----------
# TestCollatz
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # elementCreate
    # ----

    def test_elementCreate (self) :
        x = "<xml><A><b><c></c></b></A></xml>"
        y = elementCreate(x)
        self.assertTrue(type(y) is Element)
    def test_elementCreate1 (self) :
        x = "<xml></xml>"
        y = elementCreate(x)
        self.assertTrue(type(y) is Element)
    def test_elementCreate2 (self) :
        x = "<xml><A><b><d></d><c></c></b></A></xml>"
        y = elementCreate(x)
        self.assertTrue(type(y) is Element)
    def test_elementCreate3 (self) :
        x = "<xml><A><b><d></d><e><f></f></e><c></c></b></A></xml>"
        y = elementCreate(x)
        self.assertTrue(type(y) is Element)
    # ----
    # searchXml
    # ----

    def test_searchXml (self) :
        xx = "<emu><mez><mer></mer></mez><mac><mez><mer></mer></mez></mac></emu><mez><mer></mer></mez>"
        clearGlobals()
        y = searchXml(xx)
        self.assertTrue(y == [2,5])

    def test_searchXml1 (self) :
        xx = "<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>"
        clearGlobals()
        y = searchXml(xx)
        self.assertTrue(y == [2,7])
    
    def test_searchXml2 (self) :
        xx = "<red><green><blue></blue><yellow></yellow> </green></red><red><green></green></red>"
        clearGlobals()
        y = searchXml(xx)
        self.assertTrue(y == [1])

    def test_searchXml3 (self) :
        xx = "<red><green><blue></blue><yellow></yellow></green></red><red><blue></blue></red>"
        clearGlobals()
        y = searchXml(xx)
        self.assertTrue(y == [])

    # ----
    # iterElement
    # ----

    def test_iterElement (self) :
        xx = "<mez><mer></mer></mez>"
        clearGlobals()
        y = fromstring(xx)
        z = iterElement(y)
        self.assertTrue(z == [("mez", 1),("mer", 2)])

    def test_iterElement1 (self) :
        xx = "<cat><dog></dog><monkey><walrus></walrus><dolphin></dolphin></monkey></cat>"
        clearGlobals()
        y = fromstring(xx)
        z = iterElement(y)
        self.assertTrue(z == [('cat', 1), ('dog', 2), ('monkey', 2), ('walrus', 3), ('dolphin', 3)])

    def test_iterElement2 (self) :
        xx = "<a><b><c></c></b><d></d><e><f></f></e></a>"
        clearGlobals()
        y = fromstring(xx)
        z = iterElement(y)
        self.assertTrue(z == [('a', 1), ('b', 2), ('c', 3), ('d', 2), ('e', 2), ('f', 3)])

    # ----
    # compareElement
    # ----

    def test_compareElement (self) :
        clearGlobals()
        x = fromstring("<mez><mer></mer></mez>")
        y = fromstring("<emu><mez><mer></mer></mez><mac><mez><mer></mer></mez></mac></emu>")
        z = compareElement(y,x)
        self.assertTrue(z == [2,5])


    def test_compareElement1 (self) :
        clearGlobals()
        x = fromstring("<Team><Cooly></Cooly></Team>")
        y = fromstring("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>")
        z = compareElement(y,x)
        self.assertTrue(z == [2,7])

    def test_compareElement2 (self) :
        clearGlobals()
        x = fromstring("<red><blue></blue></red>")
        iterElement(x)
        y = fromstring("<red><green><blue></blue><yellow></yellow></green></red>")
        z = compareElement(y,x)
        self.assertTrue(z == [])
    

    # ----
    # searchFunction
    # ----

    def test_searchFunction (self) :
        x = [("mez", 1),("mer", 2)]
        clearGlobals()
        xx = fromstring("<mez><mer></mer></mez>")
        y = fromstring("<mez><mer></mer></mez>")
        z = searchFunction(y,xx, x)
        self.assertTrue(z == True)

    def test_searchFunction1 (self) :
        x = [("a", 1),("b", 2)]
        clearGlobals()
        xx = fromstring("<a><b></b></a>")
        y = fromstring("<b><a></a></b>")
        z = searchFunction(y,xx, x)

        self.assertTrue(z == False)

    def test_searchFunction2 (self) :
        x = [("a", 1),("b", 2),("c",2),("d",3),("e",3)]
        clearGlobals()
        xx = fromstring("<a><b></b><c><d></d><e></e></c></a>")
        y = fromstring("<a><b></b><c><d></d><e></e></c></a>")
        z = searchFunction(y,xx, x)

        self.assertTrue(z == True)

    # ----
    # sysWriter
    # ----

    def test_sysWriter (self) :
        z = io.StringIO()
        sysWriter(z, [2,7,15,16,49])
        self.assertTrue(z.getvalue() == "5\n2\n7\n15\n16\n49\n")
    def test_sysWriter1 (self) :
        z = io.StringIO()
        sysWriter(z, [])
        self.assertTrue(z.getvalue() == "0\n")
    def test_sysWriter2 (self) :
        z = io.StringIO()
        sysWriter(z, [1,2,40,16,8])
        
        self.assertTrue(z.getvalue() == "5\n1\n2\n40\n16\n8\n")


    # ----
    # XML_solve
    # ----

    def test_XML_solve (self) :
        z = io.StringIO()
        y = io.StringIO("<emu><mez><mer></mer></mez><mac><mez><mer></mer></mez></mac></emu><mez><mer></mer></mez>")
        XML_solve(y,z)
        y.close()
        self.assertTrue(z.getvalue() == "2\n2\n5\n")



    
    
        
# ----
# main
# ----
print("TestXML.py")
unittest.main()
print("Done.")
