import tkinter as tkin

class MenuTest:
  #Basic init that just bypasses to the first top level
  def __init__(self):
    self.main = tkin.Tk()
    self.main.withdraw()
    self.starter()
    tkin.mainloop()
  
  def starter(self):
    self.start = tkin.Toplevel(self.main)
    self.currentW = self.start.destroy
    self.start.title('The window...')
    self.infoS = tkin.Label(self.start,text='Start',)
    self.infoS.pack(side='top')
    self.menuThing(self.start)
  
  def tester(self):
    self.next = tkin.Toplevel(self.main)
    self.currentW = self.next.destroy
    self.next.title('The other...')
    self.infoS = tkin.Label(self.next,text='Other',)
    self.infoS.pack(side='top')
    self.menuThing(self.next)

  def menuThing(self, master):
    self.frame = tkin.Frame(master)
    self.startW = tkin.Button(master, text='Start',command=self.toStart)
    self.otherW = tkin.Button(master, text='Other',command=self.toOther)
    self.startW.pack(side='left')
    self.otherW.pack(side='left')
    self.frame.pack(side='top')
  
  def toStart(self):
    self.currentW()
    self.starter()
  
  def toOther(self):
    self.currentW()
    self.tester()

test = MenuTest()