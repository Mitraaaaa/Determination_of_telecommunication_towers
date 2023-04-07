import numpy as np
from math import exp,floor
import math

def conv(x_alley:list, y_d:list)->float:
    alley_loc = np.array([x_alley])
    d_loc = np.array([y_d])
    sigma = np.array([[1/8,0],[0,1/8]])
    dif_loc = alley_loc-d_loc
    dif_loc_t = dif_loc.T
    temp = np.matmul(dif_loc,sigma)
    temp2 = np.matmul(temp, dif_loc_t)
    return exp(-1/2*temp2)

def calculate_coordinates(location):
    x = location//20
    y = location % 20
    return [x,y]

# def manhattan_distance(point1, point2):
#     # Calculate the absolute difference between the x-coordinates and y-coordinates
#     x_diff = abs(point1[0] - point2[0])
#     y_diff = abs(point1[1] - point2[1])
#
#     # Return the sum of the absolute differences
#     return x_diff + y_diff

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calulacte_conv_block_tower():
    dp = list() #conv
    dp2 = list() # Distance
    for i in range(0,400): #Tower location
        tower_coordinate = calculate_coordinates(i)
        each_list = list()
        each_dp_2 = list()
        for j in range(0,400): #Blocks location
            block_coordinate = calculate_coordinates(j)
            each_list.append(conv(block_coordinate, tower_coordinate))
            each_dp_2.append(euclidean_distance(tower_coordinate, block_coordinate))
        dp.append(each_list)
        dp2.append(each_dp_2)
    return dp,dp2

def assign_blocks(distance, tower_coordination, blocks_population:list):
    # assigning eah neighbour to a tower based on weather that tower is consider closets to that neighbour
    each_tower_population = list([0 for x in range(400)]) #the indices are tower_ids and value is population assigned to that tower
    assign_dict = dict()
    for each in tower_coordination:
        id_coordinate = each[0]*20 + each[1]
        assign_dict[id_coordinate] = list()
        each_tower_population[id_coordinate] = 0

    for i in range(400): # neighbours location
        min_d = 1e10
        min_id = None
        for each in tower_coordination:
            id_coordinate = each[0]*20 + each[1]
            if distance[i][id_coordinate] < min_d:
                min_d = distance[i][id_coordinate]
                min_id = id_coordinate
        assign_dict[min_id].append(i)
        each_tower_population[min_id] += blocks_population[i]

    return assign_dict, each_tower_population

dp = calulacte_conv_block_tower()

def estimate_max_bound_for_eachTower(tower_id :int, assign_blocks :dict, each_tower_population:dict , distance):
    # tower_id = int ,  assign_blocks =map_list , each_tower_population= list
    # it's assumed that tower_id is an int could be two dimentioned by calculate_coordinates(tower_id)
    assigned_neighbour = assign_blocks[tower_id] # list of neighbours assigned to tower_id

    # init the farthest to first neighbour
    Farthest_neighbour = assigned_neighbour[0]
    max_dis = distance[tower_id][assigned_neighbour[0]]
    # calculate the Farthest neighbour to the chosen tower
    for x in assigned_neighbour:
        if distance[x][tower_id] > max_dis:
            max_dis = distance[x][tower_id]
            Farthest_neighbour = x

    max_bound_towerId = ((3* each_tower_population[tower_id])//conv(calculate_coordinates(Farthest_neighbour), calculate_coordinates(tower_id)))
    return max_bound_towerId

def calculate_satisfaction():
    pass
