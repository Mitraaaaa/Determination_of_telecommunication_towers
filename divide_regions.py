import math
import numpy
def divide_grid(N , dp_squares : list):
    # N is the number of regions U want to split your area, * it's not the lines of division
    N = math.sqrt(dp_squares[N])
    print(N)
    region_size = math.ceil(20/N)
    print(region_size)
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
        density += population_size[i]
    return density

def set_tower_locations(size_of_towers, population_size):
    region_list = divide_grid(size_of_towers+1)
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
    
    regions_tower = np.random.choice(values,size=size_of_towers,p = probs)
    print(regions_tower)

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

dp_squares = find_closest_square()

l = divide_grid(80, dp_squares)

set_tower_locations()
