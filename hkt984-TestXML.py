import xml.etree.ElementTree as et
import io
import unittest
from XML import xml_Eval, xml_Express, xml_Read

file1 = "<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>"

file2 = "<THU>\n<yolo>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</yolo>\n</THU>\n<Team><Cooly></Cooly></Team>"

file3 = "<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<JiaJia><Team></JiaJia></Team>"

class TestXML (unittest.TestCase) :

    # -------
    # xml_Eval
    # -------

    def test_xml_Eval1(self) :
        u = et.fromstring("<Team></Team>")
        v = et.fromstring("<Team></Team>")
        result = xml_Eval(u,v)
        self.assertTrue(result == [1,1])

    def test_xml_Eval2(self) :
        u = et.fromstring("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n"\
        + "</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon>"\
        + "</Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n"\
        + "</THU>")
        v = et.fromstring("<Team><Cooly></Cooly></Team>")
        result = xml_Eval(u,v)
        self.assertTrue(result == [2,2,7])

    def test_xml_Eval3(self) :
        u = et.fromstring("<Team><Cooly></Cooly></Team>")
        v = et.fromstring("<Team></Team>")
        result = xml_Eval(u,v)
        self.assertTrue(result == [1,1])

    # ---------
    # xml_Express
    # ---------

    def test_xml_Express1 (self) :
        query = "<T></T>"
        queryroot = et.fromstring(query)
        result = xml_Express(queryroot)
        self.assertTrue(result == ".//T")

    def test_xml_Express2 (self) :
        query = "<T> <C> <D> </D> </C> </T>"
        queryroot = et.fromstring(query)
        result = xml_Express(queryroot)
        self.assertTrue(result == ".//T/C/D/../..")

    def test_xml_Express3 (self) :
        query = "<T> <C> </C> <D> </D> </T>"
        queryroot = et.fromstring(query)
        result = xml_Express(queryroot)
        self.assertTrue(result == ".//T/C/../D/..")
        

    # -------
    # xml_Read
    # -------

    # may have to remove \n from the assert statements

    def test_xml_Read1 (self) :
        r = io.StringIO(file1)
        w = xml_Read(r)
        self.assertTrue(w == "<XML>" + file1 + "</XML>")
    def test_xml_Read2 (self) :
        r = io.StringIO(file2)
        w = xml_Read(r)
        self.assertTrue(w == "<XML>" + file2 + "</XML>")
    def test_xml_Read3 (self) :
        r = io.StringIO(file3)
        w = xml_Read(r)
        self.assertTrue(w == "<XML>" + file3 + "</XML>")



print ("TestXML.py")
unittest.main()
print ("Done.")
