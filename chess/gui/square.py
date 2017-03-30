from Tkinter import Button


class Square(Button, object):

	def __init__(self, frame, piece, command):
		self.frame = frame
		self.piece = piece
		self.command = lambda: command(self)
		super(Square, self).__init__(self.frame, image=self.piece.image, command=self.command)
