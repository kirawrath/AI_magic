#!/usr/bin/env python
from game import Game
from evolution import *
from utilities import *
from deck import *


if __name__ == '__main__':
	n_decks = 2 # Number of "best decks"
	assert n_decks % 2 == 0
	decks = []
	DB = create_database()
	for i in range(n_decks):
		d = generate_random_deck(DB)
		decks.append(d)
	
	game = Game(decks)
	
	if True:
	
		game.fight()

		# Return a list with half the size of "decks"
		winners = game.winners()

		decks = reproduce(winners) #crossover

		decks = mutate(decks)

		game(decks)
	
	
