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
        self.firstSide = LineEdit()
        self.secondSide = LineEdit()
        self.thirdSide = LineEdit()
        self.calculateButton = PushButton()
        self.resultLabel = BodyLabel()
        self.showSolution = PushButton()
        self.solutionLabel = TextEdit()
        self.solutionArr = list()
        self.customFont = self.titleLabel.font()
        self.customFont.setWeight(60)
        self.customFont.setPointSize(20)

        self.titleLabel.setText("Найти объем параллелепипеда")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFont(self.customFont)

        self.firstSide.setPlaceholderText("Сторона a")
        self.secondSide.setPlaceholderText("Сторона b")
        self.thirdSide.setPlaceholderText("Сторона c")

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
        self.vSquareLayout.addWidget(self.firstSide, 1)
        self.vSquareLayout.addWidget(self.secondSide, 1)
        self.vSquareLayout.addWidget(self.thirdSide, 1)
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
            a = float(self.firstSide.text())
            b = float(self.secondSide.text())
            c = float(self.thirdSide.text())
        except:
            self.errorLabel.setText("Поля должны содержать только числа!")
            self.errorLabel.setHidden(False)
            return

        volume = a * b * c
        self.solutionArr += [a, b, c, volume]

        self.resultLabel.setText(f"Результат: {volume}")
        self.showSolution.setHidden(False)


    def validate(self):
        first = self.firstSide.text()
        second = self.secondSide.text()
        third = self.thirdSide.text()

        if not (first and second and third):
            return 0

        return 2

    def solution(self):
        self.solutionLabel.setHidden(not self.solutionLabel.isHidden())

        if self.solutionLabel.isHidden():
            return

        arr = self.solutionArr

        text = f'''Формула для объема параллелепипеда:
        • V = a ⋅ b ⋅ c = {arr[0]} ⋅ {arr[1]} ⋅ {arr[2]} = {arr[3]}
        '''
        self.solutionLabel.setText(text)


class FullSquare(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.vSquareLayout = QVBoxLayout(self)
        self.titleLabel = BodyLabel()
        self.firstSide = LineEdit()
        self.secondSide = LineEdit()
        self.thirdSide = LineEdit()
        self.calculateButton = PushButton()
        self.resultLabel = BodyLabel()
        self.showSolution = PushButton()
        self.solutionLabel = TextEdit()
        self.solutionArr = list()
        self.customFont = self.titleLabel.font()
        self.customFont.setWeight(60)
        self.customFont.setPointSize(20)

        self.titleLabel.setText("Найти площадь полной поверхности параллелепипеда")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFont(self.customFont)

        self.firstSide.setPlaceholderText("Сторона a")
        self.secondSide.setPlaceholderText("Сторона b")
        self.thirdSide.setPlaceholderText("Сторона c")

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
        self.vSquareLayout.addWidget(self.firstSide, 1)
        self.vSquareLayout.addWidget(self.secondSide, 1)
        self.vSquareLayout.addWidget(self.thirdSide, 1)
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
        volume = 0

        try:
            a = float(self.firstSide.text())
            b = float(self.secondSide.text())
            c = float(self.thirdSide.text())
        except:
            self.errorLabel.setText("Поля должны содержать только числа!")
            self.errorLabel.setHidden(False)
            return

        square = a * b * 2 + b * c * 2 + a * c * 2
        self.solutionArr += [a, b, c, square]

        self.resultLabel.setText(f"Результат: {square}")
        self.showSolution.setHidden(False)


    def validate(self):
        first = self.firstSide.text()
        second = self.secondSide.text()
        third = self.thirdSide.text()

        if not (first and second and third):
            return 0

        return 2

    def solution(self):
        self.solutionLabel.setHidden(not self.solutionLabel.isHidden())

        if self.solutionLabel.isHidden():
            return

        arr = self.solutionArr

        text = f'''Формула для площади полной поверхности параллелепипеда:
        • S = 2 ⋅ (a ⋅ b + b ⋅ c + c ⋅ a) = 2 ⋅ ({arr[0]} ⋅ {arr[1]} + {arr[1]} ⋅ {arr[2]} + {arr[2]} ⋅ {arr[0]}) = {arr[3]}
        '''
        self.solutionLabel.setText(text)


class SideSquare(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.vSquareLayout = QVBoxLayout(self)
        self.titleLabel = BodyLabel()
        self.firstSide = LineEdit()
        self.secondSide = LineEdit()
        self.thirdSide = LineEdit()
        self.calculateButton = PushButton()
        self.resultLabel = BodyLabel()
        self.showSolution = PushButton()
        self.solutionLabel = TextEdit()
        self.solutionArr = list()
        self.customFont = self.titleLabel.font()
        self.customFont.setWeight(60)
        self.customFont.setPointSize(20)

        self.titleLabel.setText("Найти площадь боковой поверхности параллелепипеда")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFont(self.customFont)

        self.firstSide.setPlaceholderText("Сторона a")
        self.secondSide.setPlaceholderText("Сторона b")
        self.thirdSide.setPlaceholderText("Сторона c")

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
        self.vSquareLayout.addWidget(self.firstSide, 1)
        self.vSquareLayout.addWidget(self.secondSide, 1)
        self.vSquareLayout.addWidget(self.thirdSide, 1)
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
        volume = 0

        try:
            a = float(self.firstSide.text())
            b = float(self.secondSide.text())
            c = float(self.thirdSide.text())
        except:
            self.errorLabel.setText("Поля должны содержать только числа!")
            self.errorLabel.setHidden(False)
            return

        square = b * c * 2 + a * c * 2
        self.solutionArr += [a, b, c, square]

        self.resultLabel.setText(f"Результат: {square}")
        self.showSolution.setHidden(False)


    def validate(self):
        first = self.firstSide.text()
        second = self.secondSide.text()
        third = self.thirdSide.text()

        if not (first and second and third):
            return 0

        return 2

    def solution(self):
        self.solutionLabel.setHidden(not self.solutionLabel.isHidden())

        if self.solutionLabel.isHidden():
            return

        arr = self.solutionArr

        text = f'''Формула для площади боковой поверхности параллелепипеда:
        • S = 2 ⋅ (b ⋅ c + c ⋅ a) = 2 ⋅ ({arr[1]} ⋅ {arr[2]} + {arr[2]} ⋅ {arr[0]}) = {arr[3]}
        '''
        self.solutionLabel.setText(text)