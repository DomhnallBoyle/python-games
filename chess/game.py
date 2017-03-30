from gui.board import Board
from player import Player 
import Tkinter as tk


class Game:
	
	def __init__(self):
		self.players = self._setup_players()
		self.root = tk.Tk()
		self.board = self._setup_board()

	def play_game(self):
		self.root.mainloop()	

	def _setup_players(self):
		return [Player(), Player()]

	def _setup_board(self):
		return Board(self.root, self.players)

	def _is_gameover(self):
		pass
