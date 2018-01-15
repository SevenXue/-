#-*- coding:utf-8 -*-

import wx
import wx.aui, wx.grid
import sys
import pymysql
from Acuact import *
from information import *
import tmpframe

reload(sys)
sys.setdefaultencoding('utf8')


class UpdateFrame(wx.Frame):
    # 更改信息，先显示信息，后更改
    def __init__(self, parent, title, select_id):
        self.mainframe = parent

        wx.Frame.__init__(self, parent, title=title, size=(1000, 600))

        self.panel = wx.Panel(self, pos=(0, 0), size=(1000, 800))
        self.panel.SetBackgroundColour("#FFFFFF")

        # 12个编辑框
        col1 = wx.StaticText(self.panel, -1, 'id', pos=(5, 8), size=(50, 25))
        col2 = wx.TextCtrl(self.panel, -1, pos=(100, 8), size=(300, 30), style=wx.TE_READONLY)
        col2.SetBackgroundColour("#BBFFFF")
        self.id = col2

        col3 = wx.StaticText(self.panel, -1, u"穴位", pos=(450, 8), size=(50, 25))
        col4 = wx.TextCtrl(self.panel, -1, pos=(500, 8), size=(300, 30))
        self.chinese = col4

        col5 = wx.StaticText(self.panel, -1, u"脉络", pos=(5, 100), size=(50, 25))
        col6 = wx.TextCtrl(self.panel, -1, pos=(100, 100), size=(300, 30))
        self.vein = col6

        col7 = wx.StaticText(self.panel, -1, u"链接", pos=(450, 100), size=(50, 25))
        col8 = wx.TextCtrl(self.panel, -1, pos=(500, 100), size=(300, 30), style=wx.TE_READONLY)
        col8.SetBackgroundColour("#BBFFFF")
        self.url = col8

        col13 = wx.StaticText(self.panel, -1, u"解剖", pos=(5, 200), size=(50, 25))
        col14 = wx.TextCtrl(self.panel, -1, pos=(100, 200), size=(300, 100), style=wx.TE_MULTILINE)
        self.dissection = col14

        col15 = wx.StaticText(self.panel, -1, u"主治疾病", pos=(450, 200), size=(50, 25))
        col16 = wx.TextCtrl(self.panel, -1, pos=(500, 200), size=(300, 100), style=wx.TE_MULTILINE)
        self.disease = col16

        col17 = wx.StaticText(self.panel, -1, u"配伍穴位", pos=(5, 350), size=(50, 25))
        col18 = wx.TextCtrl(self.panel, -1, u"不可为空", pos=(100, 350), size=(300, 100), style=wx.TE_MULTILINE)
        self.compatibility = col18

        col19 = wx.StaticText(self.panel, -1, u"定位", pos=(450, 350), size=(50, 25))
        col20 = wx.TextCtrl(self.panel, -1, pos=(500, 350), size=(300, 100), style=wx.TE_MULTILINE)
        self.location = col20

        save_info = wx.Button(self.panel, label=u"保存", pos=(5, 500))
        self.Bind(wx.EVT_BUTTON, self.Update, save_info)

        self.select_id = select_id
        self.infoiid = self.mainframe.list.GetItem(select_id, 0).Text

        # 连接数据库
        self.dbInfo = Acuact()
        self.showAllText()

    def showAllText(self):
        data = self.dbInfo.getInfoById(self.infoiid)


        self.id.SetValue(str(data[0]))
        self.chinese.SetValue(data[1])
        self.vein.SetValue(data[2])
        self.dissection.SetValue(data[3])
        self.disease.SetValue(data[4])
        self.compatibility.SetValue(data[5])
        self.location.SetValue(data[6])
        self.url.SetValue(data[7])

    def Update(self, evt):
        #保存修改后的值
        id = self.id.GetValue()
        chinese = self.chinese.GetValue()
        vein = self.vein.GetValue()
        dissection = self.dissection.GetValue()
        disease = self.disease.GetValue()
        compatibility = self.compatibility.GetValue()
        location = self.location.GetValue()
        url = self.url.GetValue()

        if id == '' or compatibility == '':
            warn = wx.MessageDialog(self, message=u"有非空字段为空！", caption=u"错误警告", style=wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()  # 提示错误
            warn.Destroy()
            return

        else:
            print u'开始写入'

            info = Acupoint(id, chinese, vein, dissection, disease, compatibility, location, url)
            self.dbInfo.saveUpdate(id, info)
            #self.mainframe.addToList()
            self.mainframe.list.SetStringItem(self.select_id, 1, chinese)
            self.mainframe.list.SetStringItem(self.select_id, 2, vein)
            self.mainframe.list.SetStringItem(self.select_id, 3, url)
            self.mainframe.list.SetStringItem(self.select_id, 4, compatibility)

        self.Destroy()

class ShowFrame(wx.Frame):
    #显示具体信息
    def __init__(self, parent, title, select_id):

        self.mainframe = parent

        wx.Frame.__init__(self, parent, title=title, size=(1000, 500))

        self.panel= wx.Panel(self, pos=(0,0), size=(1000, 500))
        self.panel.SetBackgroundColour("#FFFFFF")

        #12个编辑框
        col1 = wx.StaticText(self.panel, -1, 'id', pos=(5, 8), size=(50,25))
        col2 = wx.TextCtrl(self.panel, -1, pos=(100, 8), size=(300, 30), style=wx.TE_READONLY)
        col2.SetBackgroundColour("#FFFFFF")
        self.id = col2

        col3 = wx.StaticText(self.panel, -1, u"穴位", pos=(450, 8), size=(50,25))
        col4 = wx.TextCtrl(self.panel, -1, pos=(500, 8), size=(300, 30), style=wx.TE_READONLY)
        col4.SetBackgroundColour("#FFFFFF")
        self.chinese = col4

        col5 = wx.StaticText(self.panel, -1, u"脉络", pos=(5, 100), size=(50,25))
        col6 = wx.TextCtrl(self.panel, -1,  pos=(100, 100), size=(300, 30), style=wx.TE_READONLY)
        col6.SetBackgroundColour("#FFFFFF")
        self.vein = col6

        col7 = wx.StaticText(self.panel, -1, u"链接", pos=(450, 100), size=(50,25), style=wx.TE_READONLY)
        col8 = wx.TextCtrl(self.panel, -1, pos=(500, 100), size=(300, 30))
        col8.SetBackgroundColour("#FFFFFF")
        self.url = col8

        col13 = wx.StaticText(self.panel, -1, u"解剖", pos=(5, 200), size=(50,25))
        col14 = wx.TextCtrl(self.panel, -1, pos=(100, 200), size=(300, 100), style = wx.TE_MULTILINE | wx.TE_READONLY)
        self.dissection = col14

        col15 = wx.StaticText(self.panel, -1, u"主治疾病", pos=(450, 200), size=(50,25))
        col16 = wx.TextCtrl(self.panel, -1, pos=(500, 200), size=(300, 100), style = wx.TE_MULTILINE | wx.TE_READONLY)
        self.disease = col16

        col17 = wx.StaticText(self.panel, -1, u"配伍穴位", pos=(5, 350), size=(50,25))
        col18 = wx.TextCtrl(self.panel, -1, u"不可为空", pos=(100, 350), size=(300, 100), style = wx.TE_MULTILINE | wx.TE_READONLY)
        self.compatiblity = col18

        col19 = wx.StaticText(self.panel, -1, u"定位", pos=(450, 350), size=(50,25))
        col20 = wx.TextCtrl(self.panel, -1, pos=(500, 350), size=(300, 100), style = wx.TE_MULTILINE | wx.TE_READONLY)
        self.location = col20

        self.select_id = select_id
        self.infoiid = self.mainframe.list.GetItem(select_id, 0).Text

        #连接数据库
        self.dbInfo = Acuact()
        self.showAllText()

    def showAllText(self):
        data = self.dbInfo.getInfoById(self.infoiid)

        self.id.SetValue(str(data[0]))
        self.chinese.SetValue(data[1])
        self.vein.SetValue(data[2])
        self.dissection.SetValue(data[3])
        self.disease.SetValue(data[4])
        self.compatiblity.SetValue(data[5])
        self.location.SetValue(data[6])
        self.url.SetValue(data[7])

class MyFrame(wx.Frame):
    """
        create the Frame for NMR
        mneubar,statusbar,mult-windows
    """

    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition, wx.Size(800,400))

        # 生成一个列表
        self.list = wx.ListCtrl(self, -1, size=(800, 300),
                                style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)

        self.list.InsertColumn(0, u"编号")
        self.list.InsertColumn(1, u"穴位")
        self.list.InsertColumn(2, u"脉络")
        self.list.InsertColumn(3, u"链接")
        self.list.InsertColumn(4, u'常用配伍')

        # self.list.InsertColumn(0, u"编号")
        # self.list.InsertColumn(1, u"题目")
        # self.list.InsertColumn(2, u"配伍穴位")
        # self.list.InsertColumn(3, u"录入者")
        # 设置各列的宽度
        self.list.SetColumnWidth(0, 50)  # 设置每一列的宽度
        self.list.SetColumnWidth(1, 50)
        self.list.SetColumnWidth(2, 100)
        self.list.SetColumnWidth(3, 350)
        self.list.SetColumnWidth(4, 350)

        # 添加一组按钮，实现增删改查,用一个panel来管理该组按钮的布局
        self.panel = wx.Panel(self, pos=(450, 300), size=(800, 100))

        # 定义一组按钮
        # base information of database
        table_list = ['Acupoint', 'Information']

        self.qName = wx.StaticText(self.panel, -1, "DataBase:", pos=(10, 15), size=(60, 30))
        self.qName0 = wx.TextCtrl(self.panel, -1, value='Acupuncture',pos=(80, 15), style=wx.TE_READONLY | wx.TE_CENTER, size=(80, 30))
        self.qName1 = wx.StaticText(self.panel, -1, "Table:", pos=(170, 15), size=(50, 30))
        self.qName2 = wx.Choice(self.panel, -1, choices=table_list, pos=(220, 15), size=(100, 30))
        show_button = wx.Button(self.panel, label=u"显示", pos=(330, 15), size=(60, 30))
        self.Bind(wx.EVT_BUTTON, self.show_data, show_button)

        #操作按钮
        add_button = wx.Button(self.panel, label=u"添加", pos=(10, 50), size=(60, 30))  # , size = (75, 30)
        del_button = wx.Button(self.panel, label=u"删除", pos=(110, 50), size=(60, 30))  # , size = (75, 30)
        update_button = wx.Button(self.panel, label=u"修改", pos=(210, 50), size=(60, 30))  # , size = (75, 30)
        query_button = wx.Button(self.panel, label=u"查看", pos=(310, 50), size=(60, 30))  # , size = (75, 30)

        # 为按钮绑定相应事件函数
        self.Bind(wx.EVT_BUTTON, self.add_data, add_button)
        self.Bind(wx.EVT_BUTTON, self.delete, del_button)
        self.Bind(wx.EVT_BUTTON, self.modify, update_button)
        self.Bind(wx.EVT_BUTTON, self.select_data, query_button)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.list, 3, wx.EXPAND)
        self.sizer.Add(self.panel, 1, wx.EXPAND | wx.ALL)

        self.SetSizer(self.sizer)
        self.Fit()

        #添加数据库操作对象
        self.dbhelper = Acuact()
        datas = self.dbhelper.getAll()

        for j in range(len(datas)):
            data = datas[j]
            index = self.list.InsertStringItem(sys.maxint,str(data[0]))
            #self.list.SetStringItem(index, 1, str(data[0]))
            self.list.SetStringItem(index, 1, data[1])
            self.list.SetStringItem(index, 2, data[2])
            self.list.SetStringItem(index, 3, data[3])
            self.list.SetStringItem(index, 4, data[4])

    def add_data(self, evt):
        return None
        #add_f = AddFrame(self, u'添加信息')
        #add_f.Show(True)

    def delete(self, event):
        return None

    def modify(self, event):
        selectId = self.list.GetFirstSelected()
        if selectId == -1:
            warn = wx.MessageDialog(self, message=u"未选中任何条目！", caption=u"错误警告", style=wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()  # 提示错误
            warn.Destroy()
            return
        else:
            show_f = UpdateFrame(self, u"修改窗口", selectId)
            show_f.Show(True)

    def select_data(self, event):
        selectId = self.list.GetFirstSelected()
        if selectId == -1:
            warn = wx.MessageDialog(self, message=u"未选中任何条目！", caption=u"错误警告", style=wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()  # 提示错误
            warn.Destroy()
            return
        else:
            show_f = ShowFrame(self, u"查看窗口", selectId)
            show_f.Show(True)

    def show_data(self, event):
        table = self.qName2.GetString(self.qName2.GetSelection())
        if table =='Information':
            tmp_app=tmpframe.MyApp(0)
            tmp_app.MainLoop()

class MyApp(wx.App):
    def OnPreInit(self):
        frame = MyFrame(None, -1, 'NMR Database')
        frame.Show(True)


if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()