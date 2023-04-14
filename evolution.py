import divide_regions
import openfile
import random
import numpy as np
from function import unique_random_list,estimate_max_bound_for_eachTower,assign_blocks,calulacte_conv_block_tower \
                    ,calculate_satisfaction
import crossovers 


class Chromosome:
    def __init__(self, towers: list, assign_dict: dict, fitness, each_tower_population: list):
        self.towers = towers
        self.assign_dict = assign_dict
        self.fitness = fitness
        self.each_tower_population = each_tower_population


class Tower:
    def __init__(self, bandwidth, id):
        self.bandwidth = bandwidth
        self.id = id
        
def make_classes(region_towers):
    l = []
    for cnt in range(len(region_towers)):
        temp = []
        for tower in region_towers[cnt]:
            t = Tower(bandwidth = 0, id = tower)
            temp.append(t)
        l.append(temp)
    return l

def make_chromosome(list_of_towers: list):
    l = []
    for each_list in list_of_towers:
        chromosome = Chromosome(towers = each_list, assign_dict = None, \
                                fitness = 0, each_tower_population = 0)
        l.append(chromosome)
    return l


def normalize_fitness(fitness):
    cnt = len(fitness)
    for i in fitness:
        fitness[i] = cnt
        cnt -= 1

def find_weighted_keys(sorted_fitness: dict):
    weighted_keys = []
    for key, value in sorted_fitness.items():
        weighted_keys.extend([key] * value)
    return weighted_keys

def make_bandwidth_towers(individual: Chromosome):
    bandwidth_towers = {}
    for tower in individual.towers:
        bandwidth_towers[tower.id] = tower.bandwidth
    return bandwidth_towers

def make_fitness(individuals: list):
    fitness = {}
    for cnt in range(len(individuals)):
        fitness[cnt] = individuals[cnt].fitness
    return fitness

def make_id_list(towers_list: list):
    id = []
    for tower in towers_list:
        id.append(tower.id)
    return id

with_calculation = 5
without_calculation = 50 - with_calculation

blocks_population,_ = openfile.read_files()
conv,distance = calulacte_conv_block_tower()

number_eproch = 5

for i in range(3,4):
    # region_towers -> list 30*i
    region_towers = divide_regions.set_tower_locations(i, blocks_population, with_calculation)

    # for j in range(without_calculation):
    #     region_towers.append(unique_random_list(i, 0, 400))

    individual = make_classes(region_towers)
    individual = make_chromosome(individual)

    
    # fitness = {}

    # for k in range(0,len(region_towers)):
        
    #     assign_dict, each_tower_population = assign_blocks(distance,region_towers[k],blocks_population)
    #     # print(assign_dict)
    #     bandwidth_towers = {}
        
    #     for towerId in region_towers[k]:
    #         max_bound_towerId = estimate_max_bound_for_eachTower(towerId,assign_dict,each_tower_population,distance)
    #         bound_towerId = random.randint(1,max_bound_towerId)
    #         # print(bound_towerId)
    #         bandwidth_towers[towerId] = bound_towerId    
    #         # print(max_bound_towerId)
            
    #     fitness[k] = calculate_satisfaction(assign_dict, each_tower_population, bandwidth_towers)        
    #     sorted_fitness = dict(sorted(fitness.items(), key=lambda x: x[1], reverse=True))

    #------------------------------------------------------------------------------------------------------------------#
    for k in range(len(individual)):
        assign_dict, each_tower_population = assign_blocks(distance, make_id_list(individual[k].towers), blocks_population)
        individual[k].assign_dict = assign_dict
        individual[k].each_tower_population = each_tower_population

        for each_tower in individual[k].towers:
            max_bound_each_tower = estimate_max_bound_for_eachTower(each_tower.id, individual[k].assign_dict \
                                                                , individual[k].each_tower_population, distance)
            bound_tower = random.randint(1, max_bound_each_tower)
            each_tower.bandwidth = bound_tower
        bandwidth_towers = make_bandwidth_towers(individual[k])
        fitness = calculate_satisfaction(individual[k].assign_dict, individual[k].each_tower_population, bandwidth_towers)
        individual[k].fitness = fitness
    fitness = make_fitness(individual)
    sorted_fitness = dict(sorted(fitness.items(), key=lambda x: x[1], reverse=True))
    normalize_fitness(sorted_fitness)

    for eproch in range(number_eproch):
        weighted_keys = find_weighted_keys(sorted_fitness)

        parent1 = np.random.choice(weighted_keys)
        parent2 = np.random.choice(weighted_keys)
        if parent1 == parent2: continue

        child = crossovers.uniform_crossover(individual[parent1].towers, individual[parent2].towers)

        # make a new chromosome
        new_assign_dict, new_each_tower_population = assign_blocks(distance, make_id_list(child), blocks_population)
        chrom = Chromosome(towers = child, assign_dict= new_assign_dict, fitness= None, \
                            each_tower_population = new_each_tower_population)
        
        individual.append(chrom)

        print(child)
    #------------------------------------------------------------------------------------------------------------------#
    
    # # normalize the fittness
    # normalize_fitness(sorted_fitness)

    # # weighted_keys = []
    # # for key, value in sorted_fitness.items():
    # #     weighted_keys.extend([key] * value)
    
    # for eproch in range(number_eproch):
    #     weighted_keys = find_weighted_keys(sorted_fitness)

    #     parent1 = np.random.choice(weighted_keys)
    #     parent2 = np.random.choice(weighted_keys)
    #     if parent1 == parent2: continue

    #     child = crossovers.uniform_crossover(region_towers[parent1], region_towers[parent2])

    #     print(child)
    

