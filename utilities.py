from random import sample, seed, random
from card import *
from deck import Deck
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
			if line[2][0] in [str(i) for i in range(10)]:
				card.cost = line[2][::-1] #reverse string

			card.cost = line[2]
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
			deck.cards.append(card)
	return deck
