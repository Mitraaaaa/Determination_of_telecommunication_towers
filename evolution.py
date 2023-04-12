import divide_regions
import function
import openfile
import random

with_calculation = 30
without_calculation = 50 - with_calculation

blocks_population,_ = openfile.read_files()

for i in range(1,401):
    #l = unique_random_list(10, 1, 401)

    # region_towers -> list 30*i
    region_towers = divide_regions.set_tower_locations(i, blocks_population, with_calculation)

    # to-do
        # bound -> 0 and max bound
