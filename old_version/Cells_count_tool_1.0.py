# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 11:45:11 2021

@author: ar3134ba
"""

import sys
from PyQt5.QtWidgets import QApplication, QInputDialog, QFileDialog,QGridLayout, QWidget, QPushButton, QDialog, QVBoxLayout, QLabel, QSlider, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt
import cv2
import os

class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title='Cells count tool'
        self.left=10
        self.top=10
        width=300 #300
        height=400 #400
        self.setFixedSize(width, height)
        self.initUI()
        
       
    def initUI(self):
        
        self.setWindowTitle(self.title)
        layout = QVBoxLayout()
        #self.setGeometry(self.left,self.top,self.width,self.height)
        
        label=QLabel()
        pixmap = QPixmap('lund_logo.png')
        pixmap = pixmap.scaled(250,250)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)

        # self.grid = QGridLayout()
        # self.grid.addWidget(self.label,1,2)
        # self.setGeometry(50,50,320,200)
        # self.setLayout(self.grid)
        
        # mainMenu=self.menuBar()
        # fileMenu=mainMenu.addMenu('File')
        # editMenu=mainMenu.addMenu('Edit')
        # helpMenu=mainMenu.addMenu('Help')
        
        
        label2 = QLabel('Welcome on the cells counts tool !',self)
        label2.setFont(QFont('Arial', 13))
        label2.setAlignment(Qt.AlignCenter)

        # label2.move(100,100)
        
        button=QPushButton('Load a JPG file',self)
        button.clicked.connect(self.openFileNameDialog)
        button.setToolTip('.jpg')
        button.setFont(QFont('Arial', 13))
        # button.move(180,180)
        
        button2=QPushButton('Load multiple files',self)
        #button2.clicked.connect(self.for_n_file())
        button2.setToolTip('JPG file')
        button2.setFont(QFont('Arial', 13))
        # button2.move(180,180)
        
        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addWidget(button, alignment=Qt.AlignCenter)
        layout.addWidget(button2, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)
        self.show()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        global filename

        filename, _ = QFileDialog.getOpenFileName(self,"File Explorer", "","All Files (*);;Python Files (*.py)", options=options)
        if filename:
            print(filename)
        
        global nbr_cells
        global name_picture
        threshold = 20
        lst=Cells_counts.cells_counts(filename, threshold)
        name_picture = lst[0]
        nbr_cells = lst[1]
        
        self.next=Second_Windows()
    
    def for_n_file(self):
        next
        # filter = "JPG (*.jpg);;PNG (*.png)"
        # file_name = QFileDialog()
        # file_name.setFileMode(QFileDialog.ExistingFiles)
        # names = file_name.getOpenFileNameAndFilter(self, "Open files", "C\\Desktop", filter)
        # print(names)
        
    
class Second_Windows(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title='Cells counts tool - Result'
        self.left=10
        self.top=10
        self.width=800
        self.height=240
        self.initUI()
        
    def display(self):
        integer , pressed = QInputDialog.getInt(self, "Threshold value","Number:",
                                            20, 0, 255, 1)
        if pressed:
            self.valuechange(integer)
         
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        layout = QVBoxLayout()
        
        self.label1=QLabel("Picture : "+ str(name_picture), self)
        self.label1.setAlignment(Qt.AlignLeft)
        #self.label1.move(50,50)
        
        self.label2=QLabel("Save directory : "+ str(os.getcwd()+'\\Results_pictures'), self)
        self.label2.setAlignment(Qt.AlignLeft)
        # self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        # self.label2.move(50,100)
        
        self.label3=QLabel("Number of cells found : "+ str(nbr_cells), self)
        # self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label3.setAlignment(Qt.AlignLeft)
        # self.label3.move(50,140)
        
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        
        self.label4 = QLabel('Threshold = 20', self)
        self.label4.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label4.setMinimumWidth(80)
        layout.addWidget(self.label4)
        
        self.label5 = QPushButton(self)
        self.label5.move(60,120)
        self.label5.setText('Update threshold')
        self.label5.clicked.connect(self.display)
        layout.addWidget(self.label5)
        
        # self.sl = QSlider(Qt.Horizontal)
        # self.sl.setMinimum(0)
        # self.sl.setMaximum(255)
        # self.sl.setValue(20)
        # self.sl.setTickPosition(QSlider.TicksBelow)
        # self.sl.setTickInterval(20)
        # layout.addWidget(self.sl)

        # self.sl.valueChanged.connect(self.valuechange)
        
        self.setLayout(layout)
        self.show()
        
    def valuechange(self, threshold_select):
        # threshold_select = self.sl.value()
        self.label4.setText('Threshold = ' +str(threshold_select))
        threshold = threshold_select
        result = Cells_counts.cells_counts(filename, threshold)
        self.label1.setText("Picture : "+ str(result[0]))
        self.label3.setText("Number of cells found : "+ str(result[1]))
        
class Cells_counts():
    
    @staticmethod
    def cells_counts(file, threshold):
        print('coucou')
    
        '''This function create a gray picture with the jpg file. 
            Then, with the cv2 library we can count the cells '''
            
        # Read image
        img = cv2.imread(file)
        
        # Convert image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #NEW 2021-08-16 Threshold
        thresholdValue = threshold
        maxValPixel = 255
        ret, thresh2 = cv2.threshold(gray, thresholdValue, maxValPixel, cv2.THRESH_BINARY)
        
        # cv2.imshow('Binary Threshold Inverted', thresh2)
        
        # Size of the picture
        width,height,dimension = img.shape
          # half of the original image
        required_width, required_height = width // 2, height // 2
            # resizing of an image is done
        resize_img_1 = cv2.resize(gray,(required_height, required_width))
        
        # Show grayscale image
        #cv2.imshow('gray image', resize_img)
        cv2.waitKey(0)
        
        #detection of the edges
        # edged = cv2.Canny(gray, 0, 30)
        
        # Find contours
        contours, h = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        # Size of the picture
        width,height,dimension = img.shape
          # half of the original image
        required_width, required_height = width // 2, height // 2
            # resizing of an image is done
        resize_img_2 = cv2.resize(thresh2,(required_height, required_width))
        
        # Show edge imqge
        cv2.imshow('Original picture', resize_img_1)
        cv2.imshow('Python contours', resize_img_2)
        
        #Location for save the data
        parent_dir = os.getcwd()
        directory = 'Results_pictures'
        path = os.path.join(parent_dir, directory)
        
        if os.path.isdir(path):
            next
        else : 
            os.mkdir(path)  #New directory for results
            
        os.chdir(path)
        filename = file.split('/')
        filename_threshold = filename[len(filename)-1][:-4] + '_THRESHOLD_python.jpg'
        filename = filename[len(filename)-1][:-4] + '_python.jpg'

        #Save the python picture
        cv2.imwrite(filename,resize_img_2)
        cv2.imwrite(filename_threshold,thresh2)
        cv2.waitKey(0)
        os.chdir(parent_dir)
        
        nbr_cells =len(contours)
        print(" ")
        print("Picture :", file)
        print('Number of cells found :', nbr_cells)  
        print(" ")
        
        return filename, nbr_cells
        #cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
        #cv2.imshow('Contours', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())



















