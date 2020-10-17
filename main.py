import argparse
import pickle
from pathlib import Path
from sys import stdin, stderr

from src.check import PlagiarismChecker
from src.make_index import Index
from src.tabulate import tabulate

THRESHOLD = 0.6


def gen_index(args):
    p = Path(args.index)
    if not p.is_dir():
        print("Index path must be a directory containing the corpus files!", file=stderr)
        exit(1)
    index = Index()
    for file_path in p.iterdir():
        if not file_path.is_file():
            continue
        with open(file_path, 'r', encoding='unicode_escape') as file:
            contents = file.read()
            index.add_doc(file_path, contents)
    index.normalize_docs()
    with open('index.pk', 'wb+') as f:
        pickle.dump(index, f)
    print('Index generated in index.pk')


def check_for_plagiarism(args):
    contents = {}
    if args.file == '-':
        contents['stdin'] = stdin.read()
    else:
        p = Path(args.file)
        if p.is_file():
            with open(p, 'r', encoding='unicode_escape') as file:
                contents[file] = file.read()
        elif p.is_dir():
            for file in p.iterdir():
                if not file.is_file():
                    continue
                with open(file, 'r', encoding='unicode_escape') as f:
                    contents[file] = f.read()
    with open('index.pk', 'rb') as f:
        index = pickle.load(f)
    checker = PlagiarismChecker(index)
    data = {}
    for file, contents in contents.items():
        scores = checker.find_score(contents)
        data[file] = sorted([(original, score) for original, score in scores.items() if score > THRESHOLD],
                            reverse=True, key=lambda x: x[1])
    tabulate(data)


def main():
    parser = argparse.ArgumentParser(description='Check for plagiarism in your documents')
    commands = parser.add_subparsers(required=True)

    query = commands.add_parser('query', help='Check file for plagiarism')
    query.add_argument('file', type=str, help='Check this file (or all files in this folder)')
    query.set_defaults(func=check_for_plagiarism)

    index = commands.add_parser('index', help='Make index')
    index.add_argument('index', type=str, help='Index this directory')
    index.set_defaults(func=gen_index)

    args = parser.parse_args()
    args.func(args)


main()
