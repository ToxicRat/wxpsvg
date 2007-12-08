import unittest
import wx
from pyparsing import ParseException

import svg.css.values as values

class FailTest(Exception):
    pass

class ParseTester(object):
    def testValidValues(self):
        #~ self.parser.debug = True
        try:
            for string, expected in self.valid:
                self.assertEqual(expected, self.parser.parseString(string)[0])
        except ParseException:
            raise FailTest("expected %r to be valid" % string)

class TestInteger(unittest.TestCase, ParseTester):
    parser = values.integer
    valid = [(x, int(x)) for x in ["01", "1"]]
    
            
class TestNumber(unittest.TestCase, ParseTester):
    parser = values.number
    valid = [(x, float(x)) for x in ["1.1", "2.3", ".3535"]]
    valid += TestInteger.valid
        
class TestSignedNumber(unittest.TestCase, ParseTester):
    parser = values.signedNumber
    valid = [(x, float(x)) for x in ["+1.1", "-2.3"]]
    valid += TestNumber.valid
    
class TestLengthUnit(unittest.TestCase, ParseTester):
    parser = values.lengthUnit
    valid = [(x,x.lower()) for x in ["em", "ex", "px", "PX", "EX", "EM"]]
        
class TestLength(unittest.TestCase):
    parser = values.length
    valid = [
        ("1.2em", (1.2, "em")),
        ("0", (0, None)),
        ("10045px", (10045, "px")),
        ("300%", (300, "%")),
    ]
    
    def testValidValues(self):
        for string, expected in self.valid:
            #~ print string, expected
            got = self.parser.parseString(string)
            self.assertEqual(expected, tuple(got))
            
    def testIntegersIfPossible(self):
        results = self.parser.parseString("100px")[0]
        self.assertTrue(isinstance(results, int))
        
    def testNoSpaceInPercent(self):
        """ SVG spec requires that the percent "immediately"
        follow the number"""
        self.assertRaises(
            ParseException,
            self.parser.parseString,
            "300 %"
        )   
        
    