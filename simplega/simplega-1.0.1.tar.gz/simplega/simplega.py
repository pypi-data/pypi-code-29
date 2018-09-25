from random import choice, random

# Chromosome
class Chromosome():
	"""A Chromosome corresponds to a candidate solution. 
	Its DNA is a collection of genes, which is the representation of each variable of the problem.
	Fitness is the measure of how well the candidate solution is suited to solve the problem."""
	def __init__(self, dna):
		self._dna = dna
		self._fitness = 0
		self._weighted_fitness = 0.0
		self._cumulative_weight = 0.0

	def __repr__(self):
		return f"DNA: {self._dna}, Fitness: {self._fitness}"

	def __eq__(self, other):
		if not type(other) == type(self): raise TypeError("Must be compared woth other instance of Chromosome class")
		return self.dna == other.dna

	def mutate(self, genes, mutation_rate = 0.01):
		"""Change the chromosome`s dna, replacing a random gene based on a given probability."""
		new_dna = []
		for gene in self._dna:
			new_dna.append(choice(genes) if random() <= mutation_rate else gene)
		return Chromosome("".join(new_dna))

	@classmethod
	def generate_random(cls, genes, size):
		"""Generate a random chromosome with a given size based on the availables genes."""
		return cls("".join([ choice(genes) for _ in range(size) ]))

	@classmethod
	def crossover(cls, chsome, crsome, crossover_points = 1):
		"""Mix two chromosomes, generatins two new chromosomes from the combination.
		Use crossover_points to specify in how many parts each chromosome will be sliced."""
		ch_g = Chromosome.chromosome_generator(chsome, crsome)
		cr_g = Chromosome.chromosome_generator(crsome, chsome)
		points = Chromosome.crossover_points_generator(crossover_points, len(chsome.dna))
		ch = ""
		cr = ""
		for _ in range(crossover_points + 1):
			l, u = next(points)
			ch += next(ch_g).dna[l:u]
			cr += next(cr_g).dna[l:u]
		return Chromosome(ch), Chromosome(cr)

	@classmethod
	def chromosome_generator(cls, ch, cr): 
		"""Generator to alternate between two chromosomes."""
		t = True
		while True:
			yield ch if t else cr
			t = not(t)

	@classmethod
	def crossover_points_generator(cls, number, size):
		"""Generator to yield the lower and upper limits of each slice."""
		l = []
		while len(l) < number:
			r = choice(range(1, size - 1))
			if not r in l: l.append(r)
		l.sort()
		l.insert(0, 0)
		l.append(size)
		points = list(zip(l, l[1:]))
		for p in points:
			yield p[0], p[1]

	@property
	def dna(self):
		"""Chromosome`s dna."""
		return self._dna

	@property
	def fitness(self):
		"""Chromosome`s fitness."""
		return self._fitness

	@fitness.setter
	def fitness(self, value):
		self._fitness = value

	@property
	def weighted_fitness(self):
		"""Chromosome`s weighted fitness, considering its fitness among the population."""
		return self._weighted_fitness

	@weighted_fitness.setter
	def weighted_fitness(self, value):
		self._weighted_fitness = value

	@property
	def cumulative_weight(self):
		"""Sum of weighted fitness, from chromosome`s position to the last chromosome. Base for roulette wheel selection."""
		return self._cumulative_weight

	@cumulative_weight.setter
	def cumulative_weight(self, value):
		self._cumulative_weight = value

# Population
class Population(): 
	"""Population is a collection candidate solutions (chromosomes)."""
	def __init__(self, population):
		self._population = population

	def __repr__(self):
		return "\n".join([ str(chromosome) for chromosome in self._population ])

	@classmethod
	def generate_random(cls, pop_size, genes, ind_size):
		"""Generate a population, with random chromosomes based on their genes and size."""
		return cls([ Chromosome.generate_random(genes, ind_size) for _ in range(pop_size) ])

	def evaluate_with(self, fitness_func):
		"""Evaluate all chromosomes with a given fitness function."""
		for chromosome in self._population:
			chromosome.fitness = fitness_func(chromosome)

	def sum_population_fitness(self):
		"""Sum the fitness of all chromosomes."""
		self._population_fitness = sum([ c.fitness for c in self._population ])

	def sort_by_fitness(self):
		"""Sort by fitness."""
		self._population.sort(key=lambda c: c.fitness, reverse=True)

	def calculate_weight_fitness(self):
		"""Calculate the weighted fitness of all chromosomes, based on the sum of all chromosomes fitness."""
		for chromosome in self._population:
			chromosome.weighted_fitness = chromosome.fitness / self._population_fitness

	def calculate_cumulative_weight(self):
		"""Calculate the cumulative weight of a chromosome, where the fittest chromosome has the cumulative weight of 1 and the less fit has the cumulative weight equal to its weighted fitness."""
		for i in range(len(self._population)):
			self._population[i].cumulative_weight = sum( [ chromosome.weighted_fitness for chromosome in self._population[i:] ] )

	def select(self):
		"""Roulette wheel selection."""
		r = random()
		for x in range(1, len(self._population)):
			if self._population[x].cumulative_weight < r:
				return self._population[x - 1]
		return self._population[len(self._population) - 1]

	def select_pair(self):
		"""Select a pair of chromosomes. Return two non-equal chromosomes."""
		c1 = self.select()
		while True:
			c2 = self.select()
			if not c1 == c2: break
		return c1, c2

	@property
	def chromosomes(self):
		"""List of chromosomes in a population."""
		return self._population

