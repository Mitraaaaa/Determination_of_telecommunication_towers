import divide_regions
import openfile
import random
import numpy as np
from function import unique_random_list,estimate_max_bound_for_eachTower,assign_blocks,calulacte_conv_block_tower \
                    ,calculate_satisfaction
import crossovers 


def normalize_fitness(fitness):
    cnt = len(fitness)
    for i in fitness:
        fitness[i] = cnt
        cnt -= 1

with_calculation = 5
without_calculation = 50 - with_calculation

blocks_population,_ = openfile.read_files()
conv,distance = calulacte_conv_block_tower()

for i in range(3,4):
    # region_towers -> list 30*i
    region_towers = divide_regions.set_tower_locations(i, blocks_population, with_calculation)

    # for j in range(without_calculation):
    #     region_towers.append(unique_random_list(i, 0, 400))
    
    fitness = {}

    for k in range(0,len(region_towers)):
        
        assign_dict, each_tower_population = assign_blocks(distance,region_towers[k],blocks_population)
        # print(assign_dict)
        bandwidth_towers = {}

        for towerId in region_towers[k]:
            max_bound_towerId = estimate_max_bound_for_eachTower(towerId,assign_dict,each_tower_population,distance)
            bound_towerId = random.randint(1,max_bound_towerId)
            # print(bound_towerId)
            bandwidth_towers[towerId] = bound_towerId    
            # print(max_bound_towerId)
            
        fitness[k] = calculate_satisfaction(assign_dict, each_tower_population, bandwidth_towers)
        sorted_fitness = dict(sorted(fitness.items(), key=lambda x: x[1], reverse=True))
    #--------------------------------------------------------------------------------------------------------------------#    
    
    # normalize the fittness
    normalize_fitness(sorted_fitness)    


    weighted_keys = []
    for key, value in sorted_fitness.items():
        weighted_keys.extend([key] * value)
    # print(weighted_keys)
    
    chosen_key = np.random.choice(weighted_keys)
    print(chosen_key)


