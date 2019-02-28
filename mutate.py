import random


def mutate(slides):
    def is_possible(percentage):
        return random.randint(0, 100) <= percentage

    # mutate by swapping two genes
    if (is_possible(50)):
        r = len(slides) - 1
        x = random.randint(0, r)
        y = random.randint(0, r)
        if x != y:
            c = slides[x].copy()
            slides[x] = slides[y].copy()
            slides[y] = c

    # pridanie noveho slajdu???

    return slides