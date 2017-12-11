# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_Dialog import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
<<<<<<< HEAD
=======
         # 利用 super 類別調用 parent 類別中的建構子
>>>>>>> 576ac11b90ef16198e4ac5805d1afd2581a945d4
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        '''以下為使用者自行編寫程式碼區'''
        self.sumSoFar = 0.0
<<<<<<< HEAD
        self.waitingForOperand = True
        
        num_button = [self.one,  self.two,  \
        self.three,  self.four,  self.five,  self.six,  self.seven,  self.eight,  self.nine,  self.zero]
        
        for i in num_button:
            i.clicked.connect(self.digitClicked)
        #self.one.clicked.connect(self.digitClicked)
        
        self.clearButton.clicked.connect(self.clear)

=======
         # 啟動時, 等待輸入運算數
        self.waitingForOperand = True
         # 顯示幕起始
        self.display.setText('0')
         # clear 按鍵
        self.clearButton.clicked.connect(self.clear)
         # 數字按鍵
         # 當多個 signal 同時指向同一個 slot 處理時, 採用 for loop
        digits = [self.one,  self.two,  self.three, \
            self.four,  self.five,  self.six, \
            self.seven,  self.eight,  self.nine,  self.zero]
            
        for i in digits:
            i.clicked.connect(self.digitClicked)
       #self.one.clicked.connect(self.digitClicked)
         # 用於產生加號與減號 signals 與 slots 用的數列
        plus_minus = [self.plusButton,  self.minusButton]
        # 加減鍵的 signals 與 slogts 設定
        for i in plus_minus:
            i.clicked.connect(self.additiveOperatorClicked)
            
>>>>>>> 576ac11b90ef16198e4ac5805d1afd2581a945d4
    def digitClicked(self):
        '''
        使用者按下數字鍵, 必須能夠累積顯示該數字
        當顯示幕已經為 0, 再按零不會顯示 00, 而仍顯示 0 或 0.0
        
        '''
        #pass
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())
<<<<<<< HEAD
        
        if self.display.text() == '0' and digitValue == 0.0:
            return
            
        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False
            
        self.display.setText(self.display.text() + str(digitValue))
        
=======
         # 處理顯示幕為 0 或輸入 0.0 時
        if self.display.text() == '0' and digitValue == 0.0:
         return
         
         # 切換是否等待輸入運算數狀態, 一開始等待運算數, 一有輸入值, 則刷新顯示幕
        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False
        self.display.setText(self.display.text() + str(digitValue))
>>>>>>> 576ac11b90ef16198e4ac5805d1afd2581a945d4
    def unaryOperatorClicked(self):
        '''單一運算元按下後處理方法'''
        pass
        
    def additiveOperatorClicked(self):
        '''加或減按下後進行的處理方法'''
        pass
        
    def multiplicativeOperatorClicked(self):
        '''乘或除按下後進行的處理方法'''
        pass
        
    def equalClicked(self):
        '''等號按下後的處理方法'''
        pass
        
    def pointClicked(self):
        '''小數點按下後的處理方法'''
        pass
        
    def changeSignClicked(self):
        '''變號鍵按下後的處理方法'''
        pass
        
    def backspaceClicked(self):
        '''回復鍵按下的處理方法'''
        pass
        
    def clear(self):
        '''清除鍵按下後的處理方法'''
<<<<<<< HEAD
        if self.waitingForOperand:
            return
 
        self.display.setText('0')
        # 清除顯示幕後, 重置等待運算數狀態變數
        self.waitingForOperand = True
        
=======
        #pass
        # 在等待運算數階段, 直接跳出 slot, 不會清除顯示幕
        if self.waitingForOperand:
            return
        # 清除顯示幕, 回復到原始顯示 0
        self.display.setText('0')
        # 重置判斷是否等待輸入運算數狀態
        self.waitingForOperand = True   
>>>>>>> 576ac11b90ef16198e4ac5805d1afd2581a945d4
    def clearAll(self):
        '''全部清除鍵按下後的處理方法'''
        pass
        
    def clearMemory(self):
        '''清除記憶體鍵按下後的處理方法'''
        pass
        
    def readMemory(self):
        '''讀取記憶體鍵按下後的處理方法'''
        pass
        
    def setMemory(self):
        '''設定記憶體鍵按下後的處理方法'''
        pass
        
    def addToMemory(self):
        '''放到記憶體鍵按下後的處理方法'''
        pass
        
    def createButton(self):
        ''' 建立按鍵處理方法, 以 Qt Designer 建立對話框時, 不需要此方法'''
        pass
        
    def abortOperation(self):
        '''中斷運算'''
        pass
        
    def calculate(self):
        '''計算'''
        pass
