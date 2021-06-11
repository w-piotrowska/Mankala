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
    res = []

    # ----- BEZ INTERFACE -------
    m = Mankala()
    res.append(m.play(1, 5, 2, 1))
    print("Ilość ruchów wygrywającego: "+str(res[0][0]))
    print("Czas: "+str(res[0][1]))

    # ----- Z INTERFACE -------
    # app = QApplication(sys.argv)
    # ex = interface.App()
    # if interface.MODE == 2:
    #     ex.on_click()
    # print("TO KONIEC")
    # sys.exit(app.exec_())






if __name__ == "__main__":
    main()

