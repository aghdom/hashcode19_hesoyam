from main import generate_population


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
