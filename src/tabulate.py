from typing import List, Tuple, Dict
from pathlib import Path

HEADER = ['Query Document', 'Original', 'Score']


def print_header():
    print('+--------------------------------+----------------------+-------+')
    print('| Query Document                 |             Original | Score |')
    print('+================================+======================+=======+')


def print_row(doc: Path, originals: List[Tuple[Path, float]]):
    doc = doc.name
    if not originals:
        print(f'| {doc:30} | {" " * 20} | {" " * 5} |')
    else:
        (original_file, score) = originals[0]
        print(f'| {doc:30} | {original_file.name:>20} | {score:5.2f} |')
        for orig, score in originals[1:]:
            print(f'| {" " * 30} | {orig.name:>20} | {score:5.2f} |')
    print('+--------------------------------+----------------------+-------+')


def tabulate(data: Dict[Path, List[Tuple[Path, float]]]):
    print_header()
    for doc, docs in data.items():
        print_row(doc, docs)
