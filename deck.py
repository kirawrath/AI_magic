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
		cards=[]
		for d in self.cards:
			if d.name in cards:
				continue
			st += str(len([c for c in self.cards if c.name == d.name])) + 'x '
			st += str(d) + '\n'
			cards.append(d.name)
		return st

