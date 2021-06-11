import time

from PyQt5 import QtWidgets
import sys

from functools import partial
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from mankala import *

INTERFACE_Y = 100
DEPTH = 5
DEPTH2 = 5
MODE = 0
TYPE = 1

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Mankala'
        self.left = 10
        self.top = 10
        self.width = 1024
        self.height = 400
        self.holes = [[],[]]
        self.active_player = 0
        self.mankala = Mankala()
        self.label = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel(self)
        self.label.setGeometry(500, 20, 100, 100)


        for i in range(0, 6):
            button = QPushButton('4', self)
            button.setGeometry(200+100*i, INTERFACE_Y+100, 100, 100)
            button.setToolTip('0_'+str(i))
            button.clicked.connect(self.on_click)
            button.setStyleSheet("background-image : url(images_100/4_hole.png); border: 1px solid #000;")

            self.holes[0].append(button)

        button = QPushButton('0', self)
        button.setGeometry(800, INTERFACE_Y, 100, 200)
        button.setToolTip('0_6')
        button.clicked.connect(self.on_click)
        button.setStyleSheet("background-image : url(images_100/0_well.png); border: hidden;")
        self.holes[0].append(button)

        for i in range(0, 6):
            button = QPushButton('4', self)
            button.setGeometry(700-100*i, INTERFACE_Y, 100, 100)
            button.setToolTip('1_'+str(i))
            button.clicked.connect(self.on_click)
            button.setStyleSheet("background-image : url(images_100/4_hole.png); border: hidden;")

            self.holes[1].append(button)

        button = QPushButton('0', self)
        button.setGeometry(100, INTERFACE_Y, 100, 200)
        button.setToolTip('1_6')
        button.clicked.connect(self.on_click)
        button.setStyleSheet("background-image : url(images_100/0_well.png); border: hidden;")
        self.holes[1].append(button)

        self.show()

    @pyqtSlot()
    def on_click(self):
        if MODE == 2 or self.active_player == int(self.sender().toolTip()[0]):

            if self.check_player_is_human():
                hole_player = int(self.sender().toolTip()[0])
                hole_number = int(self.sender().toolTip()[2])

                print("hole_player = " + str(hole_player))
                print("hole_number = " + str(hole_number))
                print()

            # if MODE == 2:
            #     m = random.randint(0, N-1)
            #     print("RUCH KOMPUTERA **** 0 ****: " + str(m + 1))
            #     active_player = self.board.move(active_player, m)
            #     print(self)
            is_do_again = True
            while(not self.mankala.board.is_finish(self.active_player) and is_do_again):
                if self.active_player == 0:
                    if MODE == 0 or MODE == 1:
                        self.active_player = self.mankala.board.move(self.active_player, hole_number)
                        print(self.mankala)
                        self.update_interface()
                        if MODE == 0:
                            is_do_again = False
                        if MODE == 1 and self.active_player == 0:
                            is_do_again = False
                    if MODE == 2:
                        if TYPE == 0:
                            m = self.mankala.min_max(self.mankala.board, DEPTH, True, self.active_player, 0)[1]
                        if TYPE == 1:
                            m = self.mankala.alfa_beta(self.mankala.board, DEPTH, True, -sys.maxsize - 1, sys.maxsize, self.active_player, 0)[1]
                        print("RUCH KOMPUTERA **** 0 ****: " + str(m + 1))
                        time.sleep(1)
                        self.active_player = self.mankala.board.move(self.active_player, m)
                        print(self.mankala)
                        self.update_interface()
                else:
                    if MODE == 0:
                        self.active_player = self.mankala.board.move(self.active_player, hole_number)
                        print(self.mankala)
                        self.update_interface()
                        is_do_again = False
                    if MODE == 1 or MODE == 2:
                        if TYPE == 0:
                            m = self.mankala.min_max(self.mankala.board, DEPTH2, True, self.active_player, 0)[1]
                        if TYPE == 1:
                            m = self.mankala.alfa_beta(self.mankala.board, DEPTH2, True, -sys.maxsize - 1, sys.maxsize, self.active_player, 0)[1]
                        print("RUCH KOMPUTERA **** 1 **** : " + str(m + 1))
                        time.sleep(1)
                        self.active_player = self.mankala.board.move(self.active_player, m)
                        print(self.mankala)
                        self.update_interface()
                        if MODE == 1 and self.active_player == 0:
                            is_do_again == False
            if self.mankala.board.is_finish(self.active_player):
                winner = self.mankala.board.end_of_the_game((self.active_player + 1) % 2)
                self.update_interface()
                self.label.setText("Wygrał Gracz " + str(winner) + "!")

    def check_player_is_human(self):
        return MODE == 0 or (MODE == 1 and self.active_player == 0)

    def update_interface(self):

        for i in range(0, 2):
            for j in range(0, 7):
                if j == 6:
                    self.holes[i][j].setStyleSheet("background-image : url(images_100/"+str(self.mankala.board.players[i][j])+"_well.png); border: none;") \
                        if self.mankala.board.players[i][j] < 34 else self.holes[i][j].setStyleSheet("background-image : url(images_100/34_well.png); border: none;")
                    self.holes[i][j].setText(str(self.mankala.board.players[i][j]))

                else:
                    if i == self.active_player:
                        self.holes[i][j].setStyleSheet("background-image : url(images_100/"+str(self.mankala.board.players[i][j])+"_hole.png); border: 1px solid #000;") \
                            if self.mankala.board.players[i][j] < 20 else self.holes[i][j].setStyleSheet("background-image : url(images_100/20_hole.png); border: 1px solid #000;")
                    else:
                        self.holes[i][j].setStyleSheet("background-image : url(images_100/"+str(self.mankala.board.players[i][j])+"_hole.png); border: hidden;") \
                            if self.mankala.board.players[i][j] < 20 else self.holes[i][j].setStyleSheet("background-image : url(images_100/20_hole.png); border: hidden;")

                    self.holes[i][j].setText(str(self.mankala.board.players[i][j]))
