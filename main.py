from PyQt5.QtWidgets import QApplication

import interface
from board import *
from mankala import *
import tkinter as tk
import tkinter.ttk as ttk
import pygubu


def main():
    #mode: 0 - człowiek człowiek; 1 - człowiek - AI; 2 - AI - AI
    #type: 0 - minmax; 1 - alfa-beta
    #def play(self, depth, depth2, mode, type):
    # m = Mankala()
    # m.play(3, 3, 1, 0)
    app = QApplication(sys.argv)
    ex = interface.App()
    if interface.MODE == 2:
        ex.on_click()
    print("TO KONIEC")
    sys.exit(app.exec_())






if __name__ == "__main__":
    main()

