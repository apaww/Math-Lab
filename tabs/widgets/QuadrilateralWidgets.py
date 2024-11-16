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
        self.angle = LineEdit()
        self.height = LineEdit()
        self.firstDiagonal = LineEdit()
        self.secondDiagonal = LineEdit()
        self.calculateButton = PushButton()
        self.resultLabel = BodyLabel()
        self.showSolution = PushButton()
        self.solutionLabel = TextEdit()
        self.solutionArr = list()
        self.customFont = self.titleLabel.font()
        self.customFont.setWeight(60)
        self.customFont.setPointSize(20)

        self.titleLabel.setText("Найти площадь четырехугольника")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFont(self.customFont)

        self.chooseMethod.setPlaceholderText("Выберите способ нахождения")
        items = ['По двум сторонам и углу', 'По стороне и высоте', 'Прямоугольник', 'Квадрат', 'Ромб', 'Трапеция']
        self.chooseMethod.addItems(items)
        self.chooseMethod.setCurrentIndex(0)
        self.chooseMethod.currentTextChanged.connect(self.change)

        self.firstSide.setPlaceholderText("Сторона a")
        self.secondSide.setPlaceholderText("Сторона b")
        self.angle.setPlaceholderText("Угол")
        self.firstDiagonal.setPlaceholderText("Диагональ a")
        self.firstDiagonal.setHidden(True)
        self.secondDiagonal.setPlaceholderText("Диагональ b")
        self.secondDiagonal.setHidden(True)
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
        self.vSquareLayout.addWidget(self.firstDiagonal, 1)
        self.vSquareLayout.addWidget(self.secondDiagonal, 1)
        self.vSquareLayout.addWidget(self.angle, 1)
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
            self.angle.setHidden(False)
            self.height.setHidden(True)
            self.firstDiagonal.setHidden(True)
            self.secondDiagonal.setHidden(True)

            self.firstSide.setText("")
            self.secondSide.setText("")
            self.angle.setText("")
            self.height.setText("")
            self.firstDiagonal.setText("")
            self.secondDiagonal.setText("")

            self.errorLabel.setHidden(True)
            self.showSolution.setHidden(True)
            self.solutionLabel.setHidden(True)
        elif curIndex == 1:
            self.firstSide.setHidden(False)
            self.secondSide.setHidden(True)
            self.angle.setHidden(True)
            self.height.setHidden(False)
            self.firstDiagonal.setHidden(True)
            self.secondDiagonal.setHidden(True)

            self.firstSide.setText("")
            self.secondSide.setText("")
            self.angle.setText("")
            self.height.setText("")
            self.firstDiagonal.setText("")
            self.secondDiagonal.setText("")

            self.errorLabel.setHidden(True)
            self.showSolution.setHidden(True)
            self.solutionLabel.setHidden(True)
        elif curIndex == 2:
            self.firstSide.setHidden(False)
            self.secondSide.setHidden(False)
            self.angle.setHidden(True)
            self.height.setHidden(True)
            self.firstDiagonal.setHidden(True)
            self.secondDiagonal.setHidden(True)

            self.firstSide.setText("")
            self.secondSide.setText("")
            self.angle.setText("")
            self.height.setText("")
            self.firstDiagonal.setText("")
            self.secondDiagonal.setText("")

            self.errorLabel.setHidden(True)
            self.showSolution.setHidden(True)
            self.solutionLabel.setHidden(True)
        elif curIndex == 3:
            self.firstSide.setHidden(False)
            self.secondSide.setHidden(True)
            self.angle.setHidden(True)
            self.height.setHidden(True)
            self.firstDiagonal.setHidden(True)
            self.secondDiagonal.setHidden(True)

            self.firstSide.setText("")
            self.secondSide.setText("")
            self.angle.setText("")
            self.height.setText("")
            self.firstDiagonal.setText("")
            self.secondDiagonal.setText("")

            self.errorLabel.setHidden(True)
            self.showSolution.setHidden(True)
            self.solutionLabel.setHidden(True)
        elif curIndex == 4:
            self.firstSide.setHidden(True)
            self.secondSide.setHidden(True)
            self.angle.setHidden(True)
            self.height.setHidden(True)
            self.firstDiagonal.setHidden(False)
            self.secondDiagonal.setHidden(False)

            self.firstSide.setText("")
            self.secondSide.setText("")
            self.angle.setText("")
            self.height.setText("")
            self.firstDiagonal.setText("")
            self.secondDiagonal.setText("")

            self.errorLabel.setHidden(True)
            self.showSolution.setHidden(True)
            self.solutionLabel.setHidden(True)
        elif curIndex == 5:
            self.firstSide.setHidden(False)
            self.secondSide.setHidden(False)
            self.angle.setHidden(True)
            self.height.setHidden(False)
            self.firstDiagonal.setHidden(True)
            self.secondDiagonal.setHidden(True)

            self.firstSide.setText("")
            self.secondSide.setText("")
            self.angle.setText("")
            self.height.setText("")
            self.firstDiagonal.setText("")
            self.secondDiagonal.setText("")

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
                alpha = float(self.angle.text())

                try:
                    square = a * b * math.sin(alpha * math.pi / 180)
                except:
                    self.errorLabel.setText("Такого угла не существует!")
                    self.errorLabel.setHidden(False)
                    return

                self.solutionArr += [curIndex, a, b, alpha, square]
            elif curIndex == 1:
                a = float(self.firstSide.text())
                h = float(self.height.text())

                square = a * h

                self.solutionArr += [curIndex, a, h, square]
            elif curIndex == 2:
                a = float(self.firstSide.text())
                b = float(self.secondSide.text())

                square = a * b

                self.solutionArr += [curIndex, a, b, square]
            elif curIndex == 3:
                a = float(self.firstSide.text())

                square = a * a

                self.solutionArr += [curIndex, a, square]
            elif curIndex == 4:
                a = float(self.firstDiagonal.text())
                b = float(self.secondDiagonal.text())

                square = a * b / 2

                self.solutionArr += [curIndex, a, b, square]
            elif curIndex == 5:
                a = float(self.firstSide.text())
                b = float(self.secondSide.text())
                h = float(self.height.text())

                square = a * b / 2 * h

                self.solutionArr += [curIndex, a, b, h, square]
        except:
            self.errorLabel.setText("Поля должны содержать только числа!")
            self.errorLabel.setHidden(False)
            return

        self.resultLabel.setText(f"Результат: {square}")
        self.showSolution.setHidden(False)


    def validate(self, curIndex):
        firstText = self.firstSide.text()
        secondText = self.secondSide.text()
        angleText = self.angle.text()
        firstDText = self.firstDiagonal.text()
        secondDText = self.secondDiagonal.text()
        heightText = self.height.text()

        if curIndex == 0 and not (firstText and secondText and angleText):
            return 0
        elif curIndex == 1 and not(firstText and heightText):
            return 0
        elif curIndex == 2 and not(firstText and secondText):
            return 0
        elif curIndex == 3 and not(firstText):
            return 0
        elif curIndex == 4 and not(firstDText and secondDText):
            return 0
        elif curIndex == 5 and not(firstText and secondText and heightText):
            return 0

        return 2

    def solution(self):
        self.solutionLabel.setHidden(not self.solutionLabel.isHidden())

        if self.solutionLabel.isHidden():
            return

        arr = self.solutionArr

        if arr[0] == 0:
            text = f'''Формула для площади параллелограма по двум сторонам и углу между ними:
            • S = a ⋅ b ⋅ sin α = {arr[1]} ⋅ {arr[2]} ⋅ sin {arr[3]}° = {arr[4]}
            '''
            self.solutionLabel.setText(text)
        elif arr[0] == 1:
            text = f'''Формула для площади параллелограма по высоте и стороне, на которую она падает:
            • S = a ⋅ h = {arr[1]} ⋅ {arr[2]} = {arr[3]}
            '''
            self.solutionLabel.setText(text)
        elif arr[0] == 2:
            text = f'''Формула для площади прямоугольника:
            • S = a ⋅ b = {arr[1]} ⋅ {arr[2]} = {arr[3]}
            '''
            self.solutionLabel.setText(text)
        elif arr[0] == 3:
            text = f'''Формула для площади квадрата:
            • S = a ⋅ a = {arr[1]} ⋅ {arr[1]} = {arr[2]}
            '''
            self.solutionLabel.setText(text)
        elif arr[0] == 4:
            text = f'''Формула для площади ромба:
            • S = a ⋅ b / 2 = {arr[1]} ⋅ {arr[2]} / 2 = {arr[3]}
            '''
            self.solutionLabel.setText(text)
        elif arr[0] == 5:
            text = f'''Формула для площади трапеции:
            • S = a ⋅ b / 2 ⋅ h = {arr[1]} ⋅ {arr[2]} / 2 ⋅ {arr[3]} = {arr[4]}
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
        self.fourthSide = LineEdit()
        self.calculateButton = PushButton()
        self.resultLabel = BodyLabel()
        self.showSolution = PushButton()
        self.solutionLabel = TextEdit()
        self.solutionArr = list()
        self.customFont = self.titleLabel.font()
        self.customFont.setWeight(60)
        self.customFont.setPointSize(20)

        self.titleLabel.setText("Найти периметр четырехугольника")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFont(self.customFont)

        self.firstSide.setPlaceholderText("Сторона a")
        self.secondSide.setPlaceholderText("Сторона b")
        self.thirdSide.setPlaceholderText("Сторона c")
        self.fourthSide.setPlaceholderText("Сторона d")

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
        self.vSquareLayout.addWidget(self.fourthSide, 1)
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
            d = float(self.fourthSide.text())
        except:
            self.errorLabel.setText("Поля должны содержать только числа!")
            self.errorLabel.setHidden(False)
            return

        perimeter = a + b + c + d

        self.solutionArr += [a, b, c, d, perimeter]

        self.resultLabel.setText(f"Результат: {perimeter}")
        self.showSolution.setHidden(False)


    def validate(self):
        firstText = self.firstSide.text()
        secondText = self.secondSide.text()
        thirdText = self.thirdSide.text()
        fourthText = self.fourthSide.text()

        if not (firstText and secondText and thirdText and fourthText):
            return 0

        return 2

    def solution(self):
        self.solutionLabel.setHidden(not self.solutionLabel.isHidden())

        if self.solutionLabel.isHidden():
            return

        arr = self.solutionArr

        text = f'''Формула для периметра четырехугольника
        • P = a + b + c + d = {arr[0]} + {arr[1]} + {arr[2]} + {arr[3]} = {arr[4]}
        '''
        self.solutionLabel.setText(text)