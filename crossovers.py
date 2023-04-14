import random

def uniform_crossover(parent1, parent2):
    #parent1: first parent
    #parent2: second parent
    #return: child
    #initialize child
    child1 = []
    child2= []
    #iterate through genes
    for i in range(len(parent1)):
        #select parent
        p = random.randint(0, 1)
        #add gene
        child1.append(parent1[i] if p == 0 else parent2[i])
        child2.append(parent1[i]if p == 1 else parent2[i])
    #return child
    return child1, child2

def single_point_crossover(parent1, parent2):
    #parent1: first parent
    #parent2: second parent
    #return: child
    #initialize child
    child = []
    #select crossover point
    point = random.randint(1, len(parent1)-1)
    #add genes
    child.extend(parent1[:point])
    child.extend(parent2[point:])
    # #return child
    # for i in range(len(child)):
    #     child[i] = str(child[i])

    return child

def two_point_crossover(parent1, parent2):
    #parent1: first parent
    #parent2: second parent
    #return: child
    #initialize child
    child1 = []
    child2 = []
    #select crossover points
    point1 = random.randint(1, len(parent1)-2)
    point2 = random.randint(point1+1, len(parent1)-1)
    #add genes
    child1.extend(parent1[:point1])
    child1.extend(parent2[point1:point2])
    child1.extend(parent1[point2:])

    child2.extend(parent2[:point1])
    child2.extend(parent1[point1:point2])
    child2.extend(parent2[point2:])


    #return child
    return child1, child2
