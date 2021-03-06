import sys


class OverWriter:
    def __init__(self, output=sys.stderr):
        self.length = 0
        self.output = output

    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.close()

    def print(self, print_string):
        self.length = max(self.length, len(print_string))
        print('\r' + print_string.ljust(self.length), end='', file=self.output, flush=True)

    @staticmethod
    def close():
        print('\n')
