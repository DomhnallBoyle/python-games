

class Player(object):

	def __init__(self):
		self.name = self._get_player_name()
		self.pieces = []
		self.score = 0

	def _get_player_name(self):
		name = raw_input('Enter a name for player: ')
		while len(name) <= 0:
			name = raw_input('Enter a name for player: ')
		return name	

	def make_move(self):
		pass

	
