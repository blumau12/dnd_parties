from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
import sys

from gui_tools.widgets import CompanyWorld, Characters
from core.container import Data


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("DnD parties")
        self.resize(1024, 768)

        self.data = Data()
        self.company_world = CompanyWorld(self)
        self.tools = None
        self.characters = Characters(self)

        self.init_gui()

    def init_gui(self):
        v_box = QVBoxLayout()

        h_box_tools = QHBoxLayout()
        h_box_tools.addWidget(self.company_world, stretch=0)
        label2 = QLabel('tools', self)
        label2.setAlignment(Qt.AlignCenter)
        h_box_tools.addWidget(label2, stretch=1)
        v_box.addLayout(h_box_tools, stretch=0)

        v_box.addWidget(self.characters, stretch=1)

        self.setLayout(v_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
