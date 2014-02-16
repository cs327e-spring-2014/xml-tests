"""
To test the program:
    % python TestCollatz.py > TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py > TestCollatz.out
"""

# -------
# imports
# -------

import io
import unittest

from XML import XML_read, XML_counter, XML_query_add, XML_make_query_string, XML_find, XML_print, test_print, XML_solve 
from xml.etree.ElementTree import fromstring
import XML




# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) : 
    # ----
    # read
    #Checks if XML reads in a and splits into query and input
    # ----

    def test_read (self) : #tests if tag is split and if tag of a is 'xml' 
        r = "<xml><red><green><blue></blue><yellow></yellow></green></red><red><green></green></red></xml>"
        a = fromstring(r)
        b,c = XML_read(a)
        self.assertTrue(b.tag == "xml")
        self.assertTrue(c.tag == "red")

    def test_read_1 (self) : #checks if polly is the tag of the input and no is tag of query
        r = "<polly><no><yay><blue></blue><yellow></yellow></yay></no><no><yay></yay></no></polly>"
        a = fromstring(r)
        b,c = XML_read(a)
        self.assertTrue(b.tag == "polly")
        self.assertTrue(c.tag == "no")

    def test_read_2 (self) : #Checks if splits even if query not in input
        r = "<xml><blue></blue><green></green></xml>"
        a = fromstring(r)
        b,c = XML_read(a)
        self.assertTrue(b.tag == "xml")
        self.assertTrue(c.tag == "green")
        

    # ----
    # counter
    #Checks if XML_counter adds the position number to each element as a text attribute
    # ----

    def test_counter_1 (self) : #Checks if the text of the first element in input ('no') is 1
        r = "<polly><no><yay><blue></blue><yellow></yellow></yay></no></polly>"
        a = fromstring(r)
        v = XML_counter(a)
        p = a.iter()
        v = next(p)
        v = next(p)
        self.assertTrue(v.text == 1)
        
        
    def test_counter_2 (self) :# checks if the text of the sixth element 'what' is 6
        r = "<polly><no><yay><blue></blue><yellow></yellow></yay></no><what></what></polly>"
        a = fromstring(r)
        v = XML_counter(a)
        p = a.iter()
        v = next(p)
        v= next(p)
        v= next(p)
        self.assertTrue(v.text == 6)
        

    def test_counter_3 (self) : #checks if no count text is added to 'polly', the root element
        r = "<polly><no><yay></yay></no><yellow></yellow></polly>"
        a = fromstring(r)
        v = XML_counter(a)
        self.assertTrue(a.text == None)



##    # -----
##    # XML_query_add: Checks if query is turned into a list
##    # -----
##
    def test_query_add_1 (self) : 
        s = "<polly><no><yay></yay></no><yellow></yellow></polly>" 
        v= fromstring(s)
        a = XML_query_add(v)
        self.assertTrue(a == ["polly","no","yay","/yay","/no","yellow","/yellow","/polly"])
        XML.query = []
##
    def test_query_add_2(self) :
        query =[]
        s = "<polly><no><yay></yay></no></polly>"
        v= fromstring(s)
        a = XML_query_add(v)
        self.assertTrue(a == ["polly","no","yay","/yay","/no","/polly"])
        XML.query = []
##
    def test_query_add_3(self) :
        s = "<polly></polly>"
        v= fromstring(s)
        a = XML_query_add(v)
        self.assertTrue(a == ["polly","/polly"])
        XML.query = []
##
    def test_query_add_4 (self) :
        s = "<bad><y></y></bad>"
        v= fromstring(s)
        a = XML_query_add(v)
        self.assertTrue(a == ["bad","y","/y","/bad"])
        XML.query = []
