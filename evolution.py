from random import random, sample
from deck import *
from card import *

def reproduce(winners, amount=0.1):
	assert amount <= 1
	assert len(winners) > 1

	n_children = len(winners)
	children=[]
	while n_children > 0:
		l = sample(winners, 2)
		d1 = l[0]
		d2 = l[1]
		if d1 == d2:
			continue
		assert len(d1) == 60 and len(d2) == 60
		c1, c2 = crossover(d1,d2,int(amount*60))
		children.append(c1)		
		children.append(c2)		
		n_children -= 2
	# If I added an extra child, discard one
	if n_children < 0:
		children.pop()
	
	winners.extend(children)
	return winners

# Return two children of deck1 and deck2
# n_swaps is the amount of cards to be
# exchanged
def crossover(deck1, deck2, n_swaps):
	while n_swaps:
		a=Deck() ; b=Deck()
		a.cards = deck1.cards
		b.cards = deck2.cards
		card = a[int(random()*60)]
		count = len([x for x in b if x.name == card.name])
		if count < 4 or isinstance(card, Land):
			for _ in range(1000):
				card2 = b[int(random()*60)]
				count2 = len([x for x in a if x.name == card2.name])
				if count2 < 4 or isinstance(card, Land):
					a.remove(card)
					b.add(card)
					b.remove(card2)
					a.add(card2)

					n_swaps-=1
					break
			else:
				print('Could not crossover decks properly')
	return a, b

# Mutate a list of decks
def mutate(decks, DB, amount=0.15):
	assert amount <= 1
	for d in decks:
		mutate_deck(d, DB, amount*60)
	return decks
# Mutate deck by changing amount% of its cards
# with cards from DB
def mutate_deck(deck, DB, n_swaps):
	assert len(deck) == 60 
	while n_swaps:	
		card = DB[int(random()*len(DB))]
		count = len([x for x in deck if x.name == card.name])
		if count < 4 or isinstance(card, Land):
			# Remove random card
			dead = sample(deck.cards, 1)[0]
			deck.remove(dead)
			# Add this one
			deck.add(card)
			n_swaps-=1
