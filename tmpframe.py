# -*- coding:utf-8 -*-

import wx
import wx.aui, wx.grid
import sys
from Infoact import *
from information import *
from Acuact import *

reload(sys)
sys.setdefaultencoding('utf8')


class AddFrame(wx.Frame):
    # 添加信息弹出的小窗口
    def __init__(self, parent, title):

        self.mainframe = parent

        wx.Frame.__init__(self, parent, title=title, size=(1300, 500))

        self.panel = wx.Panel(self, pos=(0, 0), size=(1300, 500))
        self.panel.SetBackgroundColour("#FFFFFF")

        # 12个编辑框
        col1 = wx.StaticText(self.panel, -1, u"文献统一编号", pos=(5, 8), size=(80, 25))
        col2 = wx.TextCtrl(self.panel, -1, u"不可为空", pos=(100, 8), size=(300, 30))
        self.iid = col2

        col3 = wx.StaticText(self.panel, -1, u"文献类别", pos=(450, 8), size=(50, 25))
        col4 = wx.TextCtrl(self.panel, -1, pos=(500, 8), size=(300, 30))
        self.typel = col4

        col5 = wx.StaticText(self.panel, -1, u"文献题目", pos=(850, 8), size=(50, 25))
        col6 = wx.TextCtrl(self.panel, -1, pos=(900, 8), size=(300, 30))
        self.title = col6

        col7 = wx.StaticText(self.panel, -1, u"所有作者", pos=(5, 100), size=(80, 25))
        col8 = wx.TextCtrl(self.panel, -1, pos=(100, 100), size=(300, 30))
        self.author = col8

        col9 = wx.StaticText(self.panel, -1, u"通讯作者", pos=(450, 100), size=(50, 25))
        col10 = wx.TextCtrl(self.panel, -1, pos=(500, 100), size=(300, 30))
        self.corauthor = col10

        col11 = wx.StaticText(self.panel, -1, u"发表日期", pos=(850, 100), size=(50, 25))
        col12 = wx.TextCtrl(self.panel, -1, pos=(900, 100), size=(300, 30))
        self.datel = col12

        col13 = wx.StaticText(self.panel, -1, u"疾病", pos=(5, 200), size=(80, 25))
        col14 = wx.TextCtrl(self.panel, -1, pos=(100, 200), size=(300, 100), style=wx.TE_MULTILINE)
        col25 = wx.StaticText(self.panel, -1, u"疾病用'，'隔开，结尾不要有'。'", pos=(100, 300), size=(300, 25))
        self.disease = col14

        col15 = wx.StaticText(self.panel, -1, u"症状", pos=(450, 200), size=(50, 25))
        col16 = wx.TextCtrl(self.panel, -1, pos=(500, 200), size=(300, 100), style=wx.TE_MULTILINE)
        col26 = wx.StaticText(self.panel, -1, u"症状用'，'隔开，结尾不要有'。'", pos=(100, 300), size=(300, 25))
        self.symptom = col16

        col17 = wx.StaticText(self.panel, -1, u"配伍穴位", pos=(850, 200), size=(50, 25))
        col18 = wx.TextCtrl(self.panel, -1, u"不可为空", pos=(900, 200), size=(300, 100), style=wx.TE_MULTILINE)
        col27 = wx.StaticText(self.panel, -1, u"穴位用'，'隔开，不同配伍用'；'隔开，结尾不要有'。'", pos=(900, 300), size=(300, 25))
        col18.SetBackgroundColour("#FF3030")
        self.acupoint = col18

        col19 = wx.StaticText(self.panel, -1, u"文献存储位置", pos=(5, 350), size=(80, 25))
        col20 = wx.TextCtrl(self.panel, -1, pos=(100, 350), size=(300, 30))
        self.location = col20

        col21 = wx.StaticText(self.panel, -1, u"注释", pos=(450, 350), size=(50, 25))
        col22 = wx.TextCtrl(self.panel, -1, pos=(500, 350), size=(300, 30))
        self.annotation = col22

        col23 = wx.StaticText(self.panel, -1, u"录入者", pos=(850, 350), size=(50, 25))
        col24 = wx.TextCtrl(self.panel, -1, u"不可为空", pos=(900, 350), size=(300, 30))
        self.writer = col24

        save_info = wx.Button(self.panel, label=u"保存", pos=(5, 400))
        self.Bind(wx.EVT_BUTTON, self.saveInfo, save_info)

        # 数据库接口
        self.dbInfo = Infoact()

    def saveInfo(self, evt):
        '''
            #获取文本，插入数据
        :param evt:
        :return:
        '''

        iid = self.iid.GetValue()
        typel = self.typel.GetValue()
        title = self.title.GetValue()
        author = self.author.GetValue()
        corauthor = self.corauthor.GetValue()
        datel = self.datel.GetValue()
        disease = self.disease.GetValue()
        symptom = self.symptom.GetValue()
        acupoint = self.acupoint.GetValue()
        location = self.location.GetValue()
        annotation = self.annotation.GetValue()
        writer = self.writer.GetValue()

        if iid == '' or acupoint == '' or writer == '':
            warn = wx.MessageDialog(self, message=u"有非空字段为空！", caption=u"错误警告", style=wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()  # 提示错误
            warn.Destroy()
            return

        else:
            print u'开始写入'

            info = Information(iid, typel, title, author, corauthor, datel, disease, symptom, acupoint, location,
                               annotation, writer)
            if self.mainframe.adjust_acupoint(acupoint) == 0:
                self.dbInfo.insertInfo(info)
                #self.mainframe.addToList()
                index = self.mainframe.list.InsertStringItem(sys.maxint, iid)
                self.mainframe.list.SetStringItem(index, 1, title)
                self.mainframe.list.SetStringItem(index, 2, acupoint)
                self.mainframe.list.SetStringItem(index, 3, writer)

        self.Destroy()

class UpdateFrame(wx.Frame):
    # 更改信息，先显示信息，后更改
    def __init__(self, parent, title, select_id):
        self.mainframe = parent

        wx.Frame.__init__(self, parent, title=title, size=(1300, 500))

        self.panel = wx.Panel(self, pos=(0, 0), size=(1300, 500))
        self.panel.SetBackgroundColour("#FFFFFF")

        # 12个编辑框
        col1 = wx.StaticText(self.panel, -1, u"文献统一编号", pos=(5, 8), size=(80, 25))
        col2 = wx.TextCtrl(self.panel, -1, style=wx.TE_READONLY, pos=(100, 8), size=(300, 30))
        col2.SetBackgroundColour("#BBFFFF")
        self.iid = col2

        col3 = wx.StaticText(self.panel, -1, u"文献类别", pos=(450, 8), size=(50, 25))
        col4 = wx.TextCtrl(self.panel, -1, pos=(500, 8), size=(300, 30))
        self.typel = col4

        col5 = wx.StaticText(self.panel, -1, u"文献题目", pos=(850, 8), size=(50, 25))
        col6 = wx.TextCtrl(self.panel, -1, pos=(900, 8), size=(300, 30))
        self.title = col6

        col7 = wx.StaticText(self.panel, -1, u"所有作者", pos=(5, 100), size=(80, 25))
        col8 = wx.TextCtrl(self.panel, -1, pos=(100, 100), size=(300, 30))
        self.author = col8

        col9 = wx.StaticText(self.panel, -1, u"通讯作者", pos=(450, 100), size=(50, 25))
        col10 = wx.TextCtrl(self.panel, -1, pos=(500, 100), size=(300, 30))
        self.corauthor = col10

        col11 = wx.StaticText(self.panel, -1, u"发表日期", pos=(850, 100), size=(50, 25))
        col12 = wx.TextCtrl(self.panel, -1, pos=(900, 100), size=(300, 30))
        self.datel = col12

        col13 = wx.StaticText(self.panel, -1, u"疾病", pos=(5, 200), size=(80, 25))
        col14 = wx.TextCtrl(self.panel, -1, pos=(100, 200), size=(300, 100), style=wx.TE_MULTILINE)
        col25 = wx.StaticText(self.panel, -1, u"疾病用'，'隔开，结尾不要有'。'", pos=(100, 300), size=(300, 25))
        self.disease = col14

        col15 = wx.StaticText(self.panel, -1, u"症状", pos=(450, 200), size=(50, 25))
        col16 = wx.TextCtrl(self.panel, -1, pos=(500, 200), size=(300, 100), style=wx.TE_MULTILINE)
        col26 = wx.StaticText(self.panel, -1, u"不同症状用'，'隔开，结尾不要有'。'", pos=(500, 300), size=(300, 25))
        self.symptom = col16

        col17 = wx.StaticText(self.panel, -1, u"配伍穴位", pos=(850, 200), size=(50, 25))
        col18 = wx.TextCtrl(self.panel, -1, u"不可为空", pos=(900, 200), size=(300, 100), style=wx.TE_MULTILINE)
        col27 = wx.StaticText(self.panel, -1, u"穴位用'，'隔开，不同配伍用'；'隔开，结尾不要有'。'", pos=(900, 300), size=(300, 25))
        col18.SetBackgroundColour("#FF3030")
        self.acupoint = col18

        col19 = wx.StaticText(self.panel, -1, u"文献存储位置", pos=(5, 350), size=(80, 25))
        col20 = wx.TextCtrl(self.panel, -1, pos=(100, 350), size=(300, 30))
        self.location = col20

        col21 = wx.StaticText(self.panel, -1, u"注释", pos=(450, 350), size=(50, 25))
        col22 = wx.TextCtrl(self.panel, -1, pos=(500, 350), size=(300, 30))
        self.annotation = col22

        col23 = wx.StaticText(self.panel, -1, u"录入者", pos=(850, 350), size=(50, 25))
        col24 = wx.TextCtrl(self.panel, -1, u"不可为空", pos=(900, 350), size=(300, 30))
        self.writer = col24

        save_info = wx.Button(self.panel, label=u"保存", pos=(5, 400))
        self.Bind(wx.EVT_BUTTON, self.Update, save_info)

        self.select_id = select_id
        self.infoiid = self.mainframe.list.GetItem(select_id, 0).Text

        # 连接数据库
        self.dbInfo = Infoact()
        self.showAllText()

    def showAllText(self):
        data = self.dbInfo.getInfoById(self.infoiid)

        self.iid.SetValue(data[0])
        self.typel.SetValue(data[1])
        self.title.SetValue(data[2])
        self.author.SetValue(data[3])
        self.corauthor.SetValue(data[4])
        self.datel.SetValue(data[5])
        self.disease.SetValue(data[6])
        self.symptom.SetValue(data[7])
        self.acupoint.SetValue(data[8])
        self.location.SetValue(data[9])
        self.annotation.SetValue(data[10])
        self.writer.SetValue(data[11])

    def Update(self, evt):
        #保存修改后的值
        iid = self.iid.GetValue()
        typel = self.typel.GetValue()
        title = self.title.GetValue()
        author = self.author.GetValue()
        corauthor = self.corauthor.GetValue()
        datel = self.datel.GetValue()
        disease = self.disease.GetValue()
        symptom = self.symptom.GetValue()
        acupoint = self.acupoint.GetValue()
        location = self.location.GetValue()
        annotation = self.annotation.GetValue()
        writer = self.writer.GetValue()

        if iid == '' or acupoint == '' or writer == '':
            warn = wx.MessageDialog(self, message=u"有非空字段为空！", caption=u"错误警告", style=wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()  # 提示错误
            warn.Destroy()
            return

        else:
            print u'开始写入'

            info = Information(iid, typel, title, author, corauthor, datel, disease, symptom, acupoint, location,
                               annotation, writer)

            if self.mainframe.adjust_acupoint(acupoint) == 0:
                self.dbInfo.saveUpdate(iid, info)

                #修改list中数据
                self.mainframe.list.SetStringItem(self.select_id, 1, title)
                self.mainframe.list.SetStringItem(self.select_id, 2, acupoint)
                self.mainframe.list.SetStringItem(self.select_id, 3, writer)

                self.Destroy()

class ShowFrame(wx.Frame):
    # 显示具体信息
    def __init__(self, parent, title, select_id):
        self.mainframe = parent

        wx.Frame.__init__(self, parent, title=title, size=(1300, 500))

        self.panel = wx.Panel(self, pos=(0, 0), size=(1300, 500))
        self.panel.SetBackgroundColour("#FFFFFF")

        # 12个编辑框
        col1 = wx.StaticText(self.panel, -1, u"文献统一编号", pos=(5, 8), size=(80, 25))
        col2 = wx.TextCtrl(self.panel, -1, pos=(100, 8), size=(300, 30), style=wx.TE_READONLY)
        col2.SetBackgroundColour("#FFFFFF")
        self.iid = col2

        col3 = wx.StaticText(self.panel, -1, u"文献类别", pos=(450, 8), size=(50, 25))
        col4 = wx.TextCtrl(self.panel, -1, pos=(500, 8), size=(300, 30), style=wx.TE_READONLY)
        col4.SetBackgroundColour("#FFFFFF")
        self.typel = col4

        col5 = wx.StaticText(self.panel, -1, u"文献题目", pos=(850, 8), size=(50, 25))
        col6 = wx.TextCtrl(self.panel, -1, pos=(900, 8), size=(300, 30), style=wx.TE_READONLY)
        col6.SetBackgroundColour("#FFFFFF")
        self.title = col6

        col7 = wx.StaticText(self.panel, -1, u"所有作者", pos=(5, 100), size=(80, 25))
        col8 = wx.TextCtrl(self.panel, -1, pos=(100, 100), size=(300, 30), style=wx.TE_READONLY)
        col8.SetBackgroundColour("#FFFFFF")
        self.author = col8

        col9 = wx.StaticText(self.panel, -1, u"通讯作者", pos=(450, 100), size=(50, 25))
        col10 = wx.TextCtrl(self.panel, -1, pos=(500, 100), size=(300, 30), style=wx.TE_READONLY)
        col10.SetBackgroundColour("#FFFFFF")
        self.corauthor = col10

        col11 = wx.StaticText(self.panel, -1, u"发表日期", pos=(850, 100), size=(50, 25))
        col12 = wx.TextCtrl(self.panel, -1, pos=(900, 100), size=(300, 30), style=wx.TE_READONLY)
        col12.SetBackgroundColour("#FFFFFF")
        self.datel = col12

        col13 = wx.StaticText(self.panel, -1, u"疾病", pos=(5, 200), size=(80, 25))
        col14 = wx.TextCtrl(self.panel, -1, pos=(100, 200), size=(300, 100), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.disease = col14

        col15 = wx.StaticText(self.panel, -1, u"症状", pos=(450, 200), size=(50, 25))
        col16 = wx.TextCtrl(self.panel, -1, pos=(500, 200), size=(300, 100), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.symptom = col16

        col17 = wx.StaticText(self.panel, -1, u"配伍穴位", pos=(850, 200), size=(50, 25))
        col18 = wx.TextCtrl(self.panel, -1, pos=(900, 200), size=(300, 100), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.acupoint = col18

        col19 = wx.StaticText(self.panel, -1, u"文献存储位置", pos=(5, 350), size=(80, 25))
        col20 = wx.TextCtrl(self.panel, -1, pos=(100, 350), size=(300, 30), style=wx.TE_READONLY)
        col20.SetBackgroundColour("#FFFFFF")
        self.location = col20

        col21 = wx.StaticText(self.panel, -1, u"注释", pos=(450, 350), size=(50, 25))
        col22 = wx.TextCtrl(self.panel, -1, pos=(500, 350), size=(300, 30), style=wx.TE_READONLY)
        col22.SetBackgroundColour("#FFFFFF")
        self.annotation = col22

        col23 = wx.StaticText(self.panel, -1, u"录入者", pos=(850, 350), size=(50, 25))
        col24 = wx.TextCtrl(self.panel, -1, pos=(900, 350), size=(300, 30), style=wx.TE_READONLY)
        col24.SetBackgroundColour("#FFFFFF")
        self.writer = col24

        self.select_id = select_id
        self.infoiid = self.mainframe.list.GetItem(select_id, 0).Text

        # 连接数据库
        self.dbInfo = Infoact()
        self.showAllText()

    def showAllText(self):
        data = self.dbInfo.getInfoById(self.infoiid)

        self.iid.SetValue(data[0])
        self.typel.SetValue(data[1])
        self.title.SetValue(data[2])
        self.author.SetValue(data[3])
        self.corauthor.SetValue(data[4])
        self.datel.SetValue(data[5])
        self.disease.SetValue(data[6])
        self.symptom.SetValue(data[7])
        self.acupoint.SetValue(data[8])
        self.location.SetValue(data[9])
        self.annotation.SetValue(data[10])
        self.writer.SetValue(data[11])

class MyFrame(wx.Frame):
    """
        create the Frame for NMR
        mneubar,statusbar,mult-windows
    """

    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition, wx.Size(800, 400))

        # 生成一个列表
        self.list = wx.ListCtrl(self, -1, size=(800, 300),
                                style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)

        self.list.InsertColumn(0, u"编号")
        self.list.InsertColumn(1, u"题目")
        self.list.InsertColumn(2, u"配伍穴位")
        self.list.InsertColumn(3, u"录入者")

        # 设置各列的宽度
        self.list.SetColumnWidth(0, 150)
        self.list.SetColumnWidth(1, 250)
        self.list.SetColumnWidth(2, 250)
        self.list.SetColumnWidth(3, 100)

        # 添加一组按钮，实现增删改查,用一个panel来管理该组按钮的布局
        self.panel = wx.Panel(self, pos=(0, 300), size=(400, 100))

        # 定义一组按钮
        # base information of database
        table_list = ['Acupoint', 'Information']

        self.qName = wx.StaticText(self.panel, -1, "DataBase:", pos=(10, 15), size=(60, 30))
        self.qName0 = wx.TextCtrl(self.panel, -1, value='Acupuncture', pos=(80, 15), style=wx.TE_READONLY | wx.TE_CENTER,
                                  size=(80, -1))
        self.qName1 = wx.StaticText(self.panel, -1, "Table:", pos=(180, 15))
        self.qName0 = wx.TextCtrl(self.panel, -1, value='Information', pos=(230, 15), style=wx.TE_READONLY | wx.TE_CENTER,
                                  size=(80, -1))

        # 操作按钮
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

        # 添加数据库操作对象
        self.dbhelper = Infoact()
        datas = self.dbhelper.getAll()

        for j in range(len(datas)):
            data = datas[j]
            index = self.list.InsertStringItem(sys.maxint, data[0])
            # self.list.SetStringItem(index, 1, str(data[0]))
            self.list.SetStringItem(index, 1, data[1])
            self.list.SetStringItem(index, 2, data[2])
            self.list.SetStringItem(index, 3, data[3])

    def add_data(self, evt):
        add_f = AddFrame(self, u'添加信息')
        add_f.Show(True)

    def delete(self, event):
        selectId = self.list.GetFirstSelected()
        if selectId == -1:
            warn = wx.MessageDialog(self, message=u"未选中任何条目！！！", caption=u"错误警告", style=wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()  # 提示错误
            warn.Destroy()
            return
        else:
            iid = self.list.GetItem(selectId, 0).Text
            self.list.DeleteItem(selectId)
            self.dbhelper.deleteInfo(iid)

    def modify(self, event):
        selectId = self.list.GetFirstSelected()
        if selectId == -1:
            warn = wx.MessageDialog(self, message=u"未选中任何条目！！！", caption=u"错误警告", style=wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()  # 提示错误
            warn.Destroy()
            return
        else:
            show_f = UpdateFrame(self, u"修改窗口", selectId)
            show_f.Show(True)

    def select_data(self, event):
        selectId = self.list.GetFirstSelected()
        if selectId == -1:
            warn = wx.MessageDialog(self, message=u"未选中任何条目！！！", caption=u"错误警告", style=wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()  # 提示错误
            warn.Destroy()
            return
        else:
            show_f = ShowFrame(self, u"查看窗口", selectId)
            show_f.Show(True)

    def adjust_acupoint(self, acupoint):
        dbAcu = Acuact()
        acupoints = dbAcu.getChinese()
        points = acupoint.split('；')
        point_list = []
        for item in points:
            point_list.append(item.split('，'))
        # print point_list
        tmp_label = 0
        id_list = []
        for acu_list in point_list:

            for item in acu_list:
                if item not in acupoints:
                    warn = wx.MessageDialog(self, message='"' + item + '"' + u"不在数据库中，请检查是否有别名！", caption=u"错误警告",
                                            style=wx.YES_DEFAULT | wx.ICON_ERROR)
                    warn.ShowModal()
                    warn.Destroy()
                    tmp_label = 1
                    break
                # else:
                #     for (index, acu) in enumerate(acupoints):
                #         if item == acu
        return tmp_label

class MyApp(wx.App):
    def OnPreInit(self):
        frame = MyFrame(None, -1, 'NMR Database')
        frame.Show(True)


if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()