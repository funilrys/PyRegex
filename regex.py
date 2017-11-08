#!/usr/bin/env python

# python-regex - A simple implementation ot the python.re package
# Copyright (c) 2017 Funilrys - Nissar Chababy <contact at funilrys dot com>
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Original Version: https://github.com/funilrys/python-regex

"""
A simple implementation ot the python.re package.
"""

from re import compile as comp
from re import sub as substrings


class Regex(object):  # pylint: disable=too-few-public-methods

    """A simple implementation ot the python.re package


    :param data: A string, the data to regex check
    :param regex: A string, the regex to match
    :param return_data: A boolean, if True, return the matched string
    :param group: A integer, the group to return
    :param rematch: A boolean, if True, return the matched groups into a
        formated list. (implementation of Bash ${BASH_REMATCH})
    :param replace_with: A string, the value to replace the matched regex with.
    :param occurences: A int, the number of occurence to replace.
    """

    def __init__(self, data, regex, **args):
        super(Regex, self).__init__()

        # We initiate the needed variable in order to be usable all over class
        self.data = data
        self.regex = regex

        # We assign the default value of our optional arguments
        optional_arguments = {
            "return_data": True,
            "group": 0,
            "rematch": False,
            "replace_with": None,
            "occurences": 0
        }

        # We initiate our optional_arguments in order to be usable all over the
        # class
        for (arg, default) in optional_arguments.items():
            setattr(self, arg, args.get(arg, default))

    def match(self):
        """Used to get exploitable result of re.search"""

        # We initate this variable which gonna contain the returned data
        result = []

        # We compile the regex string
        to_match = comp(self.regex)

        # In case we have to use the implementation of ${BASH_REMATCH} we use
        # re.findall otherwise, we use re.search
        if self.rematch:  # pylint: disable=no-member
            pre_result = to_match.findall(self.data)
        else:
            pre_result = to_match.search(self.data)

        if self.return_data and pre_result is not None:  # pylint: disable=no-member
            if self.rematch:  # pylint: disable=no-member
                for data in pre_result:
                    if isinstance(data, tuple):
                        result.extend(list(data))
                    else:
                        result.append(data)

                if self.group != 0:  # pylint: disable=no-member
                    return result[self.group]  # pylint: disable=no-member
            else:
                result = pre_result.group(
                    self.group).strip()  # pylint: disable=no-member

            return result
        elif not self.return_data and pre_result is not None:  # pylint: disable=no-member
            return True
        return False

    def replace(self):
        """Used to replace a matched string with another."""

        if self.replace_with is not None:  # pylint: disable=no-member
            return substrings(
                self.regex,
                self.replace_with,  # pylint: disable=no-member
                self.data,
                self.occurences)  # pylint: disable=no-member
        return self.data
