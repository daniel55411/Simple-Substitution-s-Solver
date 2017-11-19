from optparse import OptionParser
import sys


class options_parser:
    def __init__(self):
        self.parser = OptionParser("""
Encoder and decoder for English and Russian languages

python3 %prog [options] file|input-stream

""")
        self.parser.add_option(
            '-l', '--language',
            type='string',
            default='en',
            action='store',
            help='language for de/encryption'
        )

        self.parser.add_option(
            '--in',
            dest='input',
            type='string',
            action='store',
            help='input file',
        )

        self.parser.add_option(
            '--out',
            dest='output',
            type='string',
            action='store',
            help='output file'
        )

        self.parser.add_option(
            '-m', '--mode',
            type='choice',
            action='store',
            help='to encrypt/ decrypt ["enc", "dec"]',
            choices=['enc', 'dec'],
            default='enc'
        )

        self.parser.add_option(
            '-e', '--encoding',
            type='string',
            action='store',
            help='encoding for input/output file',
            default='utf-8'
        )

    def parse_opt(self):
        options, args = self.parser.parse_args()
        options.input = open(options.input,
                             'r',
                             encoding=options.encoding) if options.input is not None else sys.stdin
        options.output = open(
            options.output,
            'w',
            encoding=options.encoding) if options.output is not None else sys.stdout
        return options
