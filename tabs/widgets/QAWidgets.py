import math
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from qfluentwidgets import ComboBox, BodyLabel, LineEdit, PushButton, TextEdit, CaptionLabel

class Triangle(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.vSquareLayout = QVBoxLayout(self)
        self.volumeLabel = BodyLabel()
        self.volumeInfoLabel = BodyLabel()
        self.areaLabel = BodyLabel()
        self.areaInfoLabel = BodyLabel()
        self.titleFont = self.volumeLabel.font()
        self.titleFont.setWeight(60)
        self.titleFont.setPointSize(20)
        self.infoFont = self.volumeInfoLabel.font()
        self.infoFont.setWeight(60)
        self.infoFont.setPointSize(14)

        self.volumeLabel.setText("Как найти площадь треугольника?")
        self.volumeLabel.setAlignment(Qt.AlignCenter)
        self.volumeLabel.setFont(self.titleFont)

        self.volumeInfoLabel.setText('''
        1. Площадь треугольника через основание и высоту.
            S=0,5⋅a⋅h, где a — основание, h — высота.
        2. Площадь прямоугольного треугольника через две стороны.
            S=0,5⋅a⋅b, где a, b — стороны.
        3. Формула Герона для вычисления площади треугольника
            Сначала необходимо подсчитать разность полупериметра и каждой его стороны. 
             Потом найти произведение полученных чисел, умножить результат на полупериметр 
             и найти корень из полученного числа.
            S=√(p ⋅ (p − a) ⋅ (p − b) ⋅ (p − c)), где a, b, c — стороны, p — полупериметр, 
             который можно найти по формуле: p=(a+b+c)÷2p=(a+b+c)÷2 
            
        Источник - Онлайн школа Skysmart: https://skysmart.ru/articles/mathematic/ploshad-treugolnika
        ''')
        self.volumeInfoLabel.setAlignment(Qt.AlignLeft)
        self.volumeInfoLabel.setFont(self.infoFont)

        self.areaLabel.setText("Как найти периметр треугольника?")
        self.areaLabel.setAlignment(Qt.AlignCenter)
        self.areaLabel.setFont(self.titleFont)

        self.areaInfoLabel.setText('''
            P=a+b+c, где a, b, c — стороны.
                ''')
        self.areaInfoLabel.setAlignment(Qt.AlignLeft)
        self.areaInfoLabel.setFont(self.infoFont)

        self.vSquareLayout.addWidget(self.volumeLabel, 1)
        self.vSquareLayout.addWidget(self.volumeInfoLabel, 20)
        self.vSquareLayout.addWidget(self.areaLabel, 1)
        self.vSquareLayout.addWidget(self.areaInfoLabel, 20)
        self.vSquareLayout.setContentsMargins(100, 0, 100, 200)

        self.setObjectName(text.replace(' ', '-'))
        print(f'[objectInfo] {self.objectName()} was loaded!')


class Quadrilateral(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.vSquareLayout = QVBoxLayout(self)
        self.volumeLabel = BodyLabel()
        self.volumeInfoLabel = BodyLabel()
        self.areaLabel = BodyLabel()
        self.areaInfoLabel = BodyLabel()
        self.titleFont = self.volumeLabel.font()
        self.titleFont.setWeight(60)
        self.titleFont.setPointSize(20)
        self.infoFont = self.volumeInfoLabel.font()
        self.infoFont.setWeight(60)
        self.infoFont.setPointSize(14)

        self.volumeLabel.setText("Как найти площадь четырехугольника?")
        self.volumeLabel.setAlignment(Qt.AlignCenter)
        self.volumeLabel.setFont(self.titleFont)

        self.volumeInfoLabel.setText('''
        1. Площадь параллелограма по двум сторонам и углу между ними.
            S=a⋅b⋅sin α, где a, b — стороны, α — угол между ними.
        2. Площадь параллелограма по высоте и стороне, на которую она падает.
            S=a⋅h, где  h — высота, a — сторона, на которую она падает.
        3. Площадь прямоугольника.
            S=a⋅b, где a, b — стороны.
        4. Площадь квадрата.
            S=a⋅a, где a — сторона.
        5. Площадь ромба.
            S=a⋅b/2, где a, b — диагонали.
        6. Площадь трапеции.
            S=a+b/2⋅h, где a, b — основания, h — высота.
        ''')
        self.volumeInfoLabel.setAlignment(Qt.AlignLeft)
        self.volumeInfoLabel.setFont(self.infoFont)

        self.areaLabel.setText("Как найти периметр четырехугольника?")
        self.areaLabel.setAlignment(Qt.AlignCenter)
        self.areaLabel.setFont(self.titleFont)

        self.areaInfoLabel.setText('''
            P=a+b+c+d, где a, b, c, d — стороны.
                ''')
        self.areaInfoLabel.setAlignment(Qt.AlignLeft)
        self.areaInfoLabel.setFont(self.infoFont)

        self.vSquareLayout.addWidget(self.volumeLabel, 1)
        self.vSquareLayout.addWidget(self.volumeInfoLabel, 20)
        self.vSquareLayout.addWidget(self.areaLabel, 1)
        self.vSquareLayout.addWidget(self.areaInfoLabel, 20)
        self.vSquareLayout.setContentsMargins(100, 0, 100, 200)

        self.setObjectName(text.replace(' ', '-'))
        print(f'[objectInfo] {self.objectName()} was loaded!')


class Cylinder(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.vSquareLayout = QVBoxLayout(self)
        self.volumeLabel = BodyLabel()
        self.volumeInfoLabel = BodyLabel()
        self.areaFullLabel = BodyLabel()
        self.areaInfoFullLabel = BodyLabel()
        self.areaLabel = BodyLabel()
        self.areaInfoLabel = BodyLabel()
        self.titleFont = self.volumeLabel.font()
        self.titleFont.setWeight(60)
        self.titleFont.setPointSize(20)
        self.infoFont = self.volumeInfoLabel.font()
        self.infoFont.setWeight(60)
        self.infoFont.setPointSize(14)

        self.volumeLabel.setText("Как найти объем цилиндра?")
        self.volumeLabel.setAlignment(Qt.AlignCenter)
        self.volumeLabel.setFont(self.titleFont)

        self.volumeInfoLabel.setText('''
            V=h⋅r²⋅π, где r — радиус основания, h — высота.
        ''')
        self.volumeInfoLabel.setAlignment(Qt.AlignLeft)
        self.volumeInfoLabel.setFont(self.infoFont)

        self.areaFullLabel.setText("Как найти площадь полной поверхности цилиндра?")
        self.areaFullLabel.setAlignment(Qt.AlignCenter)
        self.areaFullLabel.setFont(self.titleFont)

        self.areaInfoFullLabel.setText('''
            S=2⋅π⋅r⋅(h+r), где r — радиус основания, h — высота.
                ''')
        self.areaInfoFullLabel.setAlignment(Qt.AlignLeft)
        self.areaInfoFullLabel.setFont(self.infoFont)

        self.areaLabel.setText("Как найти площадь боковой поверхности цилиндра?")
        self.areaLabel.setAlignment(Qt.AlignCenter)
        self.areaLabel.setFont(self.titleFont)

        self.areaInfoLabel.setText('''
            S=2⋅π⋅r⋅h, где r — радиус основания, h — высота.
                ''')
        self.areaInfoLabel.setAlignment(Qt.AlignLeft)
        self.areaInfoLabel.setFont(self.infoFont)

        self.vSquareLayout.addWidget(self.volumeLabel, 1)
        self.vSquareLayout.addWidget(self.volumeInfoLabel, 20)
        self.vSquareLayout.addWidget(self.areaFullLabel, 1)
        self.vSquareLayout.addWidget(self.areaInfoFullLabel, 20)
        self.vSquareLayout.addWidget(self.areaLabel, 1)
        self.vSquareLayout.addWidget(self.areaInfoLabel, 20)
        self.vSquareLayout.setContentsMargins(100, 0, 100, 200)

        self.setObjectName(text.replace(' ', '-'))
        print(f'[objectInfo] {self.objectName()} was loaded!')


class Cone(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.vSquareLayout = QVBoxLayout(self)
        self.volumeLabel = BodyLabel()
        self.volumeInfoLabel = BodyLabel()
        self.areaFullLabel = BodyLabel()
        self.areaInfoFullLabel = BodyLabel()
        self.areaLabel = BodyLabel()
        self.areaInfoLabel = BodyLabel()
        self.titleFont = self.volumeLabel.font()
        self.titleFont.setWeight(60)
        self.titleFont.setPointSize(20)
        self.infoFont = self.volumeInfoLabel.font()
        self.infoFont.setWeight(60)
        self.infoFont.setPointSize(14)

        self.volumeLabel.setText("Как найти объем конуса?")
        self.volumeLabel.setAlignment(Qt.AlignCenter)
        self.volumeLabel.setFont(self.titleFont)

        self.volumeInfoLabel.setText('''
            V=π⋅r²⋅h/3, где r — радиус основания, h — высота.
        ''')
        self.volumeInfoLabel.setAlignment(Qt.AlignLeft)
        self.volumeInfoLabel.setFont(self.infoFont)

        self.areaFullLabel.setText("Как найти площадь полной поверхности конуса?")
        self.areaFullLabel.setAlignment(Qt.AlignCenter)
        self.areaFullLabel.setFont(self.titleFont)

        self.areaInfoFullLabel.setText('''
            S=π⋅r⋅(l+r), где r — радиус основания, l — образующая.
                ''')
        self.areaInfoFullLabel.setAlignment(Qt.AlignLeft)
        self.areaInfoFullLabel.setFont(self.infoFont)

        self.areaLabel.setText("Как найти площадь боковой поверхности конуса?")
        self.areaLabel.setAlignment(Qt.AlignCenter)
        self.areaLabel.setFont(self.titleFont)

        self.areaInfoLabel.setText('''
            S=π⋅r⋅l, где r — радиус основания, l — образующая.
                ''')
        self.areaInfoLabel.setAlignment(Qt.AlignLeft)
        self.areaInfoLabel.setFont(self.infoFont)

        self.vSquareLayout.addWidget(self.volumeLabel, 1)
        self.vSquareLayout.addWidget(self.volumeInfoLabel, 20)
        self.vSquareLayout.addWidget(self.areaFullLabel, 1)
        self.vSquareLayout.addWidget(self.areaInfoFullLabel, 20)
        self.vSquareLayout.addWidget(self.areaLabel, 1)
        self.vSquareLayout.addWidget(self.areaInfoLabel, 20)
        self.vSquareLayout.setContentsMargins(100, 0, 100, 200)

        self.setObjectName(text.replace(' ', '-'))
        print(f'[objectInfo] {self.objectName()} was loaded!')


class Parallelepiped(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.vSquareLayout = QVBoxLayout(self)
        self.volumeLabel = BodyLabel()
        self.volumeInfoLabel = BodyLabel()
        self.areaFullLabel = BodyLabel()
        self.areaInfoFullLabel = BodyLabel()
        self.areaLabel = BodyLabel()
        self.areaInfoLabel = BodyLabel()
        self.titleFont = self.volumeLabel.font()
        self.titleFont.setWeight(60)
        self.titleFont.setPointSize(20)
        self.infoFont = self.volumeInfoLabel.font()
        self.infoFont.setWeight(60)
        self.infoFont.setPointSize(14)

        self.volumeLabel.setText("Как найти объем параллелепипеда?")
        self.volumeLabel.setAlignment(Qt.AlignCenter)
        self.volumeLabel.setFont(self.titleFont)

        self.volumeInfoLabel.setText('''
           V=a⋅b⋅c, где a, b, c — стороны.
        ''')
        self.volumeInfoLabel.setAlignment(Qt.AlignLeft)
        self.volumeInfoLabel.setFont(self.infoFont)

        self.areaFullLabel.setText("Как найти площадь полной поверхности параллелепипеда?")
        self.areaFullLabel.setAlignment(Qt.AlignCenter)
        self.areaFullLabel.setFont(self.titleFont)

        self.areaInfoFullLabel.setText('''
            S=2⋅(a⋅b+b⋅c+c⋅a), где a, b, c — стороны.
                ''')
        self.areaInfoFullLabel.setAlignment(Qt.AlignLeft)
        self.areaInfoFullLabel.setFont(self.infoFont)

        self.areaLabel.setText("Как найти площадь боковой поверхности параллелепипеда?")
        self.areaLabel.setAlignment(Qt.AlignCenter)
        self.areaLabel.setFont(self.titleFont)

        self.areaInfoLabel.setText('''
            S=2⋅(b⋅c+c⋅a), где a, b, c — стороны.
                ''')
        self.areaInfoLabel.setAlignment(Qt.AlignLeft)
        self.areaInfoLabel.setFont(self.infoFont)

        self.vSquareLayout.addWidget(self.volumeLabel, 1)
        self.vSquareLayout.addWidget(self.volumeInfoLabel, 20)
        self.vSquareLayout.addWidget(self.areaFullLabel, 1)
        self.vSquareLayout.addWidget(self.areaInfoFullLabel, 20)
        self.vSquareLayout.addWidget(self.areaLabel, 1)
        self.vSquareLayout.addWidget(self.areaInfoLabel, 20)
        self.vSquareLayout.setContentsMargins(100, 0, 100, 200)

        self.setObjectName(text.replace(' ', '-'))
        print(f'[objectInfo] {self.objectName()} was loaded!')