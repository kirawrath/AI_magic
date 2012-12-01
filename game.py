from random import shuffle
from deck import Deck
from card import *
class Player:
	def __init__(self, deck, idd=0):
		self.deck = deck
		self.life = 20
		self.hand = []
		self.id = idd
		for i in range(7):
			self.hand.append(self.deck.pop())
		self.battlefield = []
	def dec_life(self, amount):
		self.life -= amount
	def draw(self):
		if len(self.deck) == 0:
			self.life = 0
			print 'Deckout!'
			return
		self.hand.append(self.deck.pop())
	def play_card_type(self, card_type):
		for d in self.hand:
			if isinstance(d, card_type):
				self.battlefield.append(self.hand.pop(self.hand.index(d)))
				return
	def untap_and_upkeep(self):
		for d in self.battlefield:
			d.tapped = False
			d.sick = False
	def attack(self, p2):
		for atkr in self.creatures():
			if atkr.sick:
				continue
			atkr.attacking = True
			for defr in p2.creatures():
				if defr.toughness > atkr.power and (not defr.tapped):
					atkr.attacking = False
					break
			if atkr.attacking:
				print atkr
	def creatures(self):
		return [c for c in self.battlefield if isinstance(c, Creature)]
	def lands(self):
		return [c for c in self.battlefield if isinstance(c, Land)]
	def defend(self, p1):
		for defr in self.creatures():
			if defr.tapped:
				continue
			attackers = [a for a in p1.creatures() if a.attacking and \
					a.blocker == None]
			for atkr in attackers:
				if defr.power >= atkr.toughness:
					defr.damage(atkr.power)
					atkr.damage(defr.power)
					atkr.blocker = defr
					print 'blocking:',atkr.name,defr.name
					break

class Game:
	def __init__(self, decks):
		self.decks = decks
	def __call__(self, decks):
		self.decks = decks
	def winners(self):
		winners = []
		for _ in range(len(self.decks)/2):
			win = 0
			winner = None
			for d in self.decks:
				if d in winners:
					continue
				if d.win > win:
					win = d.win
					winner = d
			assert winner != None
			winners.append(winner)
		return winners
	def resolve_damage(self, p1, p2=None):
		removed = True
		while removed:
			removed = False
			for c in p1.creatures():
				if c.dmg >= c.toughness:
					removed = True
					p1.battlefield.remove(c)
		if p2 != None:
			self.resolve_damage(p2)
		else:
			return
		
		# Non-blocked attacking creatures will damage opponent
		for c in p1.creatures():
			if c.blocker == None and c.attacking:
				p2.dec_life(c.power)
			c.blocker = None
			c.attacking = False


	def fight(self):
		decks = self.decks
		for i in range(0, len(decks), 2):
			p1 = decks[i]
			p2 = []
			if len(decks) == i-1:
				p2 = decks [i-1]
			else:
				p2 = decks[i+1]

			shuffle(p1)
			shuffle(p2)

			p1 = Player(p1, 1)
			p2 = Player(p2, 2)
			n_turns = 0

			while p1.life > 0:
				
				p1.untap_and_upkeep()
				p1.draw()
				p1.play_card_type(Land)
				p1.play_card_type(Creature)
				p1.attack(p2)
				p2.defend(p1)
				self.resolve_damage(p1, p2)

				if len(p1.hand) > 7:
					print 'Removing', p1.hand[0].name, 'from hand.'
					p1.hand.pop(0)
				
				if n_turns % 2 == 0:
					print 'Turn', n_turns, ': p1', p1.life, ' p2', p2.life
					print 'p1:'
					for c in p1.creatures():
						print c.name
					print 'p2:'
					for c in p2.creatures():
						print c.name
					p1, p2 = p2, p1
				else:
					p1, p2 = p2, p1
					print 'Turn', n_turns, ': p1', p1.life, ' p2', p2.life
					print 'p1:'
					for c in p1.creatures():
						print c.name
					print 'p2:'
					for c in p2.creatures():
						print c.name
				print '-'*20

				n_turns+=1
			print 'Game ended in', n_turns,'turns.'
			print 'Lives:', p1.life, p2.life

			if p2.life == 0: #p2 died by deckout before killing p1
				p2.deck.loss += 1
				p1.deck.win += 1
			else:
				p1.deck.win += 1
				p2.deck.loss += 1
