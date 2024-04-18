import pmr

rank = {1:[1,2,3,4,0], 2: [3,4,0,2,1], 3: [2,0,4,3,1]}

skills = pmr(rank,n_sim=100000)

print("Item\tScore")
print("=====================")
for i in range(len(items)):
	print(i,"\t",skills[i])
