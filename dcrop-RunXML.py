"""
To run the program
    % python RunXML.py < RunXML.in > RunXML.out
    % chmod ugo+x RunXML.py
    % RunXML.py < RunXML.in > RunXML.out

To document the program
    % pydoc -w XML
"""

# -------
# imports
# -------

import sys

import XML
from XML import xml_assign_id, xml_potentials, xml_check, xml_matches, xml_print, xml_search

# ----
# main
# ----

xml_search(sys.stdin, sys.stdout)
