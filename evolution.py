import divide_regions
import openfile
import random
import numpy as np
from function import unique_random_list,assign_blocks,calulacte_conv_block_tower \
                    ,calculate_satisfaction, esitimate_bound_for_Towerlist
import crossovers, mutations
import matplotlib.pyplot as plt

max_bound = 800000
P_mut = 0.1
P_cro = 0.9
number_of_chromosome = 50
# number of calculated chromosome
with_calculation = 30
# number of random chromosome 
without_calculation = 50 - with_calculation

# read files
blocks_population,_ = openfile.read_files()
conv,distance = calulacte_conv_block_tower()

number_of_approach = 200

cut_range = 5 # used in best_bound_for_chromosome

def best_bound_for_chromosome(chromosome:list, assign_dict , each_tower_population , distance):
    best_statisfaction = -100
    best_chromosome_bound = []
    step = max_bound//cut_range
    for i in range(step, max_bound, step):
        total_bound_for_this_chromosome = random.randint(i, i+step)
        bound_chromosome = esitimate_bound_for_Towerlist(chromosome, assign_dict, \
                                                                each_tower_population, distance, total_bound_for_this_chromosome)
        bandwidth_towers = dict(zip(chromosome, bound_chromosome))
        new_satisfaction = calculate_satisfaction(assign_dict,each_tower_population,bandwidth_towers)
        if best_statisfaction < new_satisfaction :
            best_statisfaction = new_satisfaction
            best_chromosome_bound = bound_chromosome

    return best_statisfaction,best_chromosome_bound
        
    
def find_weighted_keys(sorted_fitness: dict):
    weighted_keys = []
    for key, value in sorted_fitness.items():
        weighted_keys.extend([key] * int(value))
    return weighted_keys

final_chromosomes = []
final_bandwidth = []
final_fitness = []

for i in range(3, 401):
    # region_towers -> list 30*i
    region_towers = divide_regions.set_tower_locations(i, blocks_population, with_calculation)

    for j in range(without_calculation):
        region_towers.append(unique_random_list(i, 0, 400))

    fitness = {}
    bandwidth = []

    for k in range(0,len(region_towers)):
        
        assign_dict, each_tower_population = assign_blocks(distance,region_towers[k])
        fitness[k], bandwidth_k = best_bound_for_chromosome(region_towers[k],assign_dict,each_tower_population,distance)
        sorted_fitness = dict(sorted(fitness.items(), key=lambda x: x[1], reverse=True))
        bandwidth.append(bandwidth_k)
    
    x_axis = []
    y_axis = []
    for eproch in range(number_of_approach):
        x_axis.append(eproch)
        # sort fitnesses of chromosome list
        
        sorted_fitness = dict(sorted(sorted_fitness.items(), key=lambda x: x[1], reverse=True))
        new_region_tower = []
        new_sorted_fitness = {}
        new_bandwidth = []
        
        #print(list(sorted_fitness.keys())[:50])
        for each in list(sorted_fitness.keys())[:50]:
            new_region_tower.append(region_towers[each])
        region_towers.clear()
        region_towers = new_region_tower.copy()

        for each in list(sorted_fitness.keys())[:50]:
            new_bandwidth.append(bandwidth[each])
        bandwidth.clear()
        bandwidth = new_bandwidth.copy()

        l = [x for x in range(50)]
        # new_sorted_fitness = list(sorted_fitness.values())[:50]
        new_sorted_fitness = dict(zip(l, list(sorted_fitness.values())[:50]))
        sorted_fitness.clear()
        sorted_fitness = new_sorted_fitness.copy()
        y_axis.append(list(sorted_fitness.values())[0])
        
        if eproch == number_of_approach - 1:
            final_chromosomes.append(region_towers[0])
            final_bandwidth.append(bandwidth[0])
            final_fitness.append(sorted_fitness[list(sorted_fitness.keys())[0]])
        
        for _ in range(number_of_chromosome):
            weighted_keys = find_weighted_keys(sorted_fitness)
            # pick parents
            parent1 = np.random.choice(weighted_keys)
            parent2 = np.random.choice(weighted_keys)
            while parent1 == parent2:
                parent1 = np.random.choice(weighted_keys)
                parent2 = np.random.choice(weighted_keys)

            # get new childs with crossovers
            child1, child2 = crossovers.uniform_crossover(region_towers[parent1], region_towers[parent2])
            child3, child4 = crossovers.two_point_crossover(region_towers[parent1], region_towers[parent2])

            # assign_blocks for new childs
            assign_blocks_child1, tower_population_child1 = assign_blocks(distance, child1)
            assign_blocks_child2, tower_population_child2 = assign_blocks(distance, child2)
            assign_blocks_child3, tower_population_child3 = assign_blocks(distance, child3)
            assign_blocks_child4, tower_population_child4 = assign_blocks(distance, child4)

            # calculate satisfaction for new childs
            h = len(region_towers)
        
            sorted_fitness[h],bandwdith_child1 = best_bound_for_chromosome(child1, assign_blocks_child1, tower_population_child1, distance)
            sorted_fitness[h+1],bandwdith_child2 = best_bound_for_chromosome(child2, assign_blocks_child2, tower_population_child2, distance)
            sorted_fitness[h+2],bandwdith_child3 = best_bound_for_chromosome(child3, assign_blocks_child3, tower_population_child3, distance)
            sorted_fitness[h+3],bandwdith_child4 = best_bound_for_chromosome(child4, assign_blocks_child4, tower_population_child4, distance)

            # update our chromosome list with new childs
            region_towers.append(child1)
            region_towers.append(child2)
            region_towers.append(child3)
            region_towers.append(child4)

            # update bandwidth
            bandwidth.append(bandwdith_child1)
            bandwidth.append(bandwdith_child2)
            bandwidth.append(bandwdith_child3)
            bandwidth.append(bandwdith_child4)
            
            # update k after apending the 4 childs to region_towers
            h += 4

            if random.random() < P_mut:
                child1 = mutations.creep_mutation(child1)
                child2 = mutations.creep_mutation(child2)
                child3 = mutations.creep_mutation(child3)
                child4 = mutations.creep_mutation(child4)

plt.plot(x_axis,y_axis,linestyle = 'solid')
plt.show()