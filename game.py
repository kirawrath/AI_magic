from random import shuffle
from deck import Deck
from card import *
from player import *
from utilities import debug, debug_flag, print_field
from copy import copy, deepcopy
trace_battle=True # To print (or not) the battle
class Game:
	def __init__(self, decks):
		self.decks = decks
	def __call__(self, decks):
		self.decks = decks
	def winners(self):
		winners = []
		for _ in range(len(self.decks)/2):
			ratio = -1
			winner = None
			for d in self.decks:
				if d in winners or (d.win+d.loss==0):
					continue
				if (float(d.win)/(d.win+d.loss)) > ratio:
					ratio = float(d.win)/(d.win+d.loss)
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
			d1 = decks[i]
			d2 = []
			if len(decks)-1 == i:
				d2 = decks [i-1]
			else:
				d2 = decks[i+1]

			shuffle(d1.cards)
			shuffle(d2.cards)

			assert d1 is not d2
			assert len(d1) == 60 and len(d2) == 60

			p1 = Player(deepcopy(d1), 1)
			p2 = Player(deepcopy(d2), 2)
			# p1 doesn't draw in the first turn
			p1.deck.cards.append(p1.hand.pop())

			n_turns = 0

			while p1.life > 0:
				
				p1.untap_and_upkeep()
				if(not p1.draw()):
					p1,p2=p2,p1
					n_turns+=1
					break
				p1.play_card_type(Land)
				while p1.play_card_type(Creature):
					pass
				p1.attack(p2)
				p2.defend(p1)
				self.resolve_damage(p1, p2)

				if len(p1.hand) > 7:
					debug('Removing', p1.hand[0].name, 'from hand.')
					p1.hand.pop(0)
				
				if debug_flag and trace_battle:
					if n_turns % 2 == 0:
						print 'Turn', n_turns, ': p1', '('+str(p1.deck.id)+')',
						print p1.life, ' p2', '('+str(p2.deck.id)+')', p2.life
						print( 'p1:')
						print_field(p1.battlefield)
						print( 'p2:')
						print_field(p2.battlefield)
						p1, p2 = p2, p1
					else:
						p1, p2 = p2, p1
						print 'Turn', n_turns, ': p1', '('+str(p1.deck.id)+')',
						print p1.life, ' p2', '('+str(p2.deck.id)+')', p2.life
						print( 'p1:')
						print_field(p1.battlefield)
						print( 'p2:')
						print_field(p2.battlefield)
					print( '-'*20)
				else:
					p1,p2 = p2,p1

				n_turns+=1
			n_turns-=1
			debug('Game ended in', n_turns,'turns.')
			if n_turns % 2==0:
				p1,p2=p2,p1
			debug('Lives:', p1.life, p2.life)
			assert len(d1) == 60 and len(d2) == 60
			# Compute score
			if p1.life <= 0:
				if p1.id == 1:
					d1.loss += 1
					d2.win += 1
				else:
					d1.win += 1
					d2.loss += 1
			else:
				assert p2.life <= 0
				if p2.id == 2:
					d1.win += 1
					d2.loss += 1
				else:
					d1.loss += 1
					d2.win += 1
