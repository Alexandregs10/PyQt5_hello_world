import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

def main():
    app = QApplication(sys.argv)
    
    window = QWidget()
    
    window.setWindowTitle('Minha Primeira Janela')
    
    window.setGeometry(100, 100, 400, 300)
    
    label = QLabel('Olá, mundo!', window)
    label.move(150, 130) 

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

