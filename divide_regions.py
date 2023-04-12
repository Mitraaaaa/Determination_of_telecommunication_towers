import math
import numpy
import openfile
import random

def divide_grid(N , dp_squares : list):
    # N is the number of regions U want to split your area, * it's not the lines of division
    N = math.sqrt(dp_squares[N])
    #print(N)
    region_size = math.ceil(20/N)
    #print(region_size)
    regions = []
    for i in range(0, 20, region_size):
        for j in range(0, 20, region_size):
            region = []
            for x in range(i, i+region_size):
                for y in range(j, j+region_size):
                    if x < 20 and y < 20:
                        region.append((x, y))
            regions.append(region)
    return regions

def check_density_of_blocks(region: list, population_size: list):
    density = 0
    for i in region:
        temp = i[0]*20 + i[1]
        density += population_size[temp]
    return density

def set_tower_locations(size_of_towers, population_size, iteration):
    dp_squares = find_closest_square()
    region_list = divide_grid(size_of_towers+1, dp_squares)
    density_list = []
    for i in region_list:
        density_list.append(check_density_of_blocks(i,population_size))

    probs = list()
    index = 1
    values = list()
    for i in density_list:
        probs.append(i/sum(density_list))
        values.append(index)
        index += 1

    final_result = []
    
    for iter in range(iteration):
        regions_tower = numpy.random.choice(values,size=size_of_towers,p = probs)
        final_list = []
        for x in regions_tower:
            block_list = region_list[x - 1]
            t = random.choice(block_list)
            to_append = t[0]*20 + t[1]
            final_list.append(to_append)
        final_result.append(final_list)
    return final_result


def find_closest_square():
    dp_closest_squares = numpy.zeros(401)
    for i in range(1, 21):
        dp_closest_squares[i*i] = 1

    tmp = 400
    for i in range(400, -1, -1):
        if dp_closest_squares[i] == 1:
            dp_closest_squares[i] = i
            tmp = i
        else:
            dp_closest_squares[i] = tmp
    return dp_closest_squares
