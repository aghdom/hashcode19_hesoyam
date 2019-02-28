import random


def get_mutate_function(v_pics, h_pics, swap_prob, add_prob):

    def mutate(slides):
        def is_possible(percentage):
            return random.randint(0, 100) <= percentage

        # mutate by swapping two genes
        if is_possible(swap_prob):
            r = len(slides) - 1
            x = random.randint(0, r)
            y = random.randint(0, r)
            if x != y:
                c = slides[x].copy()
                slides[x] = slides[y].copy()
                slides[y] = c
        if is_possible(add_prob):
            slide_h_pics = set()
            slide_v_pics = set()
            for slide in slides:
                if len(slide) == 1:
                    slide_h_pics.add(slide[0])
                else:
                    slide_v_pics.add(slide[0])
                    slide_v_pics.add(slide[1])
            pics_v_diff = set(v_pics) - set(slide_v_pics)
            pics_h_diff = set(h_pics) - set(slide_h_pics)
            if is_possible(50) and len(pics_v_diff) > 1:
                slides.extend(random.sample(pics_v_diff, 2))
            elif len(pics_v_diff) > 0:
                slides.extend(random.sample(pics_h_diff, 1))
        return slides

    return mutate
