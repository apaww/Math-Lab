import math
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from qfluentwidgets import ComboBox, BodyLabel, LineEdit, PushButton, TextEdit, CaptionLabel

class Volume(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.vSquareLayout = QVBoxLayout(self)
        self.titleLabel = BodyLabel()
        self.radius = LineEdit()
        self.height = LineEdit()
        self.calculateButton = PushButton()
        self.resultLabel = BodyLabel()
        self.showSolution = PushButton()
        self.solutionLabel = TextEdit()
        self.solutionArr = list()
        self.customFont = self.titleLabel.font()
        self.customFont.setWeight(60)
        self.customFont.setPointSize(20)

        self.titleLabel.setText("Найти объем цилиндра")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFont(self.customFont)

        self.radius.setPlaceholderText("Радиус")
        self.height.setPlaceholderText("Высота")

        self.calculateButton.setText("Вычислить")
        self.calculateButton.clicked.connect(self.calculateVolume)

        self.resultLabel.setText("Результат: ")
        self.resultLabel.setFont(self.customFont)

        self.showSolution.setText("Показать решение")
        self.showSolution.setHidden(True)
        self.showSolution.clicked.connect(self.solution)

        self.errorLabel = CaptionLabel("Нужно заполнить все поля!")
        self.errorLabel.setTextColor("#cf1010", QColor(255, 28, 32))
        self.errorLabel.setHidden(True)

        self.solutionLabel.setHidden(True)

        self.vSquareLayout.addWidget(self.titleLabel, 3)
        self.vSquareLayout.addWidget(self.radius, 1)
        self.vSquareLayout.addWidget(self.height, 1)
        self.vSquareLayout.addWidget(self.errorLabel, 1)
        self.vSquareLayout.addWidget(self.calculateButton, 1)
        self.vSquareLayout.addWidget(self.resultLabel, 2)
        self.vSquareLayout.addWidget(self.showSolution, 1)
        self.vSquareLayout.addWidget(self.solutionLabel, 10)
        self.vSquareLayout.setContentsMargins(100, 0, 100, 200)

        self.setObjectName(text.replace(' ', '-'))
        print(f'[objectInfo] {self.objectName()} was loaded!')


    def calculateVolume(self):
        check = self.validate()
        self.solutionLabel.setHidden(True)
        self.showSolution.setHidden(True)

        if check == 0:
            self.errorLabel.setText("Нужно заполнить все поля!")
            self.errorLabel.setHidden(False)
            return

        self.errorLabel.setHidden(True)
        self.solutionArr = list()
        volume = 0

        try:
            r = float(self.radius.text())
            h = float(self.height.text())
        except:
            self.errorLabel.setText("Поля должны содержать только числа!")
            self.errorLabel.setHidden(False)
            return

        volume = h * r * r * math.pi
        self.solutionArr += [h, r, volume]

        self.resultLabel.setText(f"Результат: {volume}")
        self.showSolution.setHidden(False)


    def validate(self):
        radius = self.radius.text()
        heightText = self.height.text()

        if not (radius and heightText):
            return 0

        return 2

    def solution(self):
        self.solutionLabel.setHidden(not self.solutionLabel.isHidden())

        if self.solutionLabel.isHidden():
            return

        arr = self.solutionArr

        text = f'''Формула для объема цилиндра:
        • V = h ⋅ r² ⋅ π = {arr[0]} ⋅ {arr[1]}² ⋅ {math.pi} = {arr[2]}
        '''
        self.solutionLabel.setText(text)


class FullSquare(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.vSquareLayout = QVBoxLayout(self)
        self.titleLabel = BodyLabel()
        self.radius = LineEdit()
        self.height = LineEdit()
        self.calculateButton = PushButton()
        self.resultLabel = BodyLabel()
        self.showSolution = PushButton()
        self.solutionLabel = TextEdit()
        self.solutionArr = list()
        self.customFont = self.titleLabel.font()
        self.customFont.setWeight(60)
        self.customFont.setPointSize(20)

        self.titleLabel.setText("Найти площадь полной поверхности цилиндра")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFont(self.customFont)

        self.radius.setPlaceholderText("Радиус")
        self.height.setPlaceholderText("Высота")

        self.calculateButton.setText("Вычислить")
        self.calculateButton.clicked.connect(self.calculateSquare)

        self.resultLabel.setText("Результат: ")
        self.resultLabel.setFont(self.customFont)

        self.showSolution.setText("Показать решение")
        self.showSolution.setHidden(True)
        self.showSolution.clicked.connect(self.solution)

        self.errorLabel = CaptionLabel("Нужно заполнить все поля!")
        self.errorLabel.setTextColor("#cf1010", QColor(255, 28, 32))
        self.errorLabel.setHidden(True)

        self.solutionLabel.setHidden(True)

        self.vSquareLayout.addWidget(self.titleLabel, 3)
        self.vSquareLayout.addWidget(self.radius, 1)
        self.vSquareLayout.addWidget(self.height, 1)
        self.vSquareLayout.addWidget(self.errorLabel, 1)
        self.vSquareLayout.addWidget(self.calculateButton, 1)
        self.vSquareLayout.addWidget(self.resultLabel, 2)
        self.vSquareLayout.addWidget(self.showSolution, 1)
        self.vSquareLayout.addWidget(self.solutionLabel, 10)
        self.vSquareLayout.setContentsMargins(100, 0, 100, 200)

        self.setObjectName(text.replace(' ', '-'))
        print(f'[objectInfo] {self.objectName()} was loaded!')


    def calculateSquare(self):
        check = self.validate()
        self.solutionLabel.setHidden(True)
        self.showSolution.setHidden(True)

        if check == 0:
            self.errorLabel.setText("Нужно заполнить все поля!")
            self.errorLabel.setHidden(False)
            return

        self.errorLabel.setHidden(True)
        self.solutionArr = list()
        square = 0

        try:
            r = float(self.radius.text())
            h = float(self.height.text())
        except:
            self.errorLabel.setText("Поля должны содержать только числа!")
            self.errorLabel.setHidden(False)
            return

        square = 2 * math.pi * r * (h + r)
        self.solutionArr += [h, r, square]

        self.resultLabel.setText(f"Результат: {square}")
        self.showSolution.setHidden(False)


    def validate(self):
        radius = self.radius.text()
        heightText = self.height.text()

        if not (radius and heightText):
            return 0

        return 2

    def solution(self):
        self.solutionLabel.setHidden(not self.solutionLabel.isHidden())

        if self.solutionLabel.isHidden():
            return

        arr = self.solutionArr

        text = f'''Формула для площади полной поверхности цилиндра:
        • S = 2 ⋅ π ⋅ r ⋅ (h + r) = 2 ⋅ {math.pi} ⋅ {arr[1]} ⋅ ({arr[0]} + {arr[1]}) = {arr[2]}
        '''
        self.solutionLabel.setText(text)


class SideSquare(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.vSquareLayout = QVBoxLayout(self)
        self.titleLabel = BodyLabel()
        self.radius = LineEdit()
        self.height = LineEdit()
        self.calculateButton = PushButton()
        self.resultLabel = BodyLabel()
        self.showSolution = PushButton()
        self.solutionLabel = TextEdit()
        self.solutionArr = list()
        self.customFont = self.titleLabel.font()
        self.customFont.setWeight(60)
        self.customFont.setPointSize(20)

        self.titleLabel.setText("Найти площадь боковой поверхности цилиндра")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFont(self.customFont)

        self.radius.setPlaceholderText("Радиус")
        self.height.setPlaceholderText("Высота")

        self.calculateButton.setText("Вычислить")
        self.calculateButton.clicked.connect(self.calculateSquare)

        self.resultLabel.setText("Результат: ")
        self.resultLabel.setFont(self.customFont)

        self.showSolution.setText("Показать решение")
        self.showSolution.setHidden(True)
        self.showSolution.clicked.connect(self.solution)

        self.errorLabel = CaptionLabel("Нужно заполнить все поля!")
        self.errorLabel.setTextColor("#cf1010", QColor(255, 28, 32))
        self.errorLabel.setHidden(True)

        self.solutionLabel.setHidden(True)

        self.vSquareLayout.addWidget(self.titleLabel, 3)
        self.vSquareLayout.addWidget(self.radius, 1)
        self.vSquareLayout.addWidget(self.height, 1)
        self.vSquareLayout.addWidget(self.errorLabel, 1)
        self.vSquareLayout.addWidget(self.calculateButton, 1)
        self.vSquareLayout.addWidget(self.resultLabel, 2)
        self.vSquareLayout.addWidget(self.showSolution, 1)
        self.vSquareLayout.addWidget(self.solutionLabel, 10)
        self.vSquareLayout.setContentsMargins(100, 0, 100, 200)

        self.setObjectName(text.replace(' ', '-'))
        print(f'[objectInfo] {self.objectName()} was loaded!')


    def calculateSquare(self):
        check = self.validate()
        self.solutionLabel.setHidden(True)
        self.showSolution.setHidden(True)

        if check == 0:
            self.errorLabel.setText("Нужно заполнить все поля!")
            self.errorLabel.setHidden(False)
            return

        self.errorLabel.setHidden(True)
        self.solutionArr = list()
        square = 0

        try:
            r = float(self.radius.text())
            h = float(self.height.text())
        except:
            self.errorLabel.setText("Поля должны содержать только числа!")
            self.errorLabel.setHidden(False)
            return

        square = 2 * math.pi * r * h
        self.solutionArr += [h, r, square]

        self.resultLabel.setText(f"Результат: {square}")
        self.showSolution.setHidden(False)


    def validate(self):
        radius = self.radius.text()
        heightText = self.height.text()

        if not (radius and heightText):
            return 0

        return 2

    def solution(self):
        self.solutionLabel.setHidden(not self.solutionLabel.isHidden())

        if self.solutionLabel.isHidden():
            return

        arr = self.solutionArr

        text = f'''Формула для площади боковой поверхности цилиндра:
        • S = 2 ⋅ π ⋅ r ⋅ h = 2 ⋅ {math.pi} ⋅ {arr[1]} ⋅ {arr[0]} = {arr[2]}
        '''
        self.solutionLabel.setText(text)