# Missing Features #
  * Elliptical arcs (needs patches to wx)
  * Container negotiation to determine canvas size
  * Implement the viewer as a control, not a wxPanel
  * Scrolling in the viewer, with correct viewBox and canvas size support
  * Image support
  * gradient brushes (no tests for this in the w3c suite, need to find one)
  * 

&lt;use&gt;

 element
  * animation
  * correct, standards compliant CSS parsing and cascading
  * Related: correct cascading of attributes
  * text support (needs patches to wx)
  * correct rounded rects (needs wx patches)
  * SVG DOM
  * the control should have some convenience methods to make hittesting convenient
  * Better performance (rendering is about as fast as it can be, need to optmize parsing)
  * Need a mechanism for retrieving URLs.
  * Loading needs to become async in some way, especially for the retrieval of urls.

# Requirements #
  * Python 2.5 (2.4 may work, untested)
  * wxWidgets 2.8.4 (anythign with wxGraphicsContext should work, but newer is better)
  * [pyparsing](http://pyparsing.wikispaces.com/) 1.4.6 (older will **not** work)