from PyQt5.QtCore import Qt, QMetaObject, QCoreApplication
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QSizePolicy, QStackedWidget, QFrame
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import Pivot

from tabs.widgets.TriangleWidgets import Square as TSquare, Perimeter as TPerimeter
from tabs.widgets.QuadrilateralWidgets import Square as QSquare, Perimeter as QPerimeter


class Pivit2D(QFrame):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.pivot = Pivot(self)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        self.pivot = Pivot(self)
        self.stackedWidget = QStackedWidget(self)
        self.vBoxLayout = QVBoxLayout(self)

        if text == 'triangleInterface':
            self.squareInterface = TSquare("triangleSquareInterface")
            self.perimeterInterface = TPerimeter("trianglePerimeterInterface")
        elif text == 'quadrilateralInterface':
            self.squareInterface = QSquare("quadrilateralSquareInterface")
            self.perimeterInterface = QPerimeter("quadrilateralPerimeterInterface")


        self.addSubInterface(self.squareInterface, 'squareInterface', 'Площадь')
        self.addSubInterface(self.perimeterInterface, 'perimeterInterface', 'Периметр')


        self.vBoxLayout.addWidget(self.pivot, 0, Qt.AlignHCenter)
        self.vBoxLayout.addWidget(self.stackedWidget)
        self.vBoxLayout.setContentsMargins(30, 0, 30, 30)

        self.stackedWidget.setCurrentWidget(self.squareInterface)
        self.pivot.setCurrentItem(self.squareInterface.objectName())
        self.pivot.currentItemChanged.connect(
            lambda k: self.stackedWidget.setCurrentWidget(self.findChild(QWidget, k)))

        self.setObjectName(text.replace(' ', '-'))
        print(f'[objectInfo] {self.objectName()} was loaded!')

    def addSubInterface(self, widget: QWidget, objectName, text):
        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)
        self.pivot.addItem(routeKey=objectName, text=text)