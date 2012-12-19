#!/usr/bin/env python
from game import Game
from evolution import *
from utilities import *
from deck import *
from sys import argv

if __name__ == '__main__':
	n_decks = 12 # Number of decks in each generation
	decks = []
	DB = create_database()
	for i in range(n_decks):
		d = generate_random_deck(DB)
		decks.append(d)
	
	game = Game(decks)
	
	loops=1
	if len(argv) > 1:
		loops = int(argv[1])

	for _ in range(loops):
	
		game.fight()

		# Return a list with n_decks/2 decks
		winners = game.winners()

		decks = reproduce(winners, 0.10) #crossover

		decks = mutate(decks, DB, 0.15)

		game(decks)
	
	print '\nWinners:\n'
	for d in game.winners():
		print d
		print '-'*20
