import os
import Tkinter as tk
from pieces import Bishop, Blank, King, Knight, WhitePawn, BlackPawn, Queen, Rook
from square import Square


IMAGE_PATH = '{}/pieces/images/{}.png'.format(os.path.dirname(os.path.abspath(__file__)), '{}')


class Board():

	def __init__(self, parent, players):
		self.parent = parent
		self.players = players
		self.frame = tk.Frame(self.parent)
		self.first_square = None
		self.second_square = None
		self.squares = [[0 for i in range(8)] for i in range(8)]
		self._setup_board()
	
	def move(self, square):
		if not self.first_square and not self.second_square:
			self.first_square = square
			return
		if self.first_square and not self.second_square:
			self.second_square = square
		if not self.first_square and self.second_square:
			self.first_square = square
		if self.first_square and self.second_square:
			if self.check_valid_move():
				self.swap()
				if self.check_gameover():
					self.calc_winner()
			else:
				print 'INVALID MOVE'
			self.first_square = None
			self.second_square = None
				
	def check_valid_move(self):
		piece1 = self.first_square.piece
		piece2 = self.second_square.piece
		print piece1.get_reachable_coords()
		for coord in piece1.get_reachable_coords():
			if coord[0] == piece2.x and coord[1] == piece2.y:
				return True
		return False
	
	def swap(self):
		if not isinstance(self.second_square, Blank):
			self.second_square.piece = Blank(img_path=IMAGE_PATH.format('blank'), x=self.second_square.piece.x, y=self.second_square.piece.y)
		piece1 = self.first_square.piece
		piece2 = self.second_square.piece
		self.squares[piece2.x][piece2.y] = self.first_square
		self.squares[piece1.x][piece1.y] = self.second_square
		self.first_square.grid(column=piece2.x, row=piece2.y, sticky='nsew')
		self.second_square.grid(column=piece1.x, row=piece1.y, sticky='nsew')

	def check_gameover(self):
		return False

	def calc_winner(self):
		pass

	def add_pieces_to_board(self):
		all_pieces = self.players[0].pieces + self.players[1].pieces
		for x in range(8):
			for y in range(8):
				square = None
				for piece in all_pieces:
					if piece.x == x and piece.y == y:
						square = Square(self.frame, piece, command=self.move)
						break
				else:
					square = Square(self.frame, Blank(img_path=IMAGE_PATH.format('blank'), x=x, y=y), command=self.move)
				self.squares[x][y] = square
				square.grid(column=x, row=y, sticky='nsew')	 

	def _setup_board(self):
		self.parent.title = 'Chess'
		self.parent.geometry('600x600')
		tk.Grid.rowconfigure(self.parent, 0, weight=1)
		tk.Grid.columnconfigure(self.parent, 0, weight=1)
		self.frame.grid(row=0, column=0, sticky='nsew')
		grid = tk.Frame(self.frame)
		grid.grid(sticky='nsew', column=0, row=7, columnspan=2)
		tk.Grid.rowconfigure(self.frame, 7, weight=1)  
                tk.Grid.columnconfigure(self.frame, 0, weight=1)	

		player1_pieces = []
		player2_pieces = []

		# create pawns
		for i in range(8):
			player1_pieces.append(WhitePawn(img_path=IMAGE_PATH.format('P'), x=i, y=1))
			player2_pieces.append(BlackPawn(img_path=IMAGE_PATH.format('p'), x=i, y=6))
		
		# create others
		player1_pieces.append(Rook(img_path=IMAGE_PATH.format('R'), x=0, y=0))
		player1_pieces.append(Rook(img_path=IMAGE_PATH.format('R'), x=7, y=0))
		player1_pieces.append(Knight(img_path=IMAGE_PATH.format('N'), x=1, y=0))
		player1_pieces.append(Knight(img_path=IMAGE_PATH.format('N'), x=6, y=0))
		player1_pieces.append(Bishop(img_path=IMAGE_PATH.format('B'), x=2, y=0))
		player1_pieces.append(Bishop(img_path=IMAGE_PATH.format('B'), x=5, y=0))

                player2_pieces.append(Rook(img_path=IMAGE_PATH.format('r'), x=0, y=7))
                player2_pieces.append(Rook(img_path=IMAGE_PATH.format('r'), x=7, y=7))
                player2_pieces.append(Knight(img_path=IMAGE_PATH.format('n'), x=1, y=7))
                player2_pieces.append(Knight(img_path=IMAGE_PATH.format('n'), x=6, y=7))
                player2_pieces.append(Bishop(img_path=IMAGE_PATH.format('b'), x=2, y=7))
                player2_pieces.append(Bishop(img_path=IMAGE_PATH.format('b'), x=5, y=7))

		# create king + queens		
		player1_pieces.append(King(img_path=IMAGE_PATH.format('K'), x=3, y=0))
		player1_pieces.append(Queen(img_path=IMAGE_PATH.format('Q'), x=4, y=0))
		player2_pieces.append(King(img_path=IMAGE_PATH.format('k'), x=4, y=7))
		player2_pieces.append(Queen(img_path=IMAGE_PATH.format('q'), x=3, y=7))
	
		self.players[0].pieces = player1_pieces
		self.players[1].pieces = player2_pieces

		self.add_pieces_to_board()

		for x in range(8):
			tk.Grid.columnconfigure(self.frame, x, weight=1)

		for y in range(8):
			tk.Grid.rowconfigure(self.frame, y, weight=1)
