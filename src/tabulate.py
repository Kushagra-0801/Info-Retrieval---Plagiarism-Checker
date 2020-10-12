from typing import List, Tuple, Dict

HEADER = ['Query Document', 'Original', 'Score']


def print_header():
    print('+--------------------------------+----------------------+-------+')
    print('| Query Document                 |             Original | Score |')
    print('+================================+======================+=======+')


def print_row(doc: str, originals: List[Tuple[str, float]]):
    if not originals:
        print(f'| {doc:30} | {" " * 20} | {" " * 5} |')
    else:
        print(f'| {doc:30} | {originals[0][0]:>20} | {originals[0][1]:5.2f} |')
        for orig, score in originals[1:]:
            print(f'| {" " * 30} | {orig:>20} | {score:5.2f} |')
    print('+--------------------------------+----------------------+-------+')


def tabulate(data: Dict[str, List[Tuple[str, float]]]):
    print_header()
    for doc, docs in data.items():
        print_row(doc, docs)
