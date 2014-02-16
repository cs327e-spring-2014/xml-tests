import io
import unittest

from XML import *



# Testxml
# -----------

class Testxml (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = io.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
        s = "<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>"

        status, sb = xml_read(r, s)
        self.assertTrue(status == True)
        self.assertTrue(sb == s)
    # -----------
# TestXML
# -----------

    # ----
    # xml_solve
    # ----

    def test_xml_solve1 (self):
        z = io.StringIO()
        y = io.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
        xml_solve(y,z)
        y.close()
        self.assertTrue(z.getvalue() == "2\n2\n7\n\n")

    def test_xml_solve2 (self):
        z = io.StringIO()
        y = io.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
        xml_solve(y,z)
        y.close()
        self.assertTrue(z.getvalue() == "2\n2\n7\n\n")

    def test_xml_solve3 (self) :
        z = io.StringIO()
        y = io.StringIO("<mexico><usa><canada></canada><bolivia></bolivia></usa><brazil><france></france><spain></spain></brazil></mexico><brazil><spain></spain></brazil>")
        xml_solve(y,z)
        y.close()
        self.assertTrue(z.getvalue() == "1\n5\n\n")


    # -----
    # print
    # -----

    def test_print1 (self) :
        w = io.StringIO()
        xml_print(w, [1, 10, 20])
        self.assertTrue(w.getvalue() == "1\n10\n20\n\n")

    def test_print2 (self) :
        w = io.StringIO()
        xml_print(w, [2, 20, 33])
        self.assertTrue(w.getvalue() == "2\n20\n33\n\n")
    def test_print3 (self) :
        w = io.StringIO()
        xml_print(w, [134, 60, 590])
        self.assertTrue(w.getvalue() == "134\n60\n590\n\n")

    def test_print4 (self) :
        w = io.StringIO()
        xml_print(w, [1456, 1540, 2230])
        self.assertTrue(w.getvalue() == "1456\n1540\n2230\n\n")

# ----
# main
# ----

print("TestXML.py")
unittest.main()
print("Done.")
