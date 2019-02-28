def get_tags(slide, pics):
    if len(slide) == 1:
        return pics[slide[0]]['tags']
    else:
        return pics[slide[0]]['tags'] | pics[slide[1]]['tags']



def evaluate(individual, pics):
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


ind = [
    [0],
    [1,2],
    [3],

]

pics = [
    {
        'type': 'H',
        'tags': set(['a','b','c'])
    },
    {
        'type': 'V',
        'tags': set(['a','b'])
    },
    {
        'type': 'V',
        'tags': set(['b','d'])
    },
    {
        'type': 'H',
        'tags': set(['d','e','c'])
    }
]



evaluate(ind, pics)