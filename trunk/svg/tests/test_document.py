import unittest
import svg.document as document
import wx
import xml.etree.cElementTree as etree
from cStringIO import StringIO

minimalSVG = etree.parse(StringIO(r"""<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1"></svg>"""))

app = None

class TestBrushFromColourValue(unittest.TestCase):
    
    def setUp(self):
        #need a wxApp for this
        global app
        if not app:
            app = wx.App(False)
        self.document = document.SVGDocument(minimalSVG.getroot())
        self.stateStack = [{}]

    def testNone(self):
        self.document.state["fill"] = 'none'
        self.assertEqual(
            self.document.getBrushFromState(),
            wx.NullBrush
        )

    def testCurrentColour(self):
        self.document.state["fill"] = 'currentColor'
        self.document.state["color"] = "rgb(100,100,100)"
        self.assertEqual(
            self.document.getBrushFromState().GetColour().Get(),
            (100,100,100)
        )

    def testCurrentColourNull(self):
        self.document.state["fill"] = 'currentColor'
        self.assertEqual(
            self.document.getBrushFromState(),
            wx.NullBrush
        )

    def testOpacity(self):
        self.document.state["fill"] = 'rgb(255,100,10)'
        self.document.state["fill-opacity"] = 0.5
        self.assertEqual(
            self.document.getBrushFromState().GetColour().Alpha(),
            127
        )

    def testOpacityClampHigh(self):
        self.document.state["fill"] = 'rgb(255,100,10)'
        self.document.state["fill-opacity"] = 5
        self.assertEqual(
            self.document.getBrushFromState().GetColour().Alpha(),
            255
        )

    def testOpacityClampLow(self):
        self.document.state["fill"] = 'rgb(255,100,10)'
        self.document.state["fill-opacity"] = -100
        self.assertEqual(
            self.document.getBrushFromState().GetColour().Alpha(),
            0
        )
    def testURLFallback(self):
        self.document.state["fill"] = "url(http://google.com) red"
        self.assertEqual(
            self.document.getBrushFromState().GetColour().Get(),
            (255,0,0)
        )
