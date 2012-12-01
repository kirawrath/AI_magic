from random import sample, seed, random
from card import *
from deck import Deck
import copy
debug_flag=True
def debug(*args):
	if debug_flag:
		for a in args:
			print a,
		print
def create_database():
	f = open('./database')
	DB=[]
	for line in f:
		line = line.split()
		card = None
		name = line[0].replace('_', ' ')
		if line[1] == 'L':
			card = Land()
			card.color = line[2]
			card.name = name
		if line[1] == 'C':
			card = Creature()
			card.name = name
			card.cost = line[2]
			if line[2][0].isdigit():
				card.cost = line[2][::-1] #reverse string
				if card.cost[-2].isdigit(): #mana cost > 10
					card.cost[-1], card.cost[-2] = card.cost[-2], card.cost[-1]
			card.power = int(line[3])
			card.toughness = int(line[4])
			
		DB.append(card)
	return DB

def generate_random_deck(DB):
	seed()
	deck = Deck([])
	assert len(deck) == 0
	while len(deck.cards) < 60:
		card = DB[int(len(DB) * random())]
		count = len([x for x in deck if x.name == card.name])
		if count < 4 or isinstance(card, Land):
			deck.cards.append(copy.copy(card))
	return deck
