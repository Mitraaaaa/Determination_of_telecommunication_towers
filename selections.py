import random

def roulette_wheel_selection(population):
    #calculate probabilities
    sum_fitness = 0
    for ind in population:
        sum_fitness += ind.fitness
    if sum_fitness == 0:
        return random.choice(population)
    probabilities = [ind.fitness/sum_fitness for ind in population]
    return random.choices(population, probabilities)[0]

def tournament_selection(population, k=3):
    #population: population
    #k: number of individuals to select
    #return: selected individual
    #select individuals
    parent1, parent2 = random.sample(population, k)
    #return best individual
    return parent1 if parent1.fitness > parent2.fitness else parent2
