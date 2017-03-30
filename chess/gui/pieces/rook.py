from piece import Piece


class Rook(Piece):

	def __init__(self, img_path, x, y):
		self.name = 'Rook'
		self.img_path = img_path
		self.x = x
		self.y = y
		super(Rook, self).__init__(self.name, self.img_path, self.x, self.y)

	def get_reachable_coords(self):
		pass
