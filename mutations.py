import random
def bit_fip_mutation(individual, pmut=0.1):
    #individual: individual
    #pmut: probability of mutation
    #return: mutated individual
    #iterate through genes
    for i in range(len(individual)):
        if random.random() < pmut:
            #flip gene
            individual[i] = (individual[i] + 1) % 2
    #return individual
    return individual

def creep_mutation(individual, step=4, P_CREEP=0.3):
    outoutTemp = []
    for i in range(len(individual)):
        each = individual[i]
        if random.random() < P_CREEP:
            #mutate gene
            temp = each
            each = ((int(individual[i]) + random.randint(-step, step)) % 10)
            if 0<=each<=399:       
                outoutTemp.append(each)
            else:
                outoutTemp.append(individual[i])
    #return individual
    return outoutTemp

