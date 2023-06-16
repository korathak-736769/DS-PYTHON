import random
x = random.random() # 0.0 - 1.0
# print(x)

# random_uniform()
x = random.uniform(1,10) # 1 <= x < 10
print("random_uniform : ",x) 

# random_randrange()
for i in range(15):
    x = random.randrange(1,10,2)
    print("random_randrange : ",x) 

# random_randint()
x = random.randint(1,10)
print("random_randint : ",x)

# random_list
items = [1,2,3,"a","b","c"]
x = random.choice(items)
print("random.choice : ",x)

# switch_positions_list (variablr : items)
x = random.shuffle(items)
print(items)

# random.choice_short
x = random.choice([1,2,3,"a","b","c"])
print("random.choice_short : ",x)

