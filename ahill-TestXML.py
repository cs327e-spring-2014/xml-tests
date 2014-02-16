#!/usr/bin/env python3

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

from xml.etree.ElementTree import Element, fromstring, tostring
from XML import new_tree, xml_solver, xml_print, traverse, package, purge, matcher
global level


# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # new_tree
    # ----
    
    def test_new_tree_1 (self) :
        r = '<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangi></Ahyangi>\
<Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU></xml><Team><Cooly></Cooly></Team>'
        tree, query = new_tree(r)
        self.assertTrue(type(tree) is Element)
        self.assertTrue(type(query) is Element)

    def test_new_tree_2 (self) :
        r = '<xml><THU><Team><Cooly></Cooly></Team><JiaJia><Team>\
<Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU></xml><Team><Cooly></Cooly></Team>'
        tree, query = new_tree(r)
        self.assertTrue(type(tree) is Element)
        self.assertTrue(type(query) is Element)

    def test_new_tree_3 (self) :
        r ='<xml><rl></rl><cwkb></cwkb><puk><deoh><ii><zwb><izdr><i><rdca><wmtr>\
</wmtr>\
<t>\
<bc>\
</bc>\
</t>\
<qbms>\
</qbms>\
<ikn>\
</ikn>\
<stuk>\
<fo>\
</fo>\
<gaqp>\
<r>\
</r>\
<qk>\
<ptm>\
</ptm>\
</qk>\
</gaqp>\
<g>\
</g>\
<ewsu>\
</ewsu>\
</stuk>\
<na>\
<vu>\
</vu>\
<u>\
<pl>\
</pl>\
</u>\
<wubr>\
</wubr>\
<xjbq>\
</xjbq>\
<anb>\
<srp>\
</srp>\
</anb>\
<jrd>\
<xkpv>\
<ekv>\
<y>\
</y>\
</ekv>\
<xrx><se>\
<s>\
<g>\
<kl>\
<i>\
<pie>\
</pie>\
<ql>\
</ql>\
</i>\
<xvvx>\
</xvvx>\
</kl>\
</g>\
</s>\
</se>\
</xrx>\
<osv>\
</osv>\
</xkpv>\
<psm>\
</psm>\
<pupt>\
</pupt>\
<td>\
<lg>\
</lg>\
</td>\
<jd>\
<qslt>\
<fh>\
</fh>\
<appz>\
<hqiy>\
</hqiy>\
</appz>\
<xw>\
<tdfu>\
</tdfu>\
</xw>\
</qslt>\
</jd>\
</jrd>\
</na>\
</rdca>\
</i>\
</izdr>\
</zwb>\
</ii>\
</deoh>\
</puk>\
</xml>\
<i><rdca></rdca></i>'
        tree, query = new_tree(r)
        self.assertTrue(type(tree) is Element)
        self.assertTrue(type(query) is Element)

    # -----
    # print
    # -----

    def test_xml_print (self) :
        w = io.StringIO()
        xml_print([2, 4, 7, 19],w)
        self.assertTrue(w.getvalue() == "4\n2\n4\n7\n19\n")

    def test_xml_print_2 (self) :
        w = io.StringIO()
        xml_print([2, 4, 7, 19, 34, 1],w)
        self.assertTrue(w.getvalue() == "6\n2\n4\n7\n19\n34\n1\n")

    def test_xml_print_3 (self) :
        w = io.StringIO()
        xml_print([],w)
        self.assertTrue(w.getvalue() == "0\n")



    # ----
    # purge
    # ----

    def test_purge_1 (self):
        XML.level = 1
        r = '<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangi></Ahyangi>\
<Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU></xml><Team><Cooly></Cooly></Team>'
        tree, query = new_tree(r)
        bigmap = traverse(tree, [], None)
        lookinfor = traverse(query, [], None)
        biglist = package(bigmap,lookinfor)

        biglist = purge(lookinfor, biglist)
        self.assertTrue(type(biglist) is list)
        self.assertTrue(type(biglist[0]) is list)
        self.assertTrue(type(biglist[0][0]) is list)
        self.assertTrue(type(biglist[0][0][0]) is Element)
        self.assertTrue(type(biglist[0][0][1]) is int)
        self.assertTrue(biglist[0][0][1] == 3)
        self.assertTrue(type(biglist[0][0][2]) is (Element or NoneType))
        self.assertTrue(type(biglist[0][0][3]) is int)
        self.assertTrue(biglist[0][0][3] == 3)

    def test_purge_2 (self):
        XML.level = 1
        r = '<xml><team><team><joe><cooly><team><cooly></cooly></team></cooly></joe></team></team></xml>\
<team><cooly></cooly></team>'
        tree, query = new_tree(r)
        bigmap = traverse(tree, [], None)
        lookinfor = traverse(query, [], None)
        biglist = package(bigmap,lookinfor)

        biglist = purge(lookinfor, biglist)
        self.assertTrue(type(biglist) is list)
        self.assertTrue(type(biglist[0]) is list)
        self.assertTrue(type(biglist[0][0]) is list)
        self.assertTrue(type(biglist[0][0][0]) is Element)
        self.assertTrue(type(biglist[0][0][1]) is int)
        self.assertTrue(biglist[0][0][1] == 2)
        self.assertTrue(biglist[1][0][0] == 'r')
        self.assertTrue(biglist[1][1][1] == 7)
        self.assertTrue(type(biglist[0][0][2]) is (Element or NoneType))
        self.assertTrue(type(biglist[0][0][3]) is int)
        self.assertTrue(biglist[0][0][3] == 2)
        self.assertTrue(biglist[1][0][0] == 'r')
        self.assertTrue(biglist[1][1][3] == 7)

    def test_purge_3 (self):
        XML.level = 1
        r = '<xml><team><cooly></cooly></team><team><team><cooly><cooly></cooly></cooly>\
</team><cooly></cooly></team></xml><team><cooly></cooly></team>'
        tree, query = new_tree(r)
        bigmap = traverse(tree, [], None)
        lookinfor = traverse(query, [], None)
        biglist = package(bigmap,lookinfor)

        biglist = purge(lookinfor, biglist)
        self.assertTrue(type(biglist) is list)
        self.assertTrue(type(biglist[0]) is list)
        self.assertTrue(type(biglist[0][0]) is list)
        self.assertTrue(type(biglist[0][0][0]) is Element)
        self.assertTrue(type(biglist[0][0][1]) is int)
        self.assertTrue(biglist[0][0][1] == 2)
        self.assertTrue(biglist[1][0][1] == 3)
        self.assertTrue(biglist[1][2][0] == 'r')
        self.assertTrue(type(biglist[0][0][2]) is (Element or NoneType))
        self.assertTrue(type(biglist[0][0][3]) is int)
        self.assertTrue(biglist[0][0][3] == 2)
        self.assertTrue(biglist[1][0][3] == 3)
        self.assertTrue(biglist[1][2][0] == 'r')



    # ----
    # matcher
    # ----

    def test_matcher_1 (self):
        XML.level = 1
        r = '<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangi></Ahyangi>\
<Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU></xml><Team><Cooly></Cooly></Team>'
        tree, query = new_tree(r)
        bigmap = traverse(tree, [], None)
        lookinfor = traverse(query, [], None)
        biglist = package(bigmap,lookinfor)
        biglist = purge(lookinfor, biglist)
        occurrences = matcher(lookinfor, biglist)
        self.assertTrue(type(occurrences) is list)
        self.assertTrue(occurrences[0] == 3)
        self.assertTrue(occurrences[1] == 8)
        
    def test_matcher_2 (self):
        XML.level = 1
        r = '<xml><left><meow><right><meow></meow></right></meow><right><meow></meow></right></left>\
</xml><right><meow></meow></right>'
        tree, query = new_tree(r)
        bigmap = traverse(tree, [], None)
        lookinfor = traverse(query, [], None)
        biglist = package(bigmap,lookinfor)
        biglist = purge(lookinfor, biglist)
        occurrences = matcher(lookinfor, biglist)
        self.assertTrue(type(occurrences) is list)
        self.assertTrue(occurrences == [4,6])
        
    def test_matcher_3 (self):
        XML.level = 1
        r = '<xml><emu><mez><mer><lev></lev></mer></mez><sui><mez><mer></mer></mez></sui><mac><mez><mer>\
<lev></lev></mer></mez></mac><ess><mez></mez></ess><ops></ops></emu></xml><mez><mer><lev></lev></mer></mez>'
        tree, query = new_tree(r)
        bigmap = traverse(tree, [], None)
        lookinfor = traverse(query, [], None)
        biglist = package(bigmap,lookinfor)
        biglist = purge(lookinfor, biglist)
        occurrences = matcher(lookinfor, biglist)
        self.assertTrue(type(occurrences) is list)
        self.assertTrue(occurrences == [3,10])



    # ----
    # package
    # ----

    def test_package_1 (self):
        XML.level = 1
        r = '<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangi></Ahyangi>\
<Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU></xml><Team><Cooly></Cooly></Team>'
        tree, query = new_tree(r)
        bigmap = traverse(tree, [], None)
        lookinfor = traverse(query, [], None)

        biglist = package(bigmap,lookinfor)
        self.assertTrue(type(biglist) is list)
        self.assertTrue(type(biglist[0]) is list)
        self.assertTrue(type(biglist[0][0]) is list)
        self.assertTrue(type(biglist[0][0][0]) is Element)
        self.assertTrue(type(biglist[0][0][1]) is int)
        self.assertTrue(biglist[0][0][1] == 3)
        self.assertTrue(type(biglist[0][0][2]) is (Element or NoneType))
        self.assertTrue(type(biglist[0][0][3]) is int)
        self.assertTrue(biglist[0][0][3] == 3)


    def test_package_2 (self):
        XML.level = 1
        r = '<xml><team><team><team><cooly></cooly></team></team></team></xml><team></team>'
        tree, query = new_tree(r)
        bigmap = traverse(tree, [], None)
        lookinfor = traverse(query, [], None)

        biglist = package(bigmap,lookinfor)
        self.assertTrue(type(biglist) is list)
        self.assertTrue(type(biglist[0]) is list)
        self.assertTrue(type(biglist[0][0]) is list)
        self.assertTrue(type(biglist[0][0][0]) is Element)
        self.assertTrue(type(biglist[0][0][1]) is int)
        self.assertTrue(biglist[0][0][1] == 2)
        self.assertTrue(type(biglist[0][0][2]) is (Element or NoneType))
        self.assertTrue(type(biglist[0][0][3]) is int)
        self.assertTrue(biglist[0][0][3] == 2)

    def test_package_3 (self):
        XML.level = 1
        r = '<red><green><blue></blue><yellow></yellow></green></red>\
<yellow><purple></purple></yellow>'
        tree, query = new_tree(r)
        bigmap = traverse(tree, [], None)
        lookinfor = traverse(query, [], None)

        biglist = package(bigmap,lookinfor)
        self.assertTrue(type(biglist) is list)
        self.assertTrue(type(biglist[0]) is list)
        self.assertTrue(type(biglist[0][0]) is list)
        self.assertTrue(type(biglist[0][0][0]) is Element)
        self.assertTrue(type(biglist[0][0][1]) is int)
        self.assertTrue(biglist[0][0][1] == 3)
        self.assertTrue(type(biglist[0][0][2]) is (Element or NoneType))
        self.assertTrue(type(biglist[0][0][3]) is int)
        self.assertTrue(biglist[0][0][3] == 4)


    # ----
    # traverse
    # ----

    def test_traverse_1 (self):
        XML.level = 1
        s = '<xml><xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangi></Ahyangi>\
<Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU></xml><Team><Cooly></Cooly></Team></xml>'
        x = fromstring(s)
        I = iter(x)
        elem = next(I)
        listA = []
        Dad = None
        biglist = traverse(elem, listA, Dad)
        self.assertTrue(type(biglist) is list)
        self.assertTrue(type(biglist[0]) is list)
        self.assertTrue(type(biglist[0][0]) is Element)
        self.assertTrue(type(biglist[0][1]) is int)

    def test_traverse_2 (self):
        XML.level = 1
        s = '<xml><xml></xml></xml>'
        x = fromstring(s)
        I = iter(x)
        elem = next(I)
        listA = []
        Dad = None
        biglist = traverse(elem, listA, Dad)
        self.assertTrue(type(biglist) is list)
        self.assertTrue(type(biglist[0]) is list)
        self.assertTrue(type(biglist[0][0]) is Element)
        self.assertTrue(type(biglist[0][1]) is int)
        

    def test_traverse_3 (self):
        XML.level = 1
        s = '<xml><xml><xml><xml><xml><xml><xml><xml><xml></xml></xml></xml></xml></xml></xml></xml></xml></xml>'
        x = fromstring(s)
        I = iter(x)
        elem = next(I)
        listA = []
        Dad = None
        biglist = traverse(elem, listA, Dad)
        self.assertTrue(type(biglist) is list)
        self.assertTrue(type(biglist[0]) is list)
        self.assertTrue(type(biglist[0][0]) is Element)
        self.assertTrue(type(biglist[0][1]) is int)


    # -----
    # solver
    # -----

    def test_xml_solver_1(self):
        global occurrences, position, found_position, top
        w = io.StringIO()
        r = io.StringIO('<THU><Team><ACRush></ACRush><Ahyangi></Ahyangi><Cooly></Cooly>\
</Team><JiaJia><Team><Jelly></Jelly><Dragon></Dragon><Cooly><Amber></Amber>\
</Cooly></Team></JiaJia></THU><Team><Ahyangi></Ahyangi></Team>')
        xml_solver(r,w)
        self.assertTrue(w.getvalue() == '1\n2\n')

    def test_xml_solver_2(self):
        global occurrences, position, found_position, top
        w = io.StringIO()
        r = io.StringIO('<strangetree><level1><round1></round1><round2>\
</round2><round3><level2><base1><random>\
</random></base1></level2></round3><round4></round4></level1><level2><base1>\
</base1><base2></base2><base3><level2><base1><random></random>\
</base1></level2></base3><base4></base4></level2><level3><boom1>\
</boom1><boom2></boom2><level2><base1><random></random>\
</base1></level2><boom3></boom3><boom4></boom4></level3>\
<level4></level4></strangetree><level2><base1><random></random></base1></level2>')
        xml_solver(r,w)
        self.assertTrue(w.getvalue() == '3\n6\n14\n21\n')

    def test_xml_solver_3(self):
        global occurrences, position, found_position, top
        w = io.StringIO()
        r = io.StringIO('<THU><Team><ACRush></ACRush><Ahyangi></Ahyangi><Cooly></Cooly>\
</Team><JiaJia><Team><Jelly></Jelly><Dragon></Dragon><Cooly><Amber></Amber>\
</Cooly></Team></JiaJia></THU><Tea><Ahyangi></Ahyangi></Tea>')
        xml_solver(r,w)
        self.assertTrue(w.getvalue() == '0\n')
        

# ----
# main
# ----

print("TestXML.py")
unittest.main()
print("Done.")
