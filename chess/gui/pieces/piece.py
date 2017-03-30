from abc import ABCMeta, abstractmethod
import Tkinter as tk


class Piece(object):
	__metaclass__ = ABCMeta

	def __init__(self, name, img_path, x, y):
		self.name = name
		self.img_path = img_path
		self.image = self._create_image()
		self.x = x
		self.y = y

	def _create_image(self):
		return tk.PhotoImage(file=self.img_path)

	@abstractmethod
	def get_reachable_coords(self):
		pass
	
	def after_move_actions(self):
		pass
