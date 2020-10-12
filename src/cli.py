import argparse

_parser = argparse.ArgumentParser(description='Check for plagiarism in your documents')
_commands = _parser.add_subparsers(required=True)

_query = _commands.add_parser('query', help='Check file for plagiarism')
_query.add_argument('file', type=str, help='Check this file (or all files in this folder)')
_output_formats = _query.add_mutually_exclusive_group(required=True)
_output_formats.add_argument('-t', '--table', default=True, action='store_true', help='Print output in tabular format')
_output_formats.add_argument('-j', '--json', action='store_true', help='Print output in json format')

_index = _commands.add_parser('index', help='Make index')
_index.add_argument('index', type=str, help='Index this directory')

"""
<script> [-h] (query FILE [-j | -t] | index INDEX)
file  => FILE -> (file | folder containing files) that need to checked for plagiarism
index => INDEX -> folder with the files that will constitute the corpus
"""
PARSER = _parser
