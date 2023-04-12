import divide_regions
import function
import openfile
import random

def unique_random_list(length, start, end):
    """
    Generates a list of unique random integers within a given range.

    Args:
        length (int): The length of the list to generate.
        start (int): The start of the range (inclusive).
        end (int): The end of the range (exclusive).

    Returns:
        A list of unique random integers.
    """
    if length > end - start:
        raise ValueError("Cannot generate unique list of length greater than range.")
    nums = set()
    while len(nums) < length:
        nums.add(random.randint(start, end-1))
    return list(nums)
    

for i in range(1,401):
    #l = unique_random_list(10, 1, 401)
    blocks_population,_ = openfile.read_files()

    region_towers = divide_regions.set_tower_locations(i, blocks_population)

   

