import numpy as np
from math import exp,floor

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
    # 
    x = location//20
    y = location % 20
    return [x,y]

def find_next_number():
    pass



def manhattan_distance(point1, point2):
    # Calculate the absolute difference between the x-coordinates and y-coordinates
    x_diff = abs(point1[0] - point2[0])
    y_diff = abs(point1[1] - point2[1])

    # Return the sum of the absolute differences
    return x_diff + y_diff

def calulacte_conv_block_tower():
    dp = list() #conv
    dp2 = list() # Distance
    for i in range(400): #Tower location
        tower_coordinate = calculate_coordinates(i)
        each_list = list()
        each_dp_2 = list()
        for j in range(400): #Blocks location
            block_coordinate = calculate_coordinates(j)
            each_list.append(conv(block_coordinate, tower_coordinate))
            each_dp_2.append(manhattan_distance(tower_coordinate, block_coordinate))
        dp.append(each_list)
        dp2.append(each_dp_2)
    return dp,dp2

def assign_blocks(distance, tower_coordination):
    assign_dict = dict()
    for each in tower_coordination:
        id_coordinate = each[0]*20 + each[1]
        assign_dict[id_coordinate] = list()
    for i in range(400): #Blocks location
        min_d = 1e10
        min_id = None
        for each in tower_coordination:
            id_coordinate = each[0]*20 + each[1]
            if distance[i][id_coordinate] < min_d:
                min_d = distance[i][id_coordinate]
                min_id = id_coordinate
        assign_dict[min_id].append(i)
    return assign_dict

dp = calulacte_conv_block_tower()
