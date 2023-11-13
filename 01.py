import sys
import io
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

ui_file = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>597</width>
    <height>488</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="PlotWidget" name="PlotWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>581</width>
      <height>381</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="X_label">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>410</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>410</y>
      <width>21</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>y=</string>
    </property>
   </widget>
   <widget class="QPushButton" name="CreateButton">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>410</y>
      <width>161</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Постройить</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>410</y>
      <width>21</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>x [</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>410</y>
      <width>31</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>410</y>
      <width>16</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>;</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_2">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>410</y>
      <width>31</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>410</y>
      <width>16</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>]</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>597</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <customwidgets>
  <customwidget>
   <class>PlotWidget</class>
   <extends>QGraphicsView</extends>
   <header>pyqtgraph</header>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>
"""


class Grapth(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(ui_file)
        uic.loadUi(f, self)
        self.setWindowTitle('График')
        self.CreateButton.clicked.connect(self.create_plot)

    def create_plot(self):
        y = self.X_label.text()
        if len(y) > 0 and len(self.lineEdit.text()) > 0 and len(self.lineEdit_2.text()) > 0:
            if '/' in y:
                self.PlotWidget.clear()
                coords_y = []
                coords_x = []
                for i in range(int(self.lineEdit.text()), int(self.lineEdit_2.text()) + 1):
                    if i != 0:
                        coords_x.append(i)
                        c = eval(y.replace('x', str(i)))
                        coords_y.append(c)
                    else:
                        self.PlotWidget.plot(coords_x, coords_y, pen='r')
                        coords_y = []
                        coords_x = []
                self.PlotWidget.plot(coords_x, coords_y, pen='r')
            else:
                self.PlotWidget.clear()
                coords_y = []
                for i in range(int(self.lineEdit.text()), int(self.lineEdit_2.text()) + 1):
                    c = eval(y.replace('x', str(i)))
                    coords_y.append(c)
                self.PlotWidget.plot([i for i in range(int(self.lineEdit.text()), int(self.lineEdit_2.text()) + 1)],
                                     coords_y, pen='b')

def f1():
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Grapth()
    ex.show()
    sys.exit(app.exec_())
