import random
from itertools import zip_longest
from copy import deepcopy


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def generate_population(picture_list: list, population: list, pop_size: int):
    population = deepcopy(population)
    v_pics = []
    h_pics = []
    for index, pic in enumerate(picture_list):
        if pic['type'] == 'V':
            v_pics.append(index)
        else:
            h_pics.append(index)
    for i in range(pop_size):
        individual = []
        random.shuffle(v_pics)
        for pic1, pic2 in grouper(v_pics, 2):
            individual.append([pic1, pic2])
        for pic in h_pics:
            individual.append([pic])
        random.shuffle(individual)
        population.append(individual)
    return population


def create_individual(pictures):
    individual = []
    v_pics = []
    h_pics = []
    for index, pic in enumerate(pictures):
        if pic['type'] == 'V':
            v_pics.append(index)
        else:
            h_pics.append(index)
    random.shuffle(v_pics)
    for pic1, pic2 in grouper(v_pics, 2):
        individual.append([pic1, pic2])
    for pic in h_pics:
        individual.append([pic])
    random.shuffle(individual)
    return individual


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
    v_pics = []
    h_pics = []
    for index, pic in enumerate(pictures):
        if pic['type'] == 'V':
            v_pics.append(index)
        else:
            h_pics.append(index)
    for pic in pictures:
        print(pic)
    population = []
    population = generate_population(pictures, population, 10)
