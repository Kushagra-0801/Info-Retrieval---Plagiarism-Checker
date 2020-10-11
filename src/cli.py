import argparse

_parser = argparse.ArgumentParser(description='Check for plagiarism in your documents')
_group = _parser.add_mutually_exclusive_group(required=True)
_group.add_argument('-f', '--file', type=str, help='Open the given file and check for plagiarism')
_group.add_argument('-i', '--index', type=str, help='Index the given directory for use as corpus')

"""
<script> [-h] (-f FILE | -i INDEX)
file  => FILE -> (file | folder containing files) that need to checked for plagiarism
index => INDEX -> folder with the files that will constitute the corpus
"""
PARSER = _parser
