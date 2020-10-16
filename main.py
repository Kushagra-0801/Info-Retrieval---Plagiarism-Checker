import json
import pickle
from pathlib import Path

from check import PlagiarismChecker
from cli import PARSER
from make_index import Index
from tabulate import tabulate

THRESHOLD = 0.6


def gen_index(path: Path) -> Index:
    index = Index()
    for file in path.iterdir():
        if not file.is_file():
            continue
        contents = file.read_text()
        index.add_doc(file, contents)
    return index


def main():
    args = PARSER.parse_args()

    if args.index:
        p = Path(args.index)
        if not p.is_dir():
            print("Index path must be a directory containing the corpus files")
            exit(1)
        index = gen_index(p)
        with open('index.pk', 'wb+') as f:
            pickle.dump(index, f)
    else:
        contents = {}
        if args.file == '-':
            from sys import stdin
            contents['stdin'] = stdin.read()
        else:
            p = Path(args.file)
            if p.is_file():
                contents[p] = p.read_text()
            elif p.is_dir():
                for file in p.iterdir():
                    if not file.is_file():
                        continue
                    contents[file] = file.read_text()
        with open('index.pk', 'rb') as f:
            index = pickle.load(f)
        checker = PlagiarismChecker(index)
        data = {}
        for file, contents in contents.items():
            scores = checker.find_score(contents)
            data[file] = sorted([(original, score) for original, score in scores.items() if score > THRESHOLD],
                                reverse=True, key=lambda x: x[1])
        if args.table:
            tabulate(data)
        elif args.json:
            print(json.dumps(data))


main()
