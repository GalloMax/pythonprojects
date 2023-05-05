import random

prob_sg = 0.02
prob_sgAndsg = 1
prob_sgAndNorm = 0.5
#0 is normal goat, and 1 is screaming goat

def babyChance(first, second):
    if first + second == 0:
        return 1 if random.random() <= prob_sg else 0
    elif first + second == 1:
        return 1 if random.random() <= prob_sgAndNorm else 0
    else: 
        return 1 if random.random() <= prob_sgAndsg else 0


def goatSim(start = 2, limit = 100000):

    current = [1 if random.random() <= prob_sg else 0 for i in range(start)]

    while len(current) < limit:
        random.shuffle(current)
        babies = [babyChance(current[i], current[i+1]) for i in range(0, len(current) - 1, 2)] # len(current) - 1 for when it is odd
        current.extend(babies)

    return f"Number of screaming goats: {sum(current)}. Ratio: {sum(current)}/{len(current)} = {sum(current)/len(current)}."

if __name__ == "__main__":
    print(goatSim(start = 2, limit = 100))
