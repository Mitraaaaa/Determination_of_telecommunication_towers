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

print(len(l))
for each in l:
    print(each)
    print("================================")