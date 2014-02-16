
#!/usr/bin/env python3

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

from xml.etree.ElementTree import Element, fromstring, tostring

from XML import xml_read,xml_element, xml_query, xml_eval, xml_solve, xml_print, assign_location

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = io.StringIO("<Chocolate><Cake></Cake></Chocolate>")
        a = ['']
        b = xml_read (r,a)
        self.assertTrue(b == True)
        self.assertTrue(a[0] == "<Chocolate><Cake></Cake></Chocolate>")
        
    def test_read_2 (self) :
        r = io.StringIO("<Cookies>/n/t<Thin Mints></Thin Mints>/n/t<Samoas></Samoas>/n</Cookies>")
        a = ['']
        b = xml_read (r,a)
        self.assertTrue(b == True)
        self.assertTrue(a[0] == "<Cookies>/n/t<Thin Mints></Thin Mints>/n/t<Samoas></Samoas>/n</Cookies>")

    def test_read_3 (self) :
        r = io.StringIO("<Dates><Nineties>/t/t</Nineties><Eighties>/t</Eighties></Dates>")
        a = ['']
        b = xml_read (r,a)
        self.assertTrue(b == True)
        self.assertTrue(a[0] == "<Dates><Nineties>/t/t</Nineties><Eighties>/t</Eighties></Dates>")
        
        
        
        
    # ----
    # element
    # ----

    def test_element (self) :

        b = xml_element ("<Test><Longhorn></Longhorn></Test>")
        self.assertTrue(type(b) is Element)

    def test_element_2 (self) :
        
        b = xml_element ("<Crackers>/n<Saltine></Saltine>/n<Ritz></Ritz></Crackers>")
        self.assertTrue(type(b) is Element)

    def test_element_3 (self) :
        
        b = xml_element ("<Pizza_Toppings>/n/t<Meat>/n/t/t<Pepperoni></Pepperoni>/n/t/t<Sausage></Sausage>/n/t</Meat>/n</Pizza_Toppings>")
        self.assertTrue(type(b) is Element)
        
    # ----
    # query
    # ----

    def test_query (self) :

        root = fromstring ("<xml><Taco></Taco><Burrito></Burrito></xml>")
        body, query = xml_query (root)
        self.assertTrue(type(body) is Element)
        self.assertTrue(type(query) is Element)
        self.assertTrue(body.tag == 'Taco')
        self.assertTrue(query.tag == 'Burrito')

    def test_query_2 (self) :
        
        root = fromstring ("<xml><Quidditch><Bludger></Bludger><Quaffle></Quaffle></Quidditch><Beater><Bludger></Bludger></Beater></xml>")
        body, query = xml_query (root)
        self.assertTrue(type(body) is Element)
        self.assertTrue(type(query) is Element)
        self.assertTrue(body.tag == 'Quidditch')
        self.assertTrue(query.tag == 'Beater')

    def test_query_3 (self) :
        
        root = fromstring("<xml><Languages><Spanish><Colombia></Colombia><Spain></Spain></Spanish></Languages><Languages><Russian></Russian></Languages></xml>")
        body, query = xml_query (root)
        self.assertTrue(type(body) is Element)
        self.assertTrue(type(query) is Element)
        self.assertTrue(body.tag == 'Languages')
        self.assertTrue(query.tag == 'Languages')
            

            
    #----
    #assign_location
    #----
    def test_assign_location_1(self) :
        body = fromstring('<xml><run><right><roun></roun></right></run><rich></rich></xml>')
        body = assign_location(body)
        self.assertTrue(type(body) is Element)
        self.assertTrue(body.text == '1')
            
    def test_assign_location_2(self) :
        body = fromstring('<xml><run></run><right></right></xml>')
        body = assign_location(body)
        self.assertTrue(type(body is Element))
        self.assertTrue(body.text == '1')
        
    # ----
    # eval
    # ----
    

    def test_eval (self) :
        
        body = fromstring("<Juice><Orange></Orange></Juice>")
        body = assign_location(body)
        query = fromstring("<Juice><Orange></Orange></Juice>")
        top_element = ""
        count, location = xml_eval (body, query, [0], [],0, top_element)
        self.assertTrue(count == [1])
        self.assertTrue(location == ["1"])

    def test_eval_2 (self) :

        body = fromstring("<Drinks><Juice><Orange></Orange><Grape></Grape></Juice><Soda></Soda></Drinks>")
        body = assign_location(body)
        query = fromstring("<Drinks><Juice><Orange></Orange></Juice></Drinks>")
        top_element = ""
        count, location = xml_eval (body, query, [0], [], 0, top_element)
        self.assertTrue(count == [1])
        self.assertTrue(location == ["1"])

    def test_eval_3 (self) :

        body = fromstring( "<Hogwarts><Gryffindor></Gryffindor><Ravenclaw></Ravenclaw></Hogwarts>")
        body = assign_location(body)
        query = fromstring( "<Hogwarts><Slytherin></Slytherin></Hogwarts>")
        top_element = ""
        count, location = xml_eval (body, query, [0], [], 0, top_element)
        self.assertTrue(count == [0])
        self.assertTrue(location == [])
        
    def test_eval_4 (self) :

        body = fromstring ("<Fruit><Berries><Strawberries></Strawberries></Berries><Berries><Strawberries></Strawberries></Berries></Fruit>")
        body = assign_location(body)
        query = fromstring ("<Berries><Strawberries></Strawberries></Berries>")
        top_element = ""
        count, location = xml_eval (body, query, [0], [], 0, top_element)
        self.assertTrue(count == [2])
        self.assertTrue(location == ["2", "4"])


    def test_eval_5 (self) :

        body = fromstring ("<red><green><blue></blue><yellow></yellow></green></red>")
        body = assign_location(body)
        query = fromstring ("<red><blue></blue></red>")
        top_element = ""
        count, location = xml_eval (body, query, [0], [], 0, top_element)
        self.assertTrue(count == [0])
        self.assertTrue(location == ([]))
      
    # ----
    # solve
    # ----

    def test_solve (self) :

        r = io.StringIO("<Writers><Eliot></Eliot></Writers><Writers><Eliot></Eliot></Writers>")
        w = io.StringIO()
        xml_solve (r,w)
        self.assertTrue(w.getvalue() == "1\n1\n\n")

    def test_solve_2 (self) :
        
        r = io.StringIO("<Writers><Pratchett></Pratchett><Gaiman></Gaiman><Martin></Martin></Writers><Writers><Gaiman></Gaiman></Writers>")
        w = io.StringIO()
        xml_solve (r,w)
        self.assertTrue(w.getvalue() == "1\n1\n\n")

    def test_solve_3 (self) :
        r = io.StringIO("<Writers><Fantasy><Pratchett></Pratchett><Gaiman></Gaiman></Fantasy><Fantasy><Gaiman></Gaiman><Martin></Martin></Fantasy></Writers><Writers><Fantasy><Gaiman></Gaiman></Fantasy></Writers>")
        w= io.StringIO()
        xml_solve(r,w)
        self.assertTrue(w.getvalue() == "2\n1\n1\n\n")
        


    # ----
    # print
    # ----

    def test_print (self) :
        
        w = io.StringIO()
        xml_print(w,[1],["2"])
        self.assertTrue(w.getvalue() == "1\n2\n\n")

    def test_print_2 (self) :
        
        w = io.StringIO()
        xml_print(w, [3], ["2","3","4"])
        self.assertTrue(w.getvalue() == "3\n2\n3\n4\n\n")
        
    def test_print_3 (self) :
        
        w = io.StringIO()
        xml_print(w,[0], [])
        self.assertTrue(w.getvalue() == "0\n\n")
      
# ----
# main
# ----

print("TestXML.py")
unittest.main()
print("Done.")

      