##        
##
##
##
##    # -----
##    # XML_make_query_string: checks if query list is turned into a proper Xpath string for searching
##    # -----
##
    def test_make_query_string_1 (self) : #checks if the parent/child relationship is preserved in conversion
        XML.query = ["bad","y","/y","/bad"]
        XML.query_string = ".//"
        b = XML_make_query_string()
        self.assertTrue (b == ".//bad/y/....")
        XML.query = []
        XML.query_string = ".//"
        
    def test_make_query_string_2 (self) : #checks if the parent/child.sibling relationship is preserved in conversion
        XML.query = ["polly","no","yay","/yay","/no","yellow","/yellow","/polly"]
        XML.query_string = ".//"
        b = XML_make_query_string()
        self.assertTrue (b == ".//polly/no/yay/....yellow/....")
        XML.query = []
        XML.query_string = ".//"

    def test_make_query_string_3 (self) : #checks if the parent element is signiied as such after conversion
        XML.query = ["polly","/polly"]
        XML.query_string = ".//"
        b = XML_make_query_string()
        self.assertTrue (b == ".//polly")
        XML.query = []
        XML.query_string = ".//"
        
    def test_make_query_string_4 (self) : #checks if the parent/child/grandchild relationship is preserved in conversion
        XML.query = ["polly","sally","dolly","/dolly","/sally","/polly"]
        XML.query_string = ".//"
        b = XML_make_query_string()
        self.assertTrue (b == ".//polly/sally/dolly/......")
        XML.query = []
        XML.query_string = ".//"



      # -----
##    # XML_find: checks if the position number of the query in the input is correct and added to query_position list
##    # -----

    def test_find_1 (self) : #checks if the position of the first element of the pattern is added to the list
        XML.query_string= ".//polly/sally/dolly/......"
        XML.query = ["polly","sally","dolly","/dolly","/sally","/polly"]
        XML.query_position = []
        r = "<xml><tilly>1<polly>2<sally>3<dolly>4<molly>5</molly></dolly></sally></polly></tilly></xml>"
        a = fromstring(r)
        d = XML_find(a)
        self.assertTrue(d ==['2'])
        XML.query = []
        XML.query_string = ".//"
        XML.query_position = []

    def test_find_2 (self) : #checks if the positions of the pattern's multiple occurrences are returned to the list
        XML.query_string= ".//Team/Cooly/...."
        XML.query = ["Team","Cooly","/Team","/Cooly"]
        XML.query_position = []
        r = "<xml><Team>1<Cooly>2<Team>3<Cooly>4<Tealy>5</Tealy></Cooly></Team></Cooly></Team></xml>"
        a = fromstring(r)
        d = XML_find(a)
        self.assertTrue(d ==['1','3'])
        XML.query = []
        XML.query_string = ".//"
        XML.query_position = []

    def test_find_3 (self) : #checks if the position number is returned even if the pattern order is different from that of the query
        XML.query_string= ".//BestFriend/Frenemy/..Enemy/...."
        XML.query = ["BestFriend","Frenemy","/Frenemy","Enemy","/Enemy","/BestFriend"]
        XML.query_position = []
        r = "<xml><Acquaintance>2<BestFriend>3<Enemy>4</Enemy><Frenemy>5</Frenemy></BestFriend></Acquaintance></xml>"
        a = fromstring(r)
        d = XML_find(a)
        self.assertTrue(d ==['3'])
        XML.query = []
        XML.query_string = ".//"
        XML.query_position = []
        
    def test_find_4(self) : #checks if a query not present in the input returns an empty list
        XML.query_string= ".//BestFriend"
        XML.query = ["BetFriend","/BetFriend"]
        XML.query_position = []
        r = "<xml><Acquaintance>2<BestFriend>3<Enemy>4</Enemy><BestFriend>5</BestFriend></BestFriend></Acquaintance></xml>"
        a = fromstring(r)
        d = XML_find(a)
        self.assertTrue(d ==[])
        XML.query = []
        XML.query_string = ".//"
        XML.query_position = []




           # -----
##    # XML_print: checks if prints out the output in the specified order (checks if the list test_print provides the correct values)
##    # -----
    def test_print_1(self):
        XML.query_position = ['3','4','5']
        w = test_print()
        self.assertTrue(w == [3,'3','4','5'])
        XML.query_position = []


# -----
##    # test_print: checks if test_print gives out correct values for unit testing
##    # -----
    def test_test_print_1(self):
        XML.query_position = ['3','4','5']
        w = test_print()
        self.assertTrue(w == [3,'3','4','5'])
        XML.query_position = []
        XML.query = []




    # -----
##    # XML_solve: checks if solve outputs the correct positions of query
##    # -----
    def test_solve(self):
        XML.query_position = []
        XML.query = []
        XML.query_string = ""
        XML.counter_elem_number = 1
        s= "<red><green></green></red><red><green></green></red>"
        a = XML_solve(s)
        self.assertTrue(a == [1,1])
        XML.query_position = []
        XML.query = []
        XML_query_string = ""

        
##
### ----
### main
### ----

print("TestCollatz.py")
unittest.main()
print("Done.")
