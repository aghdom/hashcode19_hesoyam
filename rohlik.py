def get_tags(slide, pics):
    if len(slide) == 1:
        return pics[slide[0]]['tags']
    else:
        return pics[slide[0]]['tags'] | pics[slide[1]]['tags']



def evaluate(individual, pics):
    if len(individual) <= 1:
        return 0
    score = 0
    prev_tags = get_tags(individual[0], pics)
    for slide in individual[1:]:
        cur_tags = get_tags(slide, pics)
        common = prev_tags | cur_tags
        only_in_prev = prev_tags - cur_tags
        only_in_cur = cur_tags - prev_tags
        score += min(len(common), len(only_in_prev), len(only_in_cur))
        prev_tags = cur_tags
    return score
