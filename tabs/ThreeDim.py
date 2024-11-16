from PyQt5.QtCore import Qt, QMetaObject, QCoreApplication
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QSizePolicy, QStackedWidget, QFrame
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import Pivot

from tabs.widgets.CylinderWidgets import Volume as CyVolume, FullSquare as CyFull, SideSquare as CySide
from tabs.widgets.ConeWidgets import Volume as CoVolume, FullSquare as CoFull, SideSquare as CoSide
from tabs.widgets.ParallelepipedWidgets import Volume as PVolume, FullSquare as PFull, SideSquare as PSide


class Pivit3D(QFrame):
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

        if text == 'cylinderInterface':
            self.volumeInterface = CyVolume("cylinderVolumeInterface")
            self.fullSquareInterface = CyFull("cylinderFullSquareInterface")
            self.sideSquareInterface = CySide("cylinderSideSquareInterface")
        elif text == 'coneInterface':
            self.volumeInterface = CoVolume("coneVolumeInterface")
            self.fullSquareInterface = CoFull("coneFullSquareInterface")
            self.sideSquareInterface = CoSide("coneSideSquareInterface")
        elif text == 'parallelepipedInterface':
            self.volumeInterface = PVolume("parallelepipedVolumeInterface")
            self.fullSquareInterface = PFull("parallelepipedFullSquareInterface")
            self.sideSquareInterface = PSide("parallelepipedSideSquareInterface")


        self.addSubInterface(self.volumeInterface, 'volumeInterface', 'Объем')
        self.addSubInterface(self.fullSquareInterface, 'fullSquareInterface', 'Полная площадь')
        self.addSubInterface(self.sideSquareInterface, 'sideSquareInterface', 'Площадь боковой поверхности')


        self.vBoxLayout.addWidget(self.pivot, 0, Qt.AlignHCenter)
        self.vBoxLayout.addWidget(self.stackedWidget)
        self.vBoxLayout.setContentsMargins(30, 0, 30, 30)

        self.stackedWidget.setCurrentWidget(self.volumeInterface)
        self.pivot.setCurrentItem(self.volumeInterface.objectName())
        self.pivot.currentItemChanged.connect(
            lambda k: self.stackedWidget.setCurrentWidget(self.findChild(QWidget, k)))

        self.setObjectName(text.replace(' ', '-'))
        print(f'[objectInfo] {self.objectName()} was loaded!')

    def addSubInterface(self, widget: QWidget, objectName, text):
        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)
        self.pivot.addItem(routeKey=objectName, text=text)