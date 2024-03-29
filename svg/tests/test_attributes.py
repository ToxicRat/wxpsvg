import unittest
import svg.attributes as a

from css.test_color import TestValueParser


class TestURLParser(unittest.TestCase):
    parser = a.url
    def testURL(self):
        self.assertEqual(
            self.parser.parseString("url(#someGradient)").asList(),
            ["URL", [('', '', '', '', "someGradient"), ()]]
        )
    def testURLWithFallback(self):
        self.assertEqual(
            self.parser.parseString("url(someGradient) red").asList(),
            ["URL", [('', '', "someGradient", '', ''), ['RGB', (255,0,0)]]]
        )
    def testEmptyURLWithFallback(self):
        self.assertEqual(
            self.parser.parseString("url() red").asList(),
            ["URL", [('', '', '', '', ''), ['RGB', (255,0,0)]]]
        )
    def testEmptyURL(self):
        self.assertEqual(
            self.parser.parseString("url()").asList(),
            ["URL", [('', '', '', '', ''), ()]]
        )
    def testxPointerURL(self):
        self.assertEqual(
            self.parser.parseString("url(#xpointer(idsomeGradient))").asList(),
            ["URL", [('', '', '', '', "xpointer(idsomeGradient)"), ()]]
        )
        
class TestPaintValueURL(TestURLParser):
    parser = a.paintValue
        
class TestPaintValue(TestValueParser):
    parser = a.paintValue
    def testNone(self):
        self.assertEqual(
            self.parser.parseString("none").asList(),
            ["NONE", ()]
        )
        
    def testCurrentColor(self):
        self.assertEqual(
            self.parser.parseString("currentColor").asList(),
            ["CURRENTCOLOR", ()]
        )