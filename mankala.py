import copy
import random
import sys
import time

from board import *

N = 6
K = 4

class Mankala:
    def __init__(self):
        self.board = Board(N, K)


    def __str__(self):
        return self.board.__str__()


    #mode: 0 - człowiek człowiek; 1 - człowiek - AI; 2 - AI - AI
    #type: 0 - minmax; 1 - alfa-beta
    def play(self, depth, depth2, mode, type):
        print(self)
        motions = 0
        motions1 = 0
        motions2 = 0
        start = time.time()
        active_player = 0
        # if mode == 2:
        #     m = random.randint(0, N-1)
        #     print("RUCH KOMPUTERA **** 0 ****: " + str(m + 1))
        #     active_player = self.board.move(active_player, m)
        #     print(self)
        while(not self.board.is_finish(active_player)):
            if active_player == 0:
                motions1 += 1
                if mode == 0 or mode == 1:
                    hole = int(input('Teraz gracz ' + str(active_player) + '\nWybierz dołek (1 - ' + str(N) + ')): '))
                    hole -= 1
                    active_player = self.board.move(active_player, hole)
                    print(self)
                if mode == 2:
                    if type == 0:
                        m = self.min_max(self.board, depth, True, active_player, 0)[1]
                    if type == 1:
                        m = self.alfa_beta(self.board, depth, True, -sys.maxsize - 1, sys.maxsize, active_player, 0)[1]
                    print("RUCH KOMPUTERA **** 0 ****: " + str(m + 1))
                    active_player = self.board.move(active_player, m)
                    print(self)
            else:
                motions2 += 1
                if mode == 0:
                    hole = int(input('Teraz gracz ' + str(active_player) + '\nWybierz dołek (1 - 6): '))
                    hole -= 1
                    active_player = self.board.move(active_player, hole)
                    print(self)
                if mode == 1 or mode == 2:
                    if type == 0:
                        m = self.min_max(self.board, depth2, True, active_player, 0)[1]
                    if type == 1:
                        m = self.alfa_beta(self.board, depth2, True, -sys.maxsize - 1, sys.maxsize, active_player, 0)[1]
                    print("RUCH KOMPUTERA **** 1 **** : " + str(m + 1))
                    active_player = self.board.move(active_player, m)
                    print(self)
        if self.board.end_of_the_game((active_player + 1) % 2) == 0:
            motions = motions1
        else:
            motions = motions2
        end = time.time()
        return [motions, end - start]


    def min_max(self, position, depth, maximizing_player, actual_player, hole):
        if depth == 0 or position.is_finish(actual_player): #position.is_finish((actual_player + 1) % 2):# or position.is_finish(actual_player):
            return [position.grade((actual_player + 1) % 2, hole), hole]

        if maximizing_player:
            max_eval = -sys.maxsize - 1
            best_node = -1
            for i in range(0, N):
                if position.players[actual_player][i] != 0:
                    child = copy.deepcopy(position)
                    if actual_player == child.move(actual_player, i):
                        tmp = self.min_max(child, depth, True, actual_player, i)
                        eval = tmp[0]
                        node = i
                    else:
                        tmp = self.min_max(child, depth - 1, False, (actual_player + 1) % 2, i)
                        eval = tmp[0]
                        node = tmp[1]
                    if max_eval < eval:
                        max_eval = eval
                        best_node = node
            return [max_eval, best_node]

        else:
            min_eval = sys.maxsize
            for i in range(0, N):
                if position.players[actual_player][i] != 0:
                    child = copy.deepcopy(position)
                    if actual_player == child.move(actual_player, i):
                        tmp = self.min_max(child, depth, False, actual_player, hole)
                    else:
                        tmp = self.min_max(child, depth - 1, True, (actual_player + 1) % 2, hole)
                    eval = tmp[0]
                    if min_eval > eval:
                        min_eval = eval
            return [min_eval, hole]

    def alfa_beta(self, position, depth, maximizing_player, alfa, beta, actual_player, hole):
        if depth == 0 or position.is_finish((actual_player + 1) % 2):# or position.is_finish(actual_player):
            return [position.grade((actual_player + 1) % 2, hole), hole]

        if maximizing_player:
            max_eval = -sys.maxsize - 1
            best_node = -1
            for i in range(0, N):
                if position.players[actual_player][i] != 0:
                    child = copy.deepcopy(position)
                    actual_player == child.move(actual_player, i)
                    tmp = self.alfa_beta(child, depth - 1, False, alfa, beta, (actual_player + 1) % 2, i)
                    eval = tmp[0]
                    node = tmp[1]
                    if alfa < eval:
                        alfa = eval
                        best_node = node
                    if alfa >= beta:
                        return [beta, hole]
            return [alfa, best_node]

        else:
            min_eval = sys.maxsize
            best_node = -1
            for i in range(0, N):
                if position.players[actual_player][i] != 0:
                    child = copy.deepcopy(position)
                    child.move(actual_player, i)
                    tmp = self.alfa_beta(child, depth - 1, True, alfa, beta, (actual_player + 1) % 2, hole)
                    eval = tmp[0]
                    if beta > eval:
                        beta = eval
                    if alfa >= beta:
                        return [alfa, hole]
            return [beta, hole]
