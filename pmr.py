import os
import sys
import choix
import random

def pmr(ranks, n_sim=1000):
    # ranks is a dictionary that includes each rankers ranking
    # rankers are enumerated from 1 to m 
    # the items are enumerated from 0 to n
    items = set(ranks[1])
    
    data = []
    for s in range(n_sim):
        l = random.sample(list(rank.keys()),k=1)
        el = random.sample(rank[l[0]],k=2)
        if rank[l[0]].index(el[0]) < rank[l[0]].index(el[1]):
            data.append((el[0],el[1]))
        else:
            data.append((el[1],el[0]))
    skills = choix.ilsr_pairwise(len(items), data, alpha=0.01)
    return skills



