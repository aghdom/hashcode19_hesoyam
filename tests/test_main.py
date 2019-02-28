from main import generate_population
from rohlik import evaluate

def test_generate_population():
    picture = [
        {'type': 'V'},
        {'type': 'V'},
        {'type': 'V'},
        {'type': 'V'},
        {'type': 'V'},
        {'type': 'V'},
    ]

    population = generate_population(picture, [], 100)
    for individual in population:
        for id, _ in enumerate(picture):
            count = 0
            for slide in population:
                for pic in slide:
                    if pic == id:
                        count += 1
            assert count in [0, 1]


def test_evaluate():
    ind = [
        [0],
        [1, 2],
        [3],

    ]

    pics = [
        {
            'type': 'H',
            'tags': set(['a', 'b', 'c'])
        },
        {
            'type': 'V',
            'tags': set(['a', 'b'])
        },
        {
            'type': 'V',
            'tags': set(['b', 'd'])
        },
        {
            'type': 'H',
            'tags': set(['d', 'e', 'c'])
        }
    ]
    score = evaluate(ind,pics)
    assert(score == 3)
