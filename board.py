import numpy as np

N = 6
# K = 4

class Board:
    def __init__(self, N, K):
        self.players = [np.repeat(K, N + 1),np.repeat(K, N + 1)]
        self.players[0][N] = 0
        self.players[1][N] = 0
        self.active_player = 0

        self.type_last_move = -1

    def __str__(self):
        res = ""
        for i in range(len(self.players[0])-1, -1, -1):
            res = res + str(self.players[0][i]) + "\t"
        res = res + "\n\t"
        for i in range(0, len(self.players[1])):
            res = res + str(self.players[1][i]) + "\t"
        return res

    def move(self, player, hole):
        if 0 <= hole < N:
            stones = self.players[player][hole]
            self.players[player][hole] = 0
            miss = False
            if stones > 0:
                actual_hole = hole + 1
                while(stones > 0):
                    if actual_hole < N or (actual_hole == N and not miss):
                        self.players[player][actual_hole] += 1
                        stones -= 1
                        actual_hole += 1
                    else:
                        player = (player + 1) % 2
                        actual_hole = 0
                        miss = not miss
                actual_hole -= 1
                if actual_hole == N:
                    return player
                if self.players[player][actual_hole] == 1 and not miss:
                    self.players[player][N] += self.players[(player + 1) % 2][N - actual_hole - 1]
                    self.players[(player + 1) % 2][N - actual_hole - 1] = 0
                if miss:
                    return player
                return (player + 1) % 2

            else:
                #print("Tu nie ma kamyczków.")
                pass

        else:
            print("Nie ma takiego pola")
        return player


    def is_finish(self, player):
        for i in range(0, N):
            if self.players[player][i] != 0:
                return False
        return True

    def play(self):
        print(self)
        active_player = 0
        while(not self.is_finish(active_player)):
            hole = int(input('Teraz gracz ' + str(active_player) + '\nWybierz dołek (1 - 6): '))
            hole -= 1
            active_player = self.move(active_player, hole)
            print(self)
        self.end_of_the_game((active_player + 1) % 2)
        if self.players[0][N] > self.players[1][N]: winner = 0
        else: winner = 1
        print("KONIEC GRY!")
        print("Wygrał gracz " + str(winner) + "!")
        print("Gratulacje!")

    def end_of_the_game(self, player):
        print("Koniec ruchów - koniec gry!")
        for i in range(0, 2):
            for j in range(0, N):
                self.players[player][N] += self.players[i][j]
                self.players[i][j] = 0
        print(self)
        if self.players[0][N] > self.players[1][N]: winner = 0
        else: winner = 1
        print("KONIEC GRY!")
        print("Wygrał gracz " + str(winner) + "!")
        print("Gratulacje!")
        return winner

    def grade1(self, player, hole):
        return self.players[player][N]

    def grade(self, player, hole):
        return self.players[player][N] - self.players[(player + 1) % 1][N]

    def grade3(self, player, hole):
        return N - hole





