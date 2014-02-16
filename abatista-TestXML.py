#!/usr/bin/env python3

import io
import unittest

from XML import get_query_pattern

class TestXML (unittest.TestCase):
    
    def test_get_query1(self):
       s = "<red><green><blue></blue><grey></grey><fish></fish><yellow></yellow><grey></grey><fish></fish><blue></blue></green><fusia><green><blue><fish></fish></blue></green></fusia></red><green><yellow></yellow></green>"
       pattern = get_query_pattern(s)
       self.assertTrue(pattern[0]=="green" and pattern[1] == "yellow")

    def test_get_query2(self):
       s = "<red><green><blue></blue></green></red><green><azul></azul><yellow></yellow></green>"
       pattern = get_query_pattern(s)
       self.assertTrue(pattern[0]=="green" and pattern[1] == "azul" and pattern[2] == "yellow")

    def test_get_query3(self):
       s = "<red><green><blue></blue><grey></grey><fish></fish><yellow></yellow><grey></grey><fish></fish><blue></blue></green><fusia><green><blue><fish></fish></blue></green></fusia></red><green><yellow><rojo></rojo></yellow><verde></verde></green>"
       pattern = get_query_pattern(s)
       self.assertTrue(pattern[0]=="green" and pattern[1] == "yellow" and pattern[2] == "rojo" and pattern[3] == "verde")

unittest.main()
print("Done")
