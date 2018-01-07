#-*- coding:utf-8 -*-

import wx
import wx.aui, wx.grid
import sys
import pymysql

reload(sys)
sys.setdefaultencoding('utf8')

class MetaPanel(wx.Panel):

    def __init__(self, parent):

        wx.Panel.__init__(self, parent, -1)

        self.parent = parent

        #base information of database
        table_list = ['Acupoint', 'Information']

        self.qName = wx.StaticText(self, -1, "DataBase:", size=(60,30))
        self.qName0 = wx.TextCtrl(self, -1, value='Acupoint',style=wx.TE_READONLY|wx.TE_CENTER, size=(100,-1))
        self.qName1 = wx.StaticText(self, -1, "Table:")
        self.qName2 = wx.Choice(self, -1, choices=table_list, size=(100,-1))

        #column
        self.col1 = wx.StaticText(self, -1, u"文献统一编号")
        self.col2 = wx.TextCtrl(self, -1, u"不可为空", size=(220, -1))

        self.col3 = wx.StaticText(self, -1, u"文献类别")
        self.col4 = wx.TextCtrl(self, -1, size=(220, -1))

        self.col5 = wx.StaticText(self, -1, u"文献题目")
        self.col6 = wx.TextCtrl(self, -1, size=(220, -1))

        self.col7 = wx.StaticText(self, -1, u"发表日期")
        self.col8 = wx.TextCtrl(self, -1, size=(220, -1))

        self.col9 = wx.StaticText(self, -1, u"所有作者")
        self.col10 = wx.TextCtrl(self, -1, size=(220, -1))

        self.col11 = wx.StaticText(self, -1, u"通讯作者")
        self.col12 = wx.TextCtrl(self, -1, size=(220, -1))

        self.col13 = wx.StaticText(self, -1, u"疾病")
        self.col14 = wx.TextCtrl(self, -1, size=(220, -1))

        self.col15 = wx.StaticText(self, -1, u"症状")
        self.col16 = wx.TextCtrl(self, -1, size=(220, -1))

        self.col17 = wx.StaticText(self, -1, u"配伍穴位")
        self.col18 = wx.TextCtrl(self, -1, u"不可为空", size=(220, -1))

        self.col19 = wx.StaticText(self, -1, u"文献存储位置")
        self.col20 = wx.TextCtrl(self, -1, size=(220, -1))

        self.col21 = wx.StaticText(self, -1, u"注释")
        self.col22 = wx.TextCtrl(self, -1, size=(220, -1))

        self.col23 = wx.StaticText(self, -1, u"录入者")
        self.col24 = wx.TextCtrl(self, -1, u"不可为空", size=(220, -1))

        # functions of database
        self.add_button = wx.Button(self, 100, "Add", size=(220,-1))
        self.Bind(wx.EVT_BUTTON, self.add_data, self.add_button)
        self.add_button.SetDefault()

        self.delete_button = wx.Button(self, 110, "Dalete", size=(220, -1))
        self.Bind(wx.EVT_BUTTON, self.delete, self.delete_button)
        self.delete_button.SetDefault()

        self.modify_button = wx.Button(self, 120, "Modify", size=(220, -1))
        self.Bind(wx.EVT_BUTTON, self.modify, self.modify_button)
        self.modify_button.SetDefault()

        self.select_button = wx.Button(self, 130, "Select", size=(220, -1))
        self.Bind(wx.EVT_BUTTON, self.select, self.select_button)
        self.select_button.SetDefault()

        # layout of the panel
        para_grid = wx.GridSizer(1, 4)
        para_grid.AddMany([
            self.qName, self.qName0,
            self.qName1, self.qName2
        ])

        column_grid = wx.GridSizer(12, 2)
        column_grid.AddMany([
            self.col1, self.col2, self.col3, self.col4,
            self.col5, self.col6, self.col7, self.col8,
            self.col9, self.col10, self.col11, self.col12,
            self.col13, self.col14, self.col15, self.col16,
            self.col17, self.col18, self.col19, self.col20,
            self.col21, self.col22, self.col23, self.col24
        ])

        function_gard = wx.GridSizer(4, 1)
        function_gard.AddMany([self.add_button, self.delete_button, self.modify_button, self.select_button])

        para_box = wx.StaticBoxSizer(wx.StaticBox(self, -1, "DataBase"))
        para_box.Add(para_grid)

        column_box = wx.StaticBoxSizer(wx.StaticBox(self, -1, "Columns"))
        column_box.Add(column_grid)

        tool_box = wx.StaticBoxSizer(wx.StaticBox(self, -1, "Function"))
        tool_box.Add(function_gard)

        # create the whole panel of left tree
        mainbox = wx.BoxSizer(wx.VERTICAL)
        mainbox.Add(para_box)
        mainbox.Add(column_box)
        mainbox.Add(tool_box)
        self.SetSizer(mainbox)


    def add_data(self, event):
        return None

    def delete(self, event):
        return None

    def modify(self, event):
        return None

    def select(self, event):
        return None

class column_panel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent, -1)

        self.parent = parent



        self.q3_1 = wx.StaticText(self, -1, "Integral width")
        self.q3_2 = wx.TextCtrl(self, -1, "0.002")

class MyFrame(wx.Frame):
    """
        create the Frame for NMR
        mneubar,statusbar,mult-windows
    """

    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition, wx.Size(800,400))

        self.params = MetaPanel(self)

        # 生成一个列表
        self.list = wx.ListCtrl(self, -1, size=(400, 300),
                                style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)  # | wx.LC_SINGLE_SEL
        # 列表有散列，分别是书本ID,书名，添加日期
        self.list.InsertColumn(0, u"编号")
        self.list.InsertColumn(1, u"类别")
        self.list.InsertColumn(2, u"题目")
        self.list.InsertColumn(4, u"发表日期")
        self.list.InsertColumn(5, u"所有作者")
        self.list.InsertColumn(6, u"通讯作者")
        self.list.InsertColumn(7, u"疾病")
        self.list.InsertColumn(8, u"症状")
        self.list.InsertColumn(9, u"配伍穴位")
        self.list.InsertColumn(10, u"存储位置")
        self.list.InsertColumn(11, u"注释")
        self.list.InsertColumn(12, u"录入者")

        # 设置各列的宽度
        self.list.SetColumnWidth(0, 60)  # 设置每一列的宽度
        self.list.SetColumnWidth(1, 90)
        self.list.SetColumnWidth(2, 230)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.params, 1, wx.LEFT| wx.RIGHT | wx.EXPAND)
        self.sizer.Add(self.list, 3 , wx.LEFT | wx.EXPAND)

        self.SetSizer(self.sizer)
        self.Fit()

class MyApp(wx.App):
    def OnPreInit(self):
        frame = MyFrame(None, -1, 'NMR Database')
        frame.Show(True)


if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()