#!/usr/bin/env python
from game import Game
from evolution import *
from utilities import *
from deck import *
from sys import argv

if __name__ == '__main__':

	n_decks = 6 # Number of decks in each generation
	mutation_rate = 0.15
	crossover_rate = 0.10
	loops=10

	if len(argv) == 5:
		loops = int(argv[1])
		n_decks = int(argv[2])
		mutation_rate = float(argv[3])
		crossover_rate = float(argv[4])
	elif len(argv) > 1:
		print 'Usage:', argv[0], 'n_iterations n_decks mutation_rate crossover_rate'
		exit()
	if mutation_rate > 1 or crossover_rate > 1:
		print 'Mutation and crossover rates should be between 0 and 1.'
		exit()

	decks = []
	DB = create_database()
	for i in range(n_decks):
		d = generate_random_deck(DB)
		decks.append(d)
	
	game = Game(decks)
	for _ in range(loops):
	
		game.fight()

		# Return a list with n_decks/2 decks
		winners = game.winners()

		decks = reproduce(winners, crossover_rate)

		decks = mutate(decks, DB, mutation_rate)

		game(decks)
	
	print '\nWinners:\n'
	for d in game.winners():
		print d
		print '-'*20
