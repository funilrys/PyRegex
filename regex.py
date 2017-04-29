#!/usr/bin/env python

from re import compile, search


class Regex(object):
    """A simple implementation ot the python.re library"""

    def __init__(self, data, regex, return_data=True, group=0):
        super(Regex, self).__init__()
        self.data = data
        self.regex = regex
        self.return_data = return_data
        self.group = group

    def match(self):
        """Used to get exploitable result of re.search"""

        toMatch = compile(self.regex)
        result = toMatch.search(self.data)

        if self.return_data and result is not None:
            return result.group(self.group).strip()
        elif self.return_data == False and result is not None:
            return True
        else:
            return False
