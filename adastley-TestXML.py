#!/usr/bin/env python

from xml.etree.ElementTree import fromstring
from XML import ReferenceType, FindMatchesInElement, CheckChildren, SolveXMLSearch

import StringIO
import unittest


# Class defining various unit tests
class XMLUnitTests(unittest.TestCase):
    # Testing of FindMatchesInElement
    def test_findMatches1(self):
        sourceElement = fromstring("<red><green><blue></blue><yellow></yellow></green></red>")
        searchPatternElement = fromstring("<green><yellow></yellow></green>")
        matches = []
        FindMatchesInElement(sourceElement, searchPatternElement, ReferenceType(1), matches)
        answer = [2]
        self.assert_(len(answer) == len(matches) and all(answer[i] == matches[i] for i in range(len(answer)-1)))

    def test_findMatches2(self):
        sourceElement = fromstring("<red><green><blue></blue><yellow></yellow></green></red>")
        searchPatternElement = fromstring("<green><blue></blue></green>")
        matches = []
        FindMatchesInElement(sourceElement, searchPatternElement, ReferenceType(1), matches)
        answer = [2]
        self.assert_(len(answer) == len(matches) and all(answer[i] == matches[i] for i in range(len(answer)-1)))

    def test_findMatches3(self):
        sourceElement = fromstring("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>")
        searchPatternElement = fromstring("<Team><Cooly></Cooly></Team>")
        matches = []
        FindMatchesInElement(sourceElement, searchPatternElement, ReferenceType(1), matches)
        answer = [2, 7]
        self.assert_(len(answer) == len(matches) and all(answer[i] == matches[i] for i in range(len(answer)-1)))

    # Testing of CheckChildren
    def test_checkChildren1(self):
        sourceElement = fromstring("<green><blue></blue><yellow></yellow></green>")
        searchPatternElement = fromstring("<green><yellow></yellow></green>")
        self.assert_(CheckChildren(sourceElement, searchPatternElement))

    def test_checkChildren2(self):
        sourceElement = fromstring("<Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team>")
        searchPatternElement = fromstring("<Team><Dragon></Dragon></Team>")
        self.assert_(not CheckChildren(sourceElement, searchPatternElement))

    def test_checkChildren3(self):
        sourceElement = fromstring("<Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team>")
        searchPatternElement = fromstring("<Team><Cooly></Cooly></Team>")
        self.assert_(CheckChildren(sourceElement, searchPatternElement))

    # Testing of the entire process
    def test_solve1(self):
        r = StringIO.StringIO("<red><green><blue></blue><yellow></yellow></green></red><red><green></green></red>")
        w = StringIO.StringIO()
        SolveXMLSearch(r, w)
        self.assert_(w.getvalue() == "1\n1\n")

    def test_solve2(self):
        r = StringIO.StringIO("<red><green><blue></blue><yellow></yellow></green></red><green><blue></blue></green>")
        w = StringIO.StringIO()
        SolveXMLSearch(r, w)
        self.assert_(w.getvalue() == "1\n2\n")

    def test_solve3(self):
        r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        SolveXMLSearch(r, w)
        self.assert_(w.getvalue() == "2\n2\n7\n")


# Call the test
unittest.main()