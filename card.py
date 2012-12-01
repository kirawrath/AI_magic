
class Card:
	def __init__(self):
		self.name=''
		self.tapped = False
	def __str__(self):
		return self.name

class Creature(Card):
	def __init__(self):
		Card.__init__(self)
		self.sick = True
		self.power = 0
		self.toughness = 0
		self.dmg = 0
		self.attacking = False
		self.blocker = None
	def damage(self, amount):
		self.dmg = amount


class Land(Card):
	def __init__(self):
		Card.__init__(self)
		self.color = ''	