# Info Retrieval - Plagiarism Checker

Checks documents for plagiarism with respect to a corpus. The Algorithm used for the same is [Bag of Words](https://en.wikipedia.org/wiki/Bag-of-words_model) 
along with [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity) for score calculation.

## Installation
### Requirements

- [Python 3.8+](https://www.python.org/)
- [Natural Language ToolKit](https://www.nltk.org/)
- [NLTK Popular Model Collection](http://www.nltk.org/nltk_data/)
- [Source Code](https://github.com/Kushagra-0801/Info-Retrieval---Plagiarism-Checker.git)

Note: Source Code can be `git clone`ed if not already present.

## Usage

- $ `cd "Path/to/cloned/repo"`
- $ `python main.py -h`

### Indexing

- Make a folder with only the files that are meant to be included in the corpus
- $ `python main.py index "path/to/folder/made/above"`
- Index can be updated by running the same command with updated corpus folder.

### Querying

- Make sure the index has been previously made
#### Stdin
- $ `python main.py query -`
- Type in the query document in the terminal now
#### Single File
- $ `python main.py query "path/to/file"`
#### Multiple Files
- $ `python main.py query "path/to/file1" "path/to/file2"`

## Documentation
- Make sure you have the `docs/build` folder.
- Open `docs/build/index.html` in your browser.
