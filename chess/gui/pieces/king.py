from piece import Piece


class King(Piece):
	
	def __init__(self, img_path, x, y):
		self.name = 'King'
		self.img_path = img_path
		self.x = x
		self.y = y
		super(King, self).__init__(self.name, self.img_path, self.x, self.y)	

	def get_reachable_coords(self):
		pass
