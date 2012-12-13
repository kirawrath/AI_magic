from deck import Deck
from card import *
from utilities import debug, debug_flag
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
			debug('Deckout!')
			return False
		self.hand.append(self.deck.pop())
		return True
	def try_to_pay_cost(self, card):
		lands = self.lands()
		used=[]
		for c in card.cost:
			for l in lands:
				if l not in used and (not l.tapped) and l.color == c:
					used.append(l)
					break
			else:
				n = card.cost[card.cost.index(c):]
				if n.isdigit():
					n=int(n)
					for l in lands:
						if l not in used and not l.tapped:
							used.append(l)
							n-=1
							if n == 0:
								break
					else:
						return False
					for u in used:
						u.tap()
					return True
				else:
					return False
		for u in used:
			u.tap()
		return True

	def play_card_type(self, card_type):
		if card_type == Land:
			for d in self.hand:
				if isinstance(d, card_type):
					self.battlefield.append(self.hand.pop(self.hand.index(d)))
					return True
			return False
		elif card_type == Creature:
			for d in self.hand:
				if isinstance(d, card_type):
					if self.try_to_pay_cost(d):
						debug('Casting', d, d.cost)
						self.battlefield.append(d)
						self.hand.remove(d)
						return True
			return False
		if debug_flag:
			assert False
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
				debug('Attacking:', atkr)
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
					debug(defr, 'blocked',atkr)
					break

