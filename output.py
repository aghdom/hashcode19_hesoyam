with open('output.txt', 'w+') as file:
    individual = ga.best_individual()[1]
    file.write(f'{len(individual)}\n')
    for slide in individual:
        if len(slide) == 2:
            file.write(f'{slide[0]} {slide[1]}\n')
        else:
            file.write(f'{slide[0]}')
