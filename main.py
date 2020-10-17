import argparse
import json
import pickle
from pathlib import Path, PosixPath
from sys import stdin, stderr
from typing import Any

from check import PlagiarismChecker
from make_index import Index
from tabulate import tabulate

THRESHOLD = 0.6


class PathEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, (Path, PosixPath)):
            return o.name
        return json.JSONEncoder.default(self, o)


def gen_index(args):
    p = Path(args.index)
    if not p.is_dir():
        print("Index path must be a directory containing the corpus files", file=stderr)
        exit(1)
    index = Index()
    for file in p.iterdir():
        if not file.is_file():
            continue
        contents = file.read_text()
        index.add_doc(file, contents)
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
            try:
                contents[p] = p.read_text()
            except ValueError:
                print(f'{p} is not in utf-8 encoding')
        elif p.is_dir():
            for file in p.iterdir():
                if not file.is_file():
                    continue
                try:
                    contents[file] = file.read_text()
                except ValueError:
                    print(f'{file} is not in utf-8 encoding')
    with open('index.pk', 'rb') as f:
        index = pickle.load(f)
    checker = PlagiarismChecker(index)
    data = {}
    for file, contents in contents.items():
        scores = checker.find_score(contents)
        data[file] = sorted([(original, score) for original, score in scores.items() if score > THRESHOLD],
                            reverse=True, key=lambda x: x[1])
    if args.json:
        print(json.dumps(data, cls=PathEncoder))
    elif args.table:
        tabulate(data)


def main():
    parser = argparse.ArgumentParser(description='Check for plagiarism in your documents')
    commands = parser.add_subparsers(required=True)

    query = commands.add_parser('query', help='Check file for plagiarism')
    query.add_argument('file', type=str, help='Check this file (or all files in this folder)')
    output_formats = query.add_mutually_exclusive_group(required=True)
    output_formats.add_argument('-t', '--table', default=True, action='store_true',
                                help='Print output in tabular format')
    output_formats.add_argument('-j', '--json', action='store_true', help='Print output in json format')
    query.set_defaults(func=check_for_plagiarism)

    index = commands.add_parser('index', help='Make index')
    index.add_argument('index', type=str, help='Index this directory')
    index.set_defaults(func=gen_index)

    args = parser.parse_args()
    args.func(args)


main()
