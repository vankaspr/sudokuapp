import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("sudoku_app")
        self.setGeometry(0,0, 503, 520)
        self.setStyleSheet("background-color: #B8DAEF;")
        
        # загружаем пользовательский шрифт
        self.load_custom_font()
        
        # center widget
        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        # Layout для центрирования
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.layout.setAlignment(Qt.AlignCenter)
        
        self.startGUI()
        
    
    def load_custom_font(self):
        """Метод для загрузки пользовательского шрифта"""
        
        font_path = os.path.join(os.path.dirname(__file__), "font", "PublicPixel.ttf")
        font_id = QtGui.QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print("Error font!")
            return 
        
        font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
        self.custom_font = QtGui.QFont(font_family, 14) 

        
    
    def startGUI(self):
        """Интерфейс главного экрана: старт тут!"""
        
        # text
        self.header = QLabel("૮ ․ ․ ྀིა  sudoku ₊˚⊹ ᰔ", self.central_widget)
        self.header.setFont(self.custom_font)
        self.header.setGeometry(20, 100, 500, 100 )
        self.header.setStyleSheet(
            "font-style: normal;"
            "font-weight: 400;"
            "font-size: 28px;"
            "line-height: 51px;"
            "color: #D9EFFC;"
            # "border: 1px solid #1B4E6F;"
            "text-align: center;"
        )
        self.layout.addWidget(self.header, alignment=Qt.AlignCenter)
        
        # gif
        self.catGifLabel  = QLabel(self.central_widget)
        self.catGifLabel.setGeometry(0, 0,  self.central_widget.width(), self.central_widget.height())
        
        cat_gif = os.path.join(os.path.dirname(__file__), "gifs", "cat.gif")
        self.catGif =  QtGui.QMovie(cat_gif)
        self.catGifLabel.setMovie(self.catGif)
        
        self.catGif.start()
        
        self.catGifLabel.setScaledContents(True)  # Гифка подстраивается под QLabel
        self.catGifLabel.setFixedSize(190, 150)  # Устанавливаем размер QLabel
        
        
        self.layout.addWidget(self.catGifLabel, alignment=Qt.AlignCenter)
        
        
        # button
        self.leggoButton = QtWidgets.QPushButton(self.central_widget)
        self.leggoButton.setMinimumSize(141, 61) 
        self.leggoButton.setMaximumSize(141, 61) 
        self.leggoButton.setStyleSheet(
            "background: #1B4E6F;"
            "border: 2px solid #ECF6FC;"
            "font-style: normal;"
            "font-weight: 400;"
            "font-size: 22px;"
            "line-height: 39px;"
            "text-align: center;"
            "color: #D9EFFC;"
            "border-radius: 30px;"
        )
        self.leggoButton.setText("leggo")
        self.leggoButton.setFont(self.custom_font)
        
        self.layout.addWidget(self.leggoButton, alignment=Qt.AlignCenter)


    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    
