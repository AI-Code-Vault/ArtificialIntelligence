import random
import matplotlib.pyplot as plt

# Objective function: maximize f(x) = x^2
def fitness(x):
    return x**2

# Parameters
population_size = 20
chromosome_length = 10  # Binary string of length 10
generations = 10000
mutation_rate = 0.01

# Helper functions
def random_chromosome():
    return ''.join(random.choice('01') for _ in range(chromosome_length))

def decode(chromosome):
    return int(chromosome, 2)

def select(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for chrom, fit in zip(population, fitnesses):
        current += fit
        if current > pick:
            return chrom

def crossover(parent1, parent2):
    point = random.randint(1, chromosome_length - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

def mutate(chromosome):
    return ''.join(
        bit if random.random() > mutation_rate else random.choice('01')
        for bit in chromosome
    )

# Initialize population
population = [random_chromosome() for _ in range(population_size)]
best_fitness_per_gen = []

# Evolution loop
for gen in range(generations):
    decoded = [decode(chrom) for chrom in population]
    fitnesses = [fitness(x) for x in decoded]
    best_fitness_per_gen.append(max(fitnesses))
    new_population = []

    while len(new_population) < population_size:
        parent1 = select(population, fitnesses)
        parent2 = select(population, fitnesses)
        offspring1, offspring2 = crossover(parent1, parent2)
        new_population.append(mutate(offspring1))
        if len(new_population) < population_size:
            new_population.append(mutate(offspring2))

    population = new_population

# Plotting fitness over generations
plt.plot(best_fitness_per_gen)
plt.xlabel('Generation')
plt.ylabel('Best Fitness')
plt.title('Genetic Algorithm Performance')
plt.grid(True)
plt.show()

# Best solution
best_chrom = max(population, key=lambda chrom: fitness(decode(chrom)))
best_solution = decode(best_chrom)
best_value = fitness(best_solution)

print(f"Best solution: {best_solution}, Best value: {best_value}")