#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 引用库
import os
import string
import sys
import time
from shutil import copyfile

import psutil
import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox


# 主界面
class Ui_MainWindow(QtWidgets.QMainWindow, QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setFixedSize(752, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.start_pushButton.setGeometry(QtCore.QRect(620, 330, 100, 100))
        self.start_pushButton.setStyleSheet("QPushButton{\n"
                                    "    background:Gray;\n"
                                    "    color:white;\n"
                                    "    box-shadow: 1px 1px 3px;font-size:25px;border-radius: 10px\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    background:black;\n"
                                    "}")
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(17)
        self.start_pushButton.setFont(font)
        self.start_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_pushButton.setObjectName("start_pushButton")
        self.exit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.exit_pushButton.setGeometry(QtCore.QRect(620, 20, 101, 41))
        self.exit_pushButton.setStyleSheet("QPushButton{\n"
                                    "    background:Red;\n"
                                    "    color:White;\n"
                                    "    box-shadow: 1px 1px 3px;font-size:14px;border-radius: 5px\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    background:black;\n"
                                    "}")
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.exit_pushButton.setFont(font)
        self.exit_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.set_java_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.set_java_lineEdit.setGeometry(QtCore.QRect(30, 60, 381, 31))
        self.set_java_lineEdit.setObjectName("set_java_lineEdit")
        self.set_java_label = QtWidgets.QLabel(self.centralwidget)
        self.set_java_label.setGeometry(QtCore.QRect(30, 40, 381, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.set_java_label.setFont(font)
        self.set_java_label.setTextFormat(QtCore.Qt.PlainText)
        self.set_java_label.setObjectName("set_java_label")
        self.set_java_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.set_java_pushButton.setGeometry(QtCore.QRect(420, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.set_java_pushButton.setFont(font)
        self.set_java_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_java_pushButton.setObjectName("set_java_pushButton")
        self.set_java_ok_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.set_java_ok_pushButton.setGeometry(QtCore.QRect(560, 60, 51, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.set_java_ok_pushButton.setFont(font)
        self.set_java_ok_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_java_ok_pushButton.setObjectName("set_java_ok_pushButton")
        self.auto_find_java_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.auto_find_java_pushButton.setGeometry(QtCore.QRect(490, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.auto_find_java_pushButton.setFont(font)
        self.auto_find_java_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.auto_find_java_pushButton.setObjectName("auto_find_java_pushButton")
        self.auto_find_java_pushButton.setStyleSheet("QPushButton{\n"
                                    "    background:yellow;\n"
                                    "    color:Black;\n"
                                    "    box-shadow: 1px 1px 3px;font-size:12px;border-radius: 5px\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    background:black;\n"
                                    "}")
        self.download_toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.download_toolButton.setGeometry(QtCore.QRect(620, 220, 101, 101))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(17)
        self.download_toolButton.setFont(font)
        self.download_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.download_toolButton.setObjectName("download_toolButton")
        self.download_toolButton.setStyleSheet("QToolButton{\n"
                                    "    background:white;\n"
                                    "    color:Black;\n"
                                    "    box-shadow: 1px 1px 3px;font-size:25px;border-radius: 10px\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    background:black;\n"
                                    "}")
        self.set_core_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.set_core_pushButton.setGeometry(QtCore.QRect(30, 130, 251, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.set_core_pushButton.setFont(font)
        self.set_core_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_core_pushButton.setObjectName("set_core_pushButton")
        self.copy_core_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.copy_core_pushButton.setGeometry(QtCore.QRect(320, 130, 241, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.copy_core_pushButton.setFont(font)
        self.copy_core_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copy_core_pushButton.setObjectName("copy_core_pushButton")
        self.set_core_label = QtWidgets.QLabel(self.centralwidget)
        self.set_core_label.setGeometry(QtCore.QRect(30, 110, 561, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.set_core_label.setFont(font)
        self.set_core_label.setTextFormat(QtCore.Qt.PlainText)
        self.set_core_label.setObjectName("set_core_label")
        self.min_mem_label = QtWidgets.QLabel(self.centralwidget)
        self.min_mem_label.setGeometry(QtCore.QRect(29, 180, 171, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.min_mem_label.setFont(font)
        self.min_mem_label.setTextFormat(QtCore.Qt.PlainText)
        self.min_mem_label.setObjectName("min_mem_label")
        self.max_mem_label = QtWidgets.QLabel(self.centralwidget)
        self.max_mem_label.setGeometry(QtCore.QRect(290, 180, 171, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.max_mem_label.setFont(font)
        self.max_mem_label.setTextFormat(QtCore.Qt.PlainText)
        self.max_mem_label.setObjectName("max_mem_label")
        self.min_mem_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.min_mem_spinBox.setGeometry(QtCore.QRect(100, 180, 71, 22))
        self.min_mem_spinBox.setObjectName("min_mem_spinBox")
        self.min_mem_spinBox.setMinimum(1)
        self.min_mem_spinBox.setMaximum(2147483647)
        self.max_mem_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.max_mem_spinBox.setGeometry(QtCore.QRect(360, 180, 71, 22))
        self.max_mem_spinBox.setObjectName("max_mem_spinBox")
        self.max_mem_spinBox.setMinimum(1)
        self.max_mem_spinBox.setMaximum(2147483647)
        self.mem_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.mem_pushButton.setGeometry(QtCore.QRect(500, 170, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.mem_pushButton.setFont(font)
        self.mem_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mem_pushButton.setObjectName("mem_pushButton")
        self.introduction_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.introduction_textBrowser.setGeometry(QtCore.QRect(20, 220, 541, 211))
        self.introduction_textBrowser.setObjectName("introduction_textBrowser")
        self.export_config_toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.export_config_toolButton.setGeometry(QtCore.QRect(620, 170, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.export_config_toolButton.setFont(font)
        self.export_config_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.export_config_toolButton.setObjectName("export_config_toolButton")
        self.export_config_toolButton.setStyleSheet("QToolButton{\n"
                                    "    background:yellow;\n"
                                    "    color:Black;\n"
                                    "    box-shadow: 1px 1px 3px;font-size:14px;border-radius: 5px\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    background:black;\n"
                                    "}")
        self.import_config_toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.import_config_toolButton.setGeometry(QtCore.QRect(620, 120, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.import_config_toolButton.setFont(font)
        self.import_config_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.import_config_toolButton.setObjectName("import_config_toolButton")
        self.import_config_toolButton.setStyleSheet("QToolButton{\n"
                                    "    background:yellow;\n"
                                    "    color:Black;\n"
                                    "    box-shadow: 1px 1px 3px;font-size:14px;border-radius: 5px\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    background:black;\n"
                                    "}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
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
                self.set_java_lineEdit.setText(getjavapath)
                get_set_java = open(r'config//javapath.ini', 'w+')
                get_set_java.write(getjavapath)
                get_set_java.close()

                self.min_mem_spinBox.setValue(int(getmin_mem))
                get_set_minmem = open(r'config//minmem.ini', 'w+')
                get_set_minmem.write(str(getmin_mem))
                get_set_minmem.close()
                self.max_mem_spinBox.setValue(int(getmax_mem))
                get_set_maxmem = open(r'config//maxmem.ini', 'w+')
                get_set_maxmem.write(str(getmax_mem))
                get_set_maxmem.close()
            else:
                print("1")
        else:
            print("1")
        self.start_pushButton.setText(_translate("MainWindow", "启动"))
        self.start_pushButton.clicked.connect(self.start_server)
        self.exit_pushButton.setText(_translate("MainWindow", "退出程序"))
        self.exit_pushButton.clicked.connect(self.exit_submit)
        self.set_java_label.setText(_translate("MainWindow", "设置Java路径：（切勿包含中文和特殊字符）"))
        self.set_java_pushButton.setText(_translate("MainWindow", "选择..."))
        self.set_java_pushButton.clicked.connect(self.browse_javaw)
        self.set_java_ok_pushButton.setText(_translate("MainWindow", "确定"))
        self.set_java_ok_pushButton.clicked.connect(self.set_java_path)
        self.auto_find_java_pushButton.setText(_translate("MainWindow", "自动查找"))
        self.auto_find_java_pushButton.clicked.connect(self.show_fdjava)
        self.download_toolButton.setText(_translate("MainWindow", "下载"))
        self.download_toolButton.clicked.connect(self.show_dl)
        self.set_core_pushButton.setText(_translate("MainWindow", "选择..."))
        self.set_core_pushButton.clicked.connect(self.browse_jar)
        self.copy_core_pushButton.setText(_translate("MainWindow", "确定"))
        self.copy_core_pushButton.clicked.connect(self.select_core)
        self.mem_pushButton.setText(_translate("MainWindow", "确定"))
        self.mem_pushButton.clicked.connect(self.set_memory)
        self.set_core_label.setText(_translate("MainWindow", "选择服务器核心：（一个服务器仅须操作一次,选过就不需要再操作）"))
        self.min_mem_label.setText(_translate("MainWindow", "最小内存:            MB"))
        self.max_mem_label.setText(_translate("MainWindow", "最大内存:            MB"))
        self.introduction_textBrowser.setHtml(_translate("MainWindow",
                                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">MCSL v1.2  ——Made by LxHTT and ChinaT</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">这是由两个人制作的MC服务器启动器。</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">软件包含了下载、设参、启动诸多功能。</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Java默认下载AdoptOpenJDK，其余可以自行百度。</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体,monospace\'; font-size:12pt; font-weight:600; color:#ff0000;\">服务器核心已经支持了</span><span style=\" font-family:\'JetBrains Mono,monospace\'; font-size:12pt; font-weight:600; color:#ff0000;\">Paper</span><span style=\" font-family:\'宋体,monospace\'; font-size:12pt; font-weight:600; color:#ff0000;\">和</span><span style=\" font-family:\'JetBrains Mono,monospace\'; font-size:12pt; font-weight:600; color:#ff0000;\">Spigot</span><span style=\" font-family:\'宋体,monospace\'; font-size:12pt; font-weight:600; color:#ff0000;\">下载。</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">服务器路径为程序同目录下的</span><span style=\" font-size:12pt; font-weight:600;\">server</span><span style=\" font-size:12pt;\">文件夹。</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">如果无法启动，可使用程序在server文件夹生成的备用启动方式</span><span style=\" font-size:12pt; font-weight:600;\">command.bat</span><span style=\" font-size:12pt;\">。</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">由于暂时不会考虑添加关闭服务器功能，所以如需关闭服务器，请在服务器中输入</span><span style=\" font-size:12pt; font-weight:600; color:#c80b37;\">stop</span><span style=\" font-size:12pt;\">指令来安全关闭您的服务器。</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">遇到Bug，请积极反馈。反馈地址：</span><span style=\" font-family:\'JetBrains Mono,monospace\'; font-size:9.8pt; color:#bd93f9;\">https://www.wjx.top/vm/mBwRt23.aspx</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">主程序</span><span style=\" font-size:12pt; color:#00aa00;\">&amp;</span><span style=\" font-size:12pt;\">自动查找Java算法：落雪无痕LxHTT   QQ：3395314362</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">下载模块</span><span style=\" font-size:12pt; color:#00aa00;\">&amp;</span><span style=\" font-size:12pt;\">自动查找Java的UI：ChinaT   QQ：3273789867</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">——————————————————————</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">v1.2更新日志：</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">整合各个下载程序，集成而强大。</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">美化UI！！！！！！</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">优化代码的逻辑性以及可读性（原先自己都傻了）</span></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">———————————</span></p>\n"
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
        self.export_config_toolButton.setText(_translate("MainWindow", "导出配置"))
        self.export_config_toolButton.clicked.connect(self.export_config)
        self.import_config_toolButton.setText(_translate("MainWindow", "导入配置"))
        self.import_config_toolButton.clicked.connect(self.import_config)

    # 窗口
    def show_dl(self):
        kill_cmd = str("taskkill /f /im cmd.exe")
        os.system("start ./tools//download_tools.exe")
        os.system(kill_cmd)

    def show_fdjava(self):
        QMessageBox.information(self, "提示",
                                "稍后，程序会未响应，稍安勿躁，马上就好，请勿关闭程序。\n（关掉此窗口即开始查找）",
                                QMessageBox.Yes)
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
            self.set_java_lineEdit.setText(ljavapath)
        else:
            print("1145141919810")
    def exit_submit(self):
        result = QMessageBox.question(self, "退出!", "是否真的要退出MCSL？", QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.No)
        if result == QMessageBox.Yes:
            QtWidgets.QApplication.quit()
        else:
            print("1")


    # 设置
    def browse_javaw(self):
        global ljavapath
        javagetStr = QFileDialog.getOpenFileName(self, '选择javaw.exe程序', os.getcwd(), "javaw.exe")
        ljavapath = javagetStr[0]
        self.set_java_lineEdit.setText(ljavapath)

    def set_java_path(self):
        global ljavapath
        ljavapath = self.set_java_lineEdit.text()
        file_set_java = open(r'config//javapath.ini', 'w+')
        file_set_java.write(ljavapath)
        file_set_java.close()

    def set_memory(self):
        global lmin_mem
        global lmax_mem
        lmin_mem = self.min_mem_spinBox.value()
        lmax_mem = self.max_mem_spinBox.value()
        file_set_minmem = open(r'config//minmem.ini', 'w+')
        file_set_minmem.write(str(lmin_mem))
        file_set_minmem.close()
        file_set_maxmem = open(r'config//maxmem.ini', 'w+')
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
            copyfile(Core, toCore)
        else:
            QMessageBox.information(self, "提示", "你似乎还没有选择Jar文件...", QMessageBox.Yes)

    def export_config(self):
        global ljavapath
        global lmin_mem
        global lmax_min
        QMessageBox.information(self, "提示",
                                "导出前，请确定你已经设置好了以下参数：\n1.Java路径\n2.最小内存\n3.最大内存",
                                QMessageBox.Yes)
        export_config = open('config.mcsl.ini', 'w+')
        ljavapath = self.set_java_lineEdit.text()
        lmin_mem = self.min_mem_spinBox.value()
        lmax_mem = self.max_mem_spinBox.value()
        export_content = ljavapath + ";" + str(lmin_mem) + ";" + str(lmax_mem)
        export_config.write(export_content)
        export_config.close()
        QMessageBox.information(self, "成功", "已保存在程序所在目录", QMessageBox.Yes)

    def import_config(self):
        QMessageBox.information(self, "提示", "请在接下来的窗口选择配置", QMessageBox.Yes)
        configgetStr = QFileDialog.getOpenFileName(self, '选择配置文件', os.getcwd(), "MCSL配置(*.mcsl.ini)")
        import_path = configgetStr[0]
        if import_path != "":
            getconfig = open(import_path, 'r')
            get_config_all = str(getconfig.read())
            config_all = get_config_all.split(";")
            get_java_path = config_all[0]
            get_min_mem = config_all[1]
            get_max_mem = config_all[2]
            self.set_java_lineEdit.setText(get_java_path)
            get_set_java = open(r'config//javapath.ini', 'w+')
            get_set_java.write(get_java_path)
            get_set_java.close()

            self.min_mem_spinBox.setValue(int(get_min_mem))
            get_set_min_mem = open(r'config//minmem.ini', 'w+')
            get_set_min_mem.write(str(get_min_mem))
            get_set_min_mem.close()

            self.max_mem_spinBox.setValue(int(get_max_mem))
            get_set_max_mem = open(r'config//maxmem.ini', 'w+')
            get_set_max_mem.write(str(get_max_mem))
            get_set_max_mem.close()
        else:
            QMessageBox.information(self, "啊这", "你啥也没选", QMessageBox.Yes)

    # 开服
    def start_server(self):
        QMessageBox.information(self, "提示",
                                "按下后，程序未响应属正常现象，您可以放心的关掉MCSL，并静待您的服务器启动。\n关掉此窗口即开始运行",
                                QMessageBox.Yes)
        getJavaPath = open(r'config//javapath.ini', 'r')
        JavaPath = str(getJavaPath.read())
        getJavaPath.close()
        getMinMem = open(r'config//minmem.ini', 'r')
        MinMem = str(getMinMem.read())
        getMinMem.close()
        getMaxMem = open(r'config//maxmem.ini', 'r')
        MaxMem = str(getMaxMem.read())
        getMaxMem.close()
        command = str(
            "\"" + JavaPath + "\" -server -Xms" + MinMem + "M -Xmx" + MaxMem + "M -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -jar \"server.jar\"")
        save_command = open(r'server//command.bat', '+w')
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
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.setWindowOpacity(0.87)
MainWindow.setWindowTitle("MCSL v1.2")
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
MainWindow.setWindowIcon(icon)
MainWindow.show()
sys.exit(app.exec_())
