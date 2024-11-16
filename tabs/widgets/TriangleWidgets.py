import math
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from qfluentwidgets import ComboBox, BodyLabel, LineEdit, PushButton, TextEdit, CaptionLabel

class Square(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.vSquareLayout = QVBoxLayout(self)
        self.titleLabel = BodyLabel()
        self.chooseMethod = ComboBox()
        self.firstSide = LineEdit()
        self.secondSide = LineEdit()
        self.thirdSide = LineEdit()
        self.height = LineEdit()
        self.calculateButton = PushButton()
        self.resultLabel = BodyLabel()
        self.showSolution = PushButton()
        self.solutionLabel = TextEdit()
        self.solutionArr = list()
        self.customFont = self.titleLabel.font()
        self.customFont.setWeight(60)
        self.customFont.setPointSize(20)

        self.titleLabel.setText("Найти площадь треугольника")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFont(self.customFont)

        self.chooseMethod.setPlaceholderText("Выберите способ нахождения")
        items = ['По трем сторонам', 'По стороне и высоте', 'Прямоугольный треугольник']
        self.chooseMethod.addItems(items)
        self.chooseMethod.setCurrentIndex(0)
        self.chooseMethod.currentTextChanged.connect(self.change)

        self.firstSide.setPlaceholderText("Сторона a")
        self.secondSide.setPlaceholderText("Сторона b")
        self.thirdSide.setPlaceholderText("Сторона c")
        self.height.setPlaceholderText("Высота")
        self.height.setHidden(True)

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
        self.vSquareLayout.addWidget(self.chooseMethod, 1)
        self.vSquareLayout.addWidget(self.firstSide, 1)
        self.vSquareLayout.addWidget(self.secondSide, 1)
        self.vSquareLayout.addWidget(self.thirdSide, 1)
        self.vSquareLayout.addWidget(self.height, 1)
        self.vSquareLayout.addWidget(self.errorLabel, 1)
        self.vSquareLayout.addWidget(self.calculateButton, 1)
        self.vSquareLayout.addWidget(self.resultLabel, 2)
        self.vSquareLayout.addWidget(self.showSolution, 1)
        self.vSquareLayout.addWidget(self.solutionLabel, 10)
        self.vSquareLayout.setContentsMargins(100, 0, 100, 200)

        self.setObjectName(text.replace(' ', '-'))
        print(f'[objectInfo] {self.objectName()} was loaded!')


    def change(self):
        curIndex = self.chooseMethod.currentIndex()
        if curIndex == 0:
            self.firstSide.setHidden(False)
            self.secondSide.setHidden(False)
            self.thirdSide.setHidden(False)
            self.height.setHidden(True)

            self.firstSide.setText("")
            self.secondSide.setText("")
            self.thirdSide.setText("")
            self.height.setText("")

            self.errorLabel.setHidden(True)
            self.showSolution.setHidden(True)
            self.solutionLabel.setHidden(True)
        elif curIndex == 1:
            self.firstSide.setHidden(False)
            self.secondSide.setHidden(True)
            self.thirdSide.setHidden(True)
            self.height.setHidden(False)

            self.firstSide.setText("")
            self.secondSide.setText("")
            self.thirdSide.setText("")
            self.height.setText("")

            self.errorLabel.setHidden(True)
            self.showSolution.setHidden(True)
            self.solutionLabel.setHidden(True)
        elif curIndex == 2:
            self.firstSide.setHidden(False)
            self.secondSide.setHidden(False)
            self.thirdSide.setHidden(True)
            self.height.setHidden(True)

            self.firstSide.setText("")
            self.secondSide.setText("")
            self.thirdSide.setText("")
            self.height.setText("")

            self.errorLabel.setHidden(True)
            self.showSolution.setHidden(True)
            self.solutionLabel.setHidden(True)


    def calculateSquare(self):
        curIndex = self.chooseMethod.currentIndex()
        check = self.validate(curIndex)
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
            if curIndex == 0:
                a = float(self.firstSide.text())
                b = float(self.secondSide.text())
                c = float(self.thirdSide.text())

                p = (a + b + c) / 2
                try:
                    square = math.sqrt(p * (p - a) * (p - b) * (p - c))
                except:
                    self.errorLabel.setText("Такого треугольника не существует!")
                    self.errorLabel.setHidden(False)
                    return

                self.solutionArr += [curIndex, a, b, c, p, square]
            elif curIndex == 1:
                a = float(self.firstSide.text())
                h = float(self.height.text())

                square = a * h / 2

                self.solutionArr += [curIndex, a, h, square]
            elif curIndex == 2:
                a = float(self.firstSide.text())
                b = float(self.secondSide.text())

                square = a * b / 2

                self.solutionArr += [curIndex, a, b, square]
        except:
            self.errorLabel.setText("Поля должны содержать только числа!")
            self.errorLabel.setHidden(False)
            return

        self.resultLabel.setText(f"Результат: {square}")
        self.showSolution.setHidden(False)


    def validate(self, curIndex):
        firstText = self.firstSide.text()
        secondText = self.secondSide.text()
        thirdText = self.thirdSide.text()
        heightText = self.height.text()

        if curIndex == 0 and not (firstText and secondText and thirdText):
            return 0
        elif curIndex == 1 and not(firstText and heightText):
            return 0
        elif curIndex == 2 and not(firstText and secondText):
            return 0

        return 2

    def solution(self):
        self.solutionLabel.setHidden(not self.solutionLabel.isHidden())

        if self.solutionLabel.isHidden():
            return

        arr = self.solutionArr

        if arr[0] == 0:
            text = f'''Формула Герона
            • Вычисляем полупериметр p: 
                    p = (a + b + c) / 2 = ({arr[1]} + {arr[2]} + {arr[3]}) / 2 = {arr[4]}
            • Считаем площадь треугольника по формуле: 
                    S = √(p ⋅ (p − a) ⋅ (p − b) ⋅ (p − c)) = √({arr[4]} ⋅ ({arr[4]} − {arr[1]}) ⋅ ({arr[4]} − {arr[2]}) ⋅ ({arr[4]} − {arr[3]})) = {arr[5]}
            '''
            self.solutionLabel.setText(text)
        elif arr[0] == 1:
            text = f'''Формула для площади треугольника через высоту и сторону, на которую она падает:
            • S = a ⋅ h / 2 = {arr[1]} ⋅ {arr[2]} / 2 = {arr[3]}
            '''
            self.solutionLabel.setText(text)
        elif arr[0] == 2:
            text = f'''Формула для площади прямоугольного треугольника:
            • S = a ⋅ b / 2 = {arr[1]} ⋅ {arr[2]} / 2 = {arr[3]}
            '''
            self.solutionLabel.setText(text)


class Perimeter(QWidget):
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

        self.titleLabel.setText("Найти периметр треугольника")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFont(self.customFont)

        self.firstSide.setPlaceholderText("Сторона a")
        self.secondSide.setPlaceholderText("Сторона b")
        self.thirdSide.setPlaceholderText("Сторона c")

        self.calculateButton.setText("Вычислить")
        self.calculateButton.clicked.connect(self.calculatePerimeter)

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


    def calculatePerimeter(self):
        check = self.validate()
        self.solutionLabel.setHidden(True)
        self.showSolution.setHidden(True)

        if check == 0:
            self.errorLabel.setText("Нужно заполнить все поля!")
            self.errorLabel.setHidden(False)
            return

        self.errorLabel.setHidden(True)
        self.solutionArr = list()
        perimeter = 0

        try:
            a = float(self.firstSide.text())
            b = float(self.secondSide.text())
            c = float(self.thirdSide.text())
        except:
            self.errorLabel.setText("Поля должны содержать только числа!")
            self.errorLabel.setHidden(False)
            return

        perimeter = a + b + c

        self.solutionArr += [a, b, c, perimeter]

        self.resultLabel.setText(f"Результат: {perimeter}")
        self.showSolution.setHidden(False)


    def validate(self):
        firstText = self.firstSide.text()
        secondText = self.secondSide.text()
        thirdText = self.thirdSide.text()

        if not (firstText and secondText and thirdText):
            return 0

        return 2

    def solution(self):
        self.solutionLabel.setHidden(not self.solutionLabel.isHidden())

        if self.solutionLabel.isHidden():
            return

        arr = self.solutionArr

        text = f'''Формула для периметра треугольника
        • P = a + b + c = {arr[0]} + {arr[1]} + {arr[2]} = {arr[3]}
        '''
        self.solutionLabel.setText(text)