from card import *
class Deck:
	def __init__(self, cards = []):
		self.cards = cards
		self.win=0
		self.loss=0
	def __len__(self):
		return len(self.cards)
	def __iter__(self):
		return iter(self.cards)
	def __getitem__(self, i):
		return self.cards[i]
	def __setitem__(self, i, v):
		self.cards[i] = v
	def pop(self):
		return self.cards.pop()
	def __str__(self):
		st=''
		lands_st='\n'
		cards=[]
		totalcost=0.0
		lands=[]
		for d in self.cards:
			if isinstance(d, Land):
				if d.name in lands:
					continue
				lands_st+=str(len([c for c in self.cards if c.name == d.name])) 
				lands_st += 'x ' + str(d) + '\n'
				lands.append(d.name)
				continue
			totalcost += d.converted_cost()
			if d.name in cards:
				continue
			st += str(len([c for c in self.cards if c.name == d.name])) + 'x '
			st += str(d) + '\n'
			cards.append(d.name)
		st += lands_st
		st += '\nAvg Mana Cost: ' + str(totalcost/60) + '\n'
		st += 'Games won/lost: ' + str(self.win)+'/'+str(self.loss)+'\n'
		return st
	def add(self, card):
		self.cards.append(card)
	def remove(self, card):
		self.cards.remove(card)

