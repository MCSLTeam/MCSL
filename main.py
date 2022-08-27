#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 引用库
import os
import string
import time
import psutil
import sys

from shutil import copyfile
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox


# from find_java import findJava


# 主界面
class Ui_MainWindow(QtWidgets.QMainWindow, QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 469)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(620, 330, 100, 100))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(17)
        self.toolButton.setFont(font)
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setObjectName("toolButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 381, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 381, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 60, 51, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(620, 220, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(620, 270, 101, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_3.setObjectName("toolButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 130, 251, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(320, 130, 241, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 561, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 171, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 180, 171, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(111, 180, 61, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(2147483647)
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(321, 180, 61, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(2147483647)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(420, 180, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setObjectName("pushButton_8")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 220, 541, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(620, 170, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_5.setGeometry(QtCore.QRect(620, 120, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.toolButton_5.setFont(font)
        self.toolButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_5.setObjectName("toolButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MCSL v1.1 By 落雪无痕LxHTT&ChinaT"))
        configpath = "config.mcsl.ini"

        if os.path.exists(configpath):
            check_config = open(configpath)
            check_config1 = check_config.read()
            if check_config1 != "":
                getconfig = open(configpath, 'r')
                getconfigall = str(getconfig.read())
                configall = getconfigall.split(";")
                getjavapath = configall[0]
                getmin_mem = configall[1]
                getmax_mem = configall[2]
                self.lineEdit.setText(getjavapath)
                get_set_java = open(r'config//javapath.ini', 'w+')
                get_set_java.write(getjavapath)
                get_set_java.close()

                self.spinBox.setValue(int(getmin_mem))
                get_set_minmem = open(r'config//minmem.ini', 'w+')
                get_set_minmem.write(str(getmin_mem))
                get_set_minmem.close()

                self.spinBox_2.setValue(int(getmax_mem))
                get_set_maxmem = open(r'config//maxmem.ini', 'w+')
                get_set_maxmem.write(str(getmax_mem))
                get_set_maxmem.close()
            else:
                print("114514")
        else:
            print("1919810")
        self.toolButton.setText(_translate("MainWindow", "启动"))
        self.toolButton.clicked.connect(self.start_server)
        self.pushButton.setText(_translate("MainWindow", "退出程序"))
        self.pushButton.clicked.connect(QtWidgets.QApplication.quit)
        self.label.setText(_translate("MainWindow", "设置Java路径：（切勿包含中文和特殊字符）"))
        self.pushButton_2.setText(_translate("MainWindow", "选择..."))
        self.pushButton_2.clicked.connect(self.browse_javaw)
        self.pushButton_3.setText(_translate("MainWindow", "确定"))
        self.pushButton_3.clicked.connect(self.set_java_path)
        self.pushButton_4.setText(_translate("MainWindow", "自动查找"))
        self.pushButton_4.clicked.connect(self.show_fdjava)
        self.toolButton_2.setText(_translate("MainWindow", "下载Java"))
        self.toolButton_2.clicked.connect(self.show_dljava)
        self.toolButton_3.setText(_translate("MainWindow", "下载服务\n器核心"))
        self.toolButton_3.clicked.connect(self.show_dlcore)
        self.pushButton_6.setText(_translate("MainWindow", "选择..."))
        self.pushButton_6.clicked.connect(self.browse_jar)
        self.pushButton_7.setText(_translate("MainWindow", "确定"))
        self.pushButton_7.clicked.connect(self.select_core)
        self.pushButton_8.setText(_translate("MainWindow", "确定"))
        self.pushButton_8.clicked.connect(self.set_memory)
        self.label_2.setText(_translate("MainWindow", "选择服务器核心：（一个服务器仅须操作一次,选过就不需要再操作）"))
        self.label_3.setText(_translate("MainWindow", "最小内存:          MB"))
        self.label_4.setText(_translate("MainWindow", "最大内存:          MB"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">MCSL v1.1  ——Made by LxHTT and ChinaT</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">这是由两个人制作的MC服务器启动器。</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">软件包含了下载、设参、启动诸多功能。</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Java默认下载AdoptOpenJDK，其余可以自行百度。</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">服务器核心默认下载Paper，其余自己搜索（？</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">服务器路径为程序同目录下的</span><span style=\" font-size:12pt; font-weight:600;\">server</span><span style=\" font-size:12pt;\">文件夹。</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">如果无法启动，可使用程序在server文件夹生成的备用启动方式</span><span style=\" font-size:12pt; font-weight:600;\">command.bat</span><span style=\" font-size:12pt;\">。</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">由于暂时不会考虑添加关闭服务器功能，所以如需关闭服务器，请在服务器中输入</span><span style=\" font-size:12pt; font-weight:600; color:#c80b37;\">stop</span><span style=\" font-size:12pt;\">指令来安全关闭您的服务器。</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">遇到Bug，请积极反馈。反馈地址：</span><span style=\" font-family:\'JetBrains Mono,monospace\'; font-size:9.8pt; color:#bd93f9;\">https://www.wjx.top/vm/mBwRt23.aspx</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">主程序</span><span style=\" font-size:12pt; color:#00aa00;\">&amp;</span><span style=\" font-size:12pt;\">自动查找Java算法：落雪无痕LxHTT   QQ：3395314362</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">下载模块</span><span style=\" font-size:12pt; color:#00aa00;\">&amp;</span><span style=\" font-size:12pt;\">自动查找Java的UI：ChinaT   QQ：3273789867</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">——————————————————————</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">v1.1更新日志：</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">修复在未选择Jar情况下闪退的Bug</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">增加了配置导入导出功能。</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">增加了许多温馨提示（</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">程序启动默认读取目录下的config.mcsl.ini配置文件。</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">优化了各下载模块的UI。</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">增加自动查找Java功能。（算法由LxHTT编写，UI由ChinaT制作）</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">———————————</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">v1.0更新日志：</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">初版。</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Java自动查找功能暂时不可用，可自行设定路径。</span></p></body></html>"))
        self.toolButton_4.setText(_translate("MainWindow", "导出配置"))
        self.toolButton_4.clicked.connect(self.export_config)
        self.toolButton_5.setText(_translate("MainWindow", "导入配置"))
        self.toolButton_5.clicked.connect(self.import_config)
    #窗口
    def show_dljava(self):
        kill_cmd = str("taskkill /f /im cmd.exe")
        os.system("start ./tools//download_java.exe")
        os.system(kill_cmd)
    def show_fdjava(self):
        QMessageBox.information(self, "提示","稍后，程序会未响应，稍安勿躁，马上就好，请勿关闭程序。\n（关掉此窗口即开始查找）",QMessageBox.Yes)
        self.find_func()
        kill_cmd = str("taskkill /f /im cmd.exe")
        os.system("start ./config//auto_find_java.exe")
        os.system(kill_cmd)
        def checkprocess(processname):
            global ljavapath
            pl = psutil.pids()
            for pid in pl:
                if psutil.Process(pid).name() == processname:
                    return pid
        if isinstance(checkprocess("auto_find_java.exe"), int):
            time.sleep(10)
            auto_set_java = open(r'config//javapath.ini', 'r')
            ljavapath = auto_set_java.read()
            auto_set_java.close()
            self.lineEdit.setText(ljavapath)
        else:
            print("1145141919810")

    def show_dlcore(self):
        kill_cmd = str("taskkill /f /im cmd.exe")
        os.system("start ./tools//download_core.exe")
        os.system(kill_cmd)

    #设置
    def browse_javaw(self):
        global ljavapath
        javagetStr = QFileDialog.getOpenFileName(self, '选择javaw.exe程序', os.getcwd(), "javaw.exe")
        ljavapath = javagetStr[0]
        self.lineEdit.setText(ljavapath)
    def set_java_path(self):
        global ljavapath
        ljavapath = self.lineEdit.text()
        file_set_java = open(r'config//javapath.ini','w+')
        file_set_java.write(ljavapath)
        file_set_java.close()

    def set_memory(self):
        global lmin_mem
        global lmax_mem
        lmin_mem = self.spinBox.value()
        lmax_mem = self.spinBox_2.value()
        file_set_minmem = open(r'config//minmem.ini', 'w+')
        file_set_minmem.write(str(lmin_mem))
        file_set_minmem.close()
        file_set_maxmem = open(r'config//maxmem.ini','w+')
        file_set_maxmem.write(str(lmax_mem))
        file_set_maxmem.close()

    def browse_jar(self):
        global jar
        core_get_Str = QFileDialog.getOpenFileName(self, '选择Jar文件', os.getcwd(), "Jar文件(*.jar)")
        lcorepath = core_get_Str[0]
        if lcorepath != "":
            jar = True
        else:
            jar = False
        file_set_core = open(r'config//corepath.ini', 'w+')
        file_set_core.write(lcorepath)
        file_set_core.close()
    def select_core(self):
        if jar == True:
            getCore = open(r'config//corepath.ini', 'r')
            Core = os.path.abspath(str(getCore.read()))
            toCore = os.path.abspath(r'server//server.jar')
            getCore.close()
            copyfile(Core,toCore)
        else:
            QMessageBox.information(self, "提示", "你似乎还没有选择Jar文件...",QMessageBox.Yes)

    def export_config(self):
        global ljavapath
        global lmin_mem
        global lmax_min
        QMessageBox.information(self, "提示", "导出前，请确定你已经设置好了以下参数：\n1.Java路径\n2.最小内存\n3.最大内存", QMessageBox.Yes)
        export_config = open('config.mcsl.ini', 'w+')
        ljavapath = self.lineEdit.text()
        lmin_mem = self.spinBox.value()
        lmax_mem = self.spinBox_2.value()
        export_content = ljavapath + ";" + str(lmin_mem) + ";" + str(lmax_mem)
        export_config.write(export_content)
        export_config.close()
        QMessageBox.information(self, "成功","已保存在程序所在目录",QMessageBox.Yes)
    def import_config(self):
        QMessageBox.information(self, "提示","请在接下来的窗口选择配置",QMessageBox.Yes)
        configgetStr = QFileDialog.getOpenFileName(self, '选择配置文件', os.getcwd(), "MCSL配置(*.mcsl.ini)")
        import_path = configgetStr[0]
        if import_path != "":
            getconfig = open(import_path,'r')
            get_config_all = str(getconfig.read())
            config_all = get_config_all.split(";")
            get_java_path = config_all[0]
            get_min_mem = config_all[1]
            get_max_mem = config_all[2]
            self.lineEdit.setText(get_java_path)
            get_set_java = open(r'config//javapath.ini', 'w+')
            get_set_java.write(get_java_path)
            get_set_java.close()

            self.spinBox.setValue(int(get_min_mem))
            get_set_min_mem = open(r'config//minmem.ini', 'w+')
            get_set_min_mem.write(str(get_min_mem))
            get_set_min_mem.close()

            self.spinBox_2.setValue(int(get_max_mem))
            get_set_max_mem = open(r'config//maxmem.ini', 'w+')
            get_set_max_mem.write(str(get_max_mem))
            get_set_max_mem.close()
        else:
            QMessageBox.information(self, "啊这", "你啥也没选", QMessageBox.Yes)

    #开服
    def start_server(self):
        QMessageBox.information(self, "提示","按下后，程序未响应属正常现象，您可以放心的关掉MCSL，并静待您的服务器启动。\n关掉此窗口即开始运行",QMessageBox.Yes)
        getJavaPath = open(r'config//javapath.ini','r')
        JavaPath = str(getJavaPath.read())
        getJavaPath.close()
        getMinMem = open(r'config//minmem.ini','r')
        MinMem = str(getMinMem.read())
        getMinMem.close()
        getMaxMem = open(r'config//maxmem.ini','r')
        MaxMem = str(getMaxMem.read())
        getMaxMem.close()
        command = str("\"" + JavaPath + "\" -server -Xms" + MinMem + "M -Xmx" + MaxMem + "M -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -jar \"server.jar\"")
        save_command = open(r'server//command.bat','+w')
        save_command.write(command)
        save_command.close()
        os.chdir("server")
        os.system(r"command.bat")

    def find_func(self):
        global panL
        filename = 'javaw.exe'
        disk_list = []
        itl = open(r'config//javalist.ini', 'w+')
        itl.write("")
        itl.close()

        def list_disk():
            for c in string.ascii_uppercase:
                disk = c + ":"
                if os.path.isdir(disk):
                    disk = c + ":"
                    disk_list.append(disk)
            pan = open(r'config//disklist.ini', 'w+')
            count = len(disk_list)
            w1 = 0

            for w1 in range(count):
                write_disk = disk_list[w1] + "\n"
                pan.write(write_disk)
                w1 = w1 + 1
            pan.close()

        def find_java():
            global panL
            result = []
            path = panL + '\\'
            i = 0
            for root, lists, files in os.walk(path):
                for file in files:
                    if filename in file:
                        i = i + 1
                        wr1te = os.path.join(root, file)  # 搜索
                        # print('%s' % (wr1te))
                        result.append(wr1te)
                        i = i + 1
            count = len(result)
            w1 = 0
            javalist = open(r'config//javalist.ini', 'a+')
            for w1 in range(count):
                write_java = result[w1] + "\n"
                javalist.write(write_java)
                w1 = w1 + 1
            javalist.close()

        list_disk()
        x = 0
        for x in range(len(disk_list)):
            panL = disk_list[x]
            find_java()
            x = x + 1
# 启动应用
jar = False
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())