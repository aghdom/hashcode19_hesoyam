from rohlik import evaluate

# import random
# from deap import tools, base, creator
#
# IND_SIZE = 10
#
# toolbox = base.Toolbox()
# toolbox.register("attribute", random.random)
# # toolbox.register("individual", tools.initRepeat, creator.Individual,
#                  toolbox.attribute, n=IND_SIZE)
# # toolbox.register("population", tools.initRepeat, list, toolbox.individual)
#
#
# def evaluate(individual):
#     return sum(individual),
#
#
# toolbox.register("mate", tools.cxTwoPoint)
# toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
# toolbox.register("select", tools.selTournament, tournsize=3)
# toolbox.register("evaluate", evaluate)
#
#
# def main():
#     # pop = toolbox.population(n=50)
#     cxpb, mutpb, ngen = 0.5, 0.2, 40
#
#     # Evaluate the entire population
#     # fitnesses = map(toolbox.evaluate, pop)
#     for ind, fit in zip(pop, fitnesses):
#         ind.fitness.values = fit
#
#     for g in range(ngen):
#         # Select the next generation individuals
#         # offspring = toolbox.select(pop, len(pop))
#         # Clone the selected individuals
#         # offspring = map(toolbox.clone, offspring)
#
#         # Apply crossover and mutation on the offspring
#         for child1, child2 in zip(offspring[::2], offspring[1::2]):
#             if random.random() < cxpb:
#                 # toolbox.mate(child1, child2)
#                 del child1.fitness.values
#                 del child2.fitness.values
#
#         for mutant in offspring:
#             if random.random() < mutpb:
#                 toolbox.mutate(mutant)
#                 del mutant.fitness.values
#
#         # Evaluate the individuals with an invalid fitness
#         invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
#         fitnesses = map(toolbox.evaluate, invalid_ind)
#         for ind, fit in zip(invalid_ind, fitnesses):
#             ind.fitness.values = fit
#
#         # The population is entirely replaced by the offspring
#         pop[:] = offspring
#
#     return pop
import random
from itertools import zip_longest
from copy import deepcopy


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def generate_population(picture_list: list, population: list, pop_size: int):
    population = deepcopy(population)
    v_len = 0
    h_len = 0
    v_pics = []
    h_pics = []
    for index, pic in enumerate(picture_list):
        if pic['type'] == 'V':
            v_len += 1
            v_pics.append(index)
        else:
            h_len += 1
            h_pics.append(index)
    for i in range(pop_size):
        individual = []
        random.shuffle(v_pics)
        for pic1, pic2 in grouper(v_pics, 2):
            individual.append([pic1, pic2])
        print(individual)
        for pic in h_pics:
            individual.append([pic])
        random.shuffle(individual)
        population.append(individual)
    return population


if __name__ == '__main__':
    pictures = []
    with open('data/a_example.txt') as f:
        f.readline()
        for line in f.readlines():
            parsed_line = line.split(' ')
            tags = parsed_line[2:]
            tags[-1] = tags[-1].strip('\n')
            tags = set(tags)
            pictures.append({'type': parsed_line[0], 'tags': tags})
    for pic in pictures:
        print(pic)
    population = []
    population = generate_population(pictures, population, 10)
    # main()