class GAHelper():
	"""Helper class with useful functions."""
	@classmethod
	def chunckdna_generator(cls, chromosome, num_col): 
		"""Split a chromosome`s dna based on a defined number of genes per line, generating a matrix (n x num_col).
		Outputs a generator.
		See https://stackoverflow.com/questions/18854620"""
		return (chromosome.dna[0+i:num_col+i] for i in range(0, len(chromosome.dna), num_col))

	@classmethod
	def chunckdna(cls, chromosome, num_col): 
		"""Return a list from GAHelper.chunckdna_generator."""
		return list(GAHelper.chunckdna_generator(chromosome, num_col))

	@classmethod
	def print_as_matrix(cls, chromosome, num_col):
		"""Print chromosome`s dna as a matrix, limiting the number of columns."""
		print("".join([ l + "\n" for l in GAHelper.chunckdna_generator(chromosome, num_col) ])[:-1])
		

	@classmethod
	def get_column(cls, chromosome, column, num_col): 
		"""Return the genes of a given column, considering the matrix from the chromosome`s dna."""
		if column >= num_col: raise ValueError("Chromosome doesn`t have this much columns.")
		return "".join([ l[i] for i in range(column , num_col , num_col) for l in GAHelper.chunckdna(chromosome, num_col) ])

	@classmethod
	def get_row(cls, chromosome, row, num_col): 
		"""Return the genes of a given row, considering the matrix from the chromosome`s dna."""
		if row > (len(chromosome.dna) // num_col) - 1: raise ValueError("Chromosome doesn`t have this much rows.")
		return GAHelper.chunckdna(chromosome, num_col)[row]


class GA(): 
	"""Perform genetic algorithm. 
	Provide a fitnesst function as first parameter.
	Optional parameters and its default values include:
	genes = A-Z
	chromosome_size = 10
	population_size = 100
	generations = 100
	crossover_points = 1
	elitism_rate = 0.05
	crossover_rate = 0.85
	mutation_rate = 0.01
	"""
	def __init__(self, fitness_func, **kwargs):
		self._fitness_func = fitness_func
		self._fittest_chromosome = Chromosome("")
		self._genes = kwargs.get("genes", [ chr(n) for n in range(65,91) ])
		self._chromosome_size = kwargs.get("chromosome_size", 10)
		self._population_size = kwargs.get("population_size", 100)
		self._generations = kwargs.get("generations", 100)
		self._crossover_points = kwargs.get("crossover_points", 1)
		self._elitism_rate = kwargs.get("elitism_rate", 0.05)
		self._crossover_rate = kwargs.get("crossover_rate", 0.85)
		self._mutation_rate = kwargs.get("mutation_rate", 0.01)

	def get_fittest(self):
		"""Return the fittest chromosome"""
		return self._fittest_chromosome

	def run(self, verbose = False):
		"""Create initial population and iterates over the defined number of generations.
		Performs evaluation, selection, crossover and mutation for each generation."""
		population = Population.generate_random(self._population_size,self._genes, self._chromosome_size)
		for generation in range(self._generations):
			population.evaluate_with(self._fitness_func)
			population.sum_population_fitness()
			population.calculate_weight_fitness()
			population.sort_by_fitness()
			population.calculate_cumulative_weight()

			if verbose: print(f"Fittest chromosome in generation {generation} is {population.chromosomes[0]}")
			self._fittest_chromosome = population.chromosomes[0]

			new_generation = []

			# Perform elitism
			for i in range(int(self._population_size * self._elitism_rate)):
				new_generation.append(population.chromosomes[i])

			# Perform crossover
			while len(new_generation) < self._population_size:
				p1, p2 = population.select_pair()
				c1, c2 = Chromosome.crossover(p1, p2, self._crossover_points)

				# Apply crossover rate and mutation
				if random() <= self._crossover_rate:
					c1 = c1.mutate(self._genes, self._mutation_rate)
					c2 = c2.mutate(self._genes, self._mutation_rate)
					if not c1 in new_generation: new_generation.append(c1)
					if not c2 in new_generation: new_generation.append(c2)
				else:
					p1 = p1.mutate(self._genes, self._mutation_rate)
					p2 = p2.mutate(self._genes, self._mutation_rate)
					if not p1 in new_generation: new_generation.append(p1)
					if not p2 in new_generation: new_generation.append(p2)

				population = Population(new_generation)

