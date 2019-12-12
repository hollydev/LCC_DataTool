import wx
class MyFrame(wx.Frame):

    def OnQuit(self, e):
        self.Close()

    def __init__(self, parent, title):
          wx.Frame.__init__(self, parent, title=title, size=(600,600))
          panel = wx.Panel(self)
          self.control = wx.TextCtrl(panel, style=wx.TE_MULTILINE, pos = (300,5), size = (250, 500))
          menubar = wx.MenuBar()
          fileMenu = wx.Menu()
          fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')
          self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)
          menubar.Append(fileMenu, '&File')
          self.SetMenuBar(menubar)
          self.Show(True)

app = wx.App(False)
frame = MyFrame(None, 'LCC_DataTool')
app.MainLoop()