import gvar

def header_name(message):
  Log.Enabled=True
  attr = gray_bold()
  Log.Checkpoint(message,"",pmHigher,attr)
  Log.Enabled=False

def test_name(message):
  Log.Enabled=True
  attr = blue_bold()
  Log.Checkpoint(message,"",pmHigher,attr)
  Log.Enabled=False
  
def test_data(message):
  Log.Enabled=True
  attr = blue()
  Log.Checkpoint(message,"",pmHigher,attr)
  Log.Enabled=False
  
def validation(message):
  Log.Enabled=True
  attr = green_bold()
  wnd = Sys.Desktop.ActiveWindow()
  Log.Checkpoint(message,"",pmHigher,attr,wnd)
  Log.Enabled=False
      
def checkpt_with_picture(message,priority,object):
  Log.Enabled=True
  attr = green()
  Log.Checkpoint(message,"", priority, attr, object)
  Log.Enabled=False
  
def checkpt_with_no_picture(message):
  Log.Enabled=True
  attr = green()
  Log.Checkpoint(message,"", pmHigher, attr)
  Log.Enabled=False

def msg_with_picture(message):
  Log.Enabled=True
  wnd = Sys.Desktop.ActiveWindow()
  Log.Message(message,"", pmHigher, "", wnd)
  Log.Enabled=False

def msg_with_no_picture(message):
  Log.Enabled=True
  Log.Message(message,"", pmHigher, "")
  Log.Enabled=False
  
def error_with_picture(message):
  Log.Enabled=True 
  attr = red_bold()
  Log.Error(message,"", pmHigher, attr)
  wnd = Sys.Desktop.ActiveWindow()
  Log.Picture(wnd, "Error Screenshot", wnd.FullName)                  
  Log.Enabled=False  

def error_with_no_picture(message,additionalInformation=""):
  Log.Enabled=True
  attr = red_bold()
  Log.Error(message, additionalInformation, pmHigher, attr)
  Log.Enabled=False

def CorrectRGBComponent(component):
  component = aqConvert.VarToInt(component)
  if component < 0:
    component = 0
  else:
    if component > 255:
      component = 255
  return component

def RGB(r, g, b):
  r = CorrectRGBComponent(r)
  g = CorrectRGBComponent(g)
  b = CorrectRGBComponent(b)
  return r | (g << 8) | (b << 16)

def gray_bold():
  attr = Log.CreateNewAttributes()
  attr.Bold = True;
  attr.FontColor = RGB(255, 255, 255)
  attr.BackColor = RGB(128, 128, 128)
  return attr

def blue_bold():
  attr = Log.CreateNewAttributes()
  attr.Bold = True;
  attr.FontColor = RGB(0, 0, 128)
  attr.BackColor = RGB(166, 202, 240)
  return attr
  
def blue():
  attr = Log.CreateNewAttributes()
  attr.FontColor = RGB(0, 0, 128)
  return attr  

def green():
  attr = Log.CreateNewAttributes()
  attr.FontColor = RGB(0, 128, 0)
  return attr 
  
def green_bold():
  attr = Log.CreateNewAttributes()
  attr.Bold = True;
  attr.FontColor = RGB(0, 128, 0)
  return attr
 
def red_bold():
  attr = Log.CreateNewAttributes()
  attr.Bold = True;
  attr.FontColor = RGB(255, 0, 0)
  return attr
  
def yellow_bold():
  attr = Log.CreateNewAttributes()
  attr.Bold = True;
  attr.FontColor = RGB(255, 255, 0)
  attr.BackColor = RGB(255, 251, 240)
  return attr

def test():
  var1 = 'TEST'
  var1 = ''.join([ data for data in var1 if data.isdigit()])
  Log.Message(var1)
