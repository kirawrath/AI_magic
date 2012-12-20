
This project goal is to output the best possible Magic the Gathering deck. Please refer to the project report for details.

You can navigate throught this code using your browser if you prefer at: https://github.com/kirawrath/AI_magic.git

This project was implemented using Python 2.7.3, before running it please verify if you have python installed, also note that Python 3.x is not backward compatible.

To run the project is very simple, you can simply type from a terminal:

python main.py

And it will run the project using the default values, you can also execute using user defined attributes. The atributes avaliable to be changed are:

	n_loops: Number of iterations the program will execute (i.e. the number of generations to be generated).
	n_decks: Number of decks in each generation.
	mutation_rate: After the crossover, the percentage that each deck will mutate by randomly exchanging some of its cards with cards in the database.
	crossover_rate: The amount (percentage) of cards that each deck will exchange with each other when ``crossovering''.

Note that the mutate and crossover rates should receive values between 0 and 1, also note that for n_loops > 10000 the software starts to take several minutes to run.

The default values are n_loops=10, n_decks=6, mutation_rate=0.15, crossover_rate=0.10, in order to set different values, this must be done via the command line (argv) and all the values should be send (i.e. the main function verify the values of the argv only if all the four parameters are defined, it uses the default values otherwise). For example, the following would be a valid call (the order of the arguments is the same as written above):

python main.py 100 10 0.10 0.05

If you want to see what is going on during the simulation, like the battles, players lives, partial score results, in the begining of the file \verb+utilities.py+ there are three flags that control the amount of output the program produces, fell free to change those boolean variables to True if you want, the output is very well formated (at least for me).

The final output of the program will be the ``winners'' decks, i.e. the decks that had the best performance accordingly to the fitness function.


