import wx
import wx.py.shell
import wx.aui
import wx.grid
        
class PathGrid(wx.grid.Grid):
    def __init__(self, parent, pathOps):
        super(PathGrid, self).__init__(parent)
        self.CreateGrid(100,10)
        firstColAttr = wx.grid.GridCellAttr()
        choices = sorted(pathOps.keys())
        firstColAttr.SetEditor(wx.grid.GridCellChoiceEditor(choices))
        self.SetColMinimalWidth(0,140)
        self.SetColAttr(0, firstColAttr)
        
class PathPanel(wx.Panel):
    ctx = None
    path = None
    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        if not (self.ctx and self.path):
            return
        self.ctx.DrawPath(self.path)
        
        

class DrawFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.pathOps = dict((k,v) for (k,v) in wx.GraphicsPath.__dict__.iteritems() if k.startswith("Add"))
        self.pathOps["CloseSubpath"] = wx.GraphicsPath.CloseSubpath
        self.pathOps["MoveToPoint"] = wx.GraphicsPath.MoveToPoint
        self.pathOps[""] = None
        
        self._mgr = wx.aui.AuiManager()
        self._mgr.SetManagedWindow(self)
        
        self.panel = PathPanel(self)
        
        self.locals = {
            "wx":wx,
            "frame":self,
            "panel":self.panel,
            "context":None
        }
        
        self.nb = wx.aui.AuiNotebook(self)
        
        self.shell = wx.py.shell.Shell(self.nb, locals = self.locals)
        
        self.grid = PathGrid(self.nb, self.pathOps)
        
        
        self.nb.AddPage(self.shell, "Shell")
        self.nb.AddPage(self.grid, "Path", True)
        
        
        self._mgr.AddPane(self.nb, 
            wx.aui.AuiPaneInfo().Bottom().CaptionVisible(False).BestSize((-1,300))
        )
        self._mgr.AddPane(self.panel, wx.aui.AuiPaneInfo().CenterPane())
        
        self._mgr.Update()
        
        wx.CallAfter(self.CreateContext)
        #wx.CallAfter(self.shell.SetFocus)
        
        #~ self.panel.Bind(wx.EVT_SIZE, self.OnSize, source=self.panel)
        
        self.panel.Bind(wx.EVT_PAINT, self.panel.OnPaint, source=self.panel)
        
        #~ self.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.OnPathChange)
        
    def CreateContext(self):
        ctx = wx.GraphicsContext_Create(self.panel)
        self.locals["context"] = ctx
        ctx.SetPen(wx.BLACK_PEN)
        ctx.SetBrush(wx.RED_BRUSH)
        return ctx
        
    def OnPathChange(self, evt):
        self.panel.ctx = self.CreateContext()
        self.panel.path = self.panel.ctx.CreatePath()
        self.FillPath(self.panel.path)
        self.panel.Refresh()
    
    def FillPath(self, path):
        for row in xrange(100):
            print row,
            operation = self.grid.GetCellValue(row, 0)
            if not operation:
                return
            print operation,
            args = []
            for col in xrange(1,20):
                v = self.grid.GetCellValue(row, col)
                if not v:
                    break
                args.append(float(v))
            self.pathOps[operation](path, *args)
            print args
            
                
    def OnSize(self, evt):
        if self.panel.ctx:
            self.CreateContext()

            
        
            
if __name__ == '__main__':
    app = wx.App(False)
    frame = DrawFrame(None)
    frame.Show()
    app.MainLoop()