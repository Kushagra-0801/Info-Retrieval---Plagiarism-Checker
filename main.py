import pickle
from pathlib import Path

from cli import PARSER
from make_index import Index


def gen_index(path: Path) -> Index:
    index = Index()
    for file in path.iterdir():
        if not file.is_file():
            continue
        with open(file) as f:
            contents = f.read()
            index.add_doc(file, contents)
    return index


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
    # TODO: Write the case with the query
    # 3 cases
    # 1. stdin
    # 2. Single file
    # 3. Directory of files
    pass
