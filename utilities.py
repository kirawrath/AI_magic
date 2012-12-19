from random import sample, seed, random
from card import *
from deck import Deck
import copy
#trace_battle=True # To print (or not) the battle
trace_battle=False
#debug_flag=True
debug_flag=False
partial_results = False #To print partial results
def debug(*args):
	if debug_flag:
		for a in args:
			print a,
		print
deck_id = -1
def get_new_id():
	global deck_id
	deck_id+=1
	if debug_flag:
		print 'Deck', deck_id, 'created!'
	return deck_id
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
		elif line[1] == 'C':
			assert len(line) == 5
			card = Creature()
			card.name = name
			card.cost = line[2]
			if line[2][0].isdigit():
				card.cost = line[2][::-1] #reverse string
				# Don't work for mana cost > 99 (which is fine).
				if len(card.cost) > 1 and card.cost[-2].isdigit(): #mana cost > 10
					card.cost = card.cost[:len(card.cost)-2]+card.cost[-1]+card.cost[-2]
			card.power = int(line[3])
			card.toughness = int(line[4])
		else:
			print line
			assert False
			
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
def print_field(bf):
	st=''
	lands_st='\n'
	cards=[]
	lands=[]
	for d in bf:
		if isinstance(d, Land):
			if d.name in lands:
				continue
			lands_st+=str(len([c for c in bf if c.name == d.name])) 
			lands_st += 'x ' + str(d) + '\n'
			lands.append(d.name)
			continue
		if d.name in cards:
			continue
		st += str(len([c for c in bf if c.name == d.name])) + 'x '
		st += str(d) + '\n'
		cards.append(d.name)
	st += lands_st
	print st
