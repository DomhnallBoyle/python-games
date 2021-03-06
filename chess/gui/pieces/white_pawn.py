from pawn import Pawn


class WhitePawn(Pawn):
	
	def __init__(self, img_path, x, y):
		super(WhitePawn, self).__init__(img_path, x, y)

	def get_reachable_coords(self):
		if self.has_moved:
			return [(self.x, self.y+1)]
		else:
			return [(self.x, self.y+1), (self.x, self.y+2)]

