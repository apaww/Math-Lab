import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from qfluentwidgets import FluentWindow, NavigationItemPosition
from qfluentwidgets import FluentIcon as FIF

from tabs.TwoDim import Pivit2D
from tabs.ThreeDim import Pivit3D
from tabs.QA import QA


class Window(FluentWindow):
    def __init__(self):
        super().__init__()

        self.triangle = Pivit2D('triangleInterface')
        self.quadrilateral = Pivit2D('quadrilateralInterface')
        self.cylinder = Pivit3D('cylinderInterface')
        self.cone = Pivit3D('coneInterface')
        self.parallelepiped = Pivit3D('parallelepipedInterface')
        self.qa = QA('QAInterface')

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.triangle, FIF.RIGHT_ARROW, 'Треугольник')
        self.addSubInterface(self.quadrilateral, FIF.RIGHT_ARROW, 'Четырехугольник')
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.cylinder, FIF.RIGHT_ARROW, 'Цилиндр')
        self.addSubInterface(self.cone, FIF.RIGHT_ARROW, 'Конус')
        self.addSubInterface(self.parallelepiped, FIF.RIGHT_ARROW, 'Параллелепипед')
        self.addSubInterface(self.qa, FIF.QUESTION, 'Справка', NavigationItemPosition.BOTTOM)

    def initWindow(self):
        self.resize(1400, 800)
        self.setWindowIcon(QIcon('./static/icon.png'))
        self.setWindowTitle('Math Lab')

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        self.navigationInterface.setMinimumExpandWidth(900)
        self.navigationInterface.expand(useAni=False)


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec())