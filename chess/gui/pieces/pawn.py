from abc import ABCMeta, abstractmethod
from piece import Piece


class Pawn(Piece):
	__metaclass__ = ABCMeta		

	def __init__(self, img_path, x, y):
		self.name = 'Pawn'
		self.img_path = img_path
		self.x = x
		self.y = y
		self.has_moved = False
		super(Pawn, self).__init__(self.name, self.img_path, self.x, self.y)
	
	def after_move_actions(self):
		self.has_moved = True
