import math
def divide_grid(N):
    region_size = int(20 / math.sqrt(N))
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


l = divide_grid()

for each in l:
    print(each)
    print("================================")