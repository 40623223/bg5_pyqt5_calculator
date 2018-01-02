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
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        '''以下為使用者自行編寫程式碼區'''
        
        self.equalButton.clicked.connect(self.equalClicked)
        
        self.clearAllButton.clicked.connect(self.clearAll)
        
        self.clearButton.clicked.connect(self.clear)
        
        self.pendingAdditiveOperator = ''
        
        self.sumSoFar = 0
        
        self.waitingForOperand = True
        
        self.display.setText('0')\
       
        self.pendingMultiplicativeOperator = ''
        
        self.backspaceButton.clicked.connect(self.backspaceClicked)
        
        digits = [self.one,  self.two,  self.three, \
            self.four,  self.five,  self.six, \
            self.seven,  self.eight,  self.nine,  self.zero]

        for i in digits:
            i.clicked.connect(self.digitClicked)


        self.clearButton.clicked.connect(self.clear)
        
        self.waitingForOperand = True


        
        self.display.setText('0')\
        
        #unaryOperator = [self.squareRootButton, self.powerButton,  self.reciprocalButton]        

        additiveOperatorClicked = [self.plusButton,  self.minusButton]
        for i in additiveOperatorClicked:
            i.clicked.connect(self.additiveOperatorClicked)
        
        self.waitingForOperand = True
        
        multiply_divide = [self.timesButton,  self.divisionButton]
        for i in multiply_divide:
            i.clicked.connect(self.multiplicativeOperatorClicked)
        
    def digitClicked(self):
        '''
        使用者按下數字鍵, 必須能夠累積顯示該數字
        當顯示幕已經為 0, 再按零不會顯示 00, 而仍顯示 0 或 0.0
        
        '''
        #pass
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())
        if self.display.text() == '0' and digitValue == 0.0:
            return
        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False
            
        self.display.setText(self.display.text() + str(digitValue))
            
    def unaryOperatorClicked(self):
        '''單一運算元按下後處理方法'''
        pass
        
    def additiveOperatorClicked(self):
        '''加或減按下後進行的處理方法'''
        #pass
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())
        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return
 
            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''
            
        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return
            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand
            self.pendingAdditiveOperator = clickedOperator
            self.waitingForOperand = True
    def multiplicativeOperatorClicked(self):
        '''乘或除按下後進行的處理方法'''
        #pass
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())
        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return
                self.display.setText(str(self.factorSoFar))
        else:
            self.factorSoFar = operand
        self.pendingMultiplicativeOperator = clickedOperator
        self.waitingForOperand = True
       
        
    def equalClicked(self):
        '''等號按下後的處理方法'''
        #pass
        operand = float(self.display.text())
        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''
        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return
 
            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand
 
        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True    
    def pointClicked(self):
        '''小數點按下後的處理方法'''
        pass
        
    def changeSignClicked(self):
        '''變號鍵按下後的處理方法'''
        pass
        
    def backspaceClicked(self):
        '''回復鍵按下的處理方法'''
        #pass
        if self.waitingForOperand:
            return
        text = self.display.text()[:-1]
        if not text:
            text="0"
            self.waitingForOperand = True
         
        self.display.setText(text)   
        
    def clear(self):
        '''清除鍵按下後的處理方法'''
        #pass
        self.waitingForOperand = True
        self.display.setText('0')
    def clearAll(self):
        '''全部清除鍵按下後的處理方法'''
        #pass
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''
        self.display.setText('0')
        self.waitingForOperand = True
 
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
        #pass
        self.clearAll()
        self.display.setText("fuck")
    def calculate(self, rightOperand, pendingOperator):
        '''計算'''
        #pass
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand   
        elif pendingOperator == "*":
            self.factorSoFar *= rightOperand
        elif pendingOperator == "/":
            if rightOperand == 0.0:
                return False
            self.factorSoFar /= rightOperand
            
        return True
