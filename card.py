	
class Card:
	def __init__(self):
		self.name=''
		self.tapped = False
	def __str__(self):
		return self.name
	def tap(self):
		self.tapped = True

class Creature(Card):
	def __init__(self):
		Card.__init__(self)
		self.sick = True
		self.power = 0
		self.toughness = 0
		self.dmg = 0
		self.attacking = False
		self.blocker = None
		self.cost = ''
	def damage(self, amount):
		self.dmg = amount
	def converted_cost(self):
		c=0
		cost = self.cost
		for d in cost:
			if d.isalpha():
				c+=1
			else:
				n=cost[cost.index(d):]
				if n.isdigit():
					c += int(n)
					break
				else:
					print 'Failed to get converted mana cost'
		return c


class Land(Card):
	def __init__(self):
		Card.__init__(self)
		self.color = ''	
