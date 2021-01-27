import wx;
from sqlitedb import *;
from userdb import *;

data = ['aaa','bbb','ccc'];

app = wx.App();
frame = wx.Frame(None, title='Shop Management');
panel1 = wx.Panel(frame);
panel2 = wx.Panel(frame);
panel1.SetBackgroundColour(colour='blue');
panel2.SetBackgroundColour(colour='green');

textId = wx.TextCtrl(panel1);
textPwd = wx.TextCtrl(panel1);
textName = wx.TextCtrl(panel1);
bt = wx.Button(panel1, label='ADD');

userList = wx.ListBox(panel2,choices=data);
userList.SetBackgroundColour(colour='white')
userList.SetSize(wx.Size(180,200))
#List Event.....
def itemselect(event):
    dataCnt = userList.GetSelection();
    wx.MessageBox(data[dataCnt], 'User Information', wx.OK);

userList.Bind(wx.EVT_LISTBOX, itemselect)

# 버튼 이벤트
def onClick(event):
    id = textId.GetValue();
    pwd = textPwd.GetValue();
    name = textName.GetValue();
    wx.MessageBox(id, 'Alert', wx.OK)
    print('Inserted')
    # 이곳에서 디비에 인서트 작업 수행
    data.append(id+' '+name);
    userList.Append(id+' '+name);
    textId.SetValue('');
    textPwd.SetValue('');
    textName.SetValue('');
bt.Bind(wx.EVT_BUTTON, onClick);

box1 = wx.BoxSizer(wx.VERTICAL);
box1.Add(textId);
box1.Add(textPwd);
box1.Add(textName);
box1.Add(bt);
panel1.SetSizer(box1);

# Grid................................
grid = wx.GridSizer(1,2,10,10);
grid.Add(panel1,0,wx.EXPAND);
grid.Add(panel2,0,wx.EXPAND);

frame.SetSizer(grid);
frame.Show(True);
app.MainLoop();
