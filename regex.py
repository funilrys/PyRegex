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

from re import compile, findall, search


class Regex(object):

    """A simple implementation ot the python.re package


    :param data: A string, the data to regex check
    :param regex: A string, the regex to match
    :param return_data: A boolean, if True, return the matched string
    :param group: A integer, the group to return
    :param rematch: A boolean, if True, return the matched groups into a formated list. (implementation of Bash ${BASH_REMATCH})
    """

    def __init__(self, data, regex, **args):
        super(Regex, self).__init__()

        self.data = data
        self.regex = regex

        optional_arguments = {
            "return_data": True,
            "group": 0,
            "rematch": False
        }

        for (arg, default) in optional_arguments.items():
            setattr(self, arg, args.get(arg, default))

    def match(self):
        """Used to get exploitable result of re.search"""

        result = []
        to_match = compile(self.regex)

        if self.rematch == False:
            pre_result = to_match.search(self.data)
        else:
            pre_result = to_match.findall(self.data)

        if self.return_data and result is not None:
            if self.rematch:
                for data in pre_result:
                    if isinstance(data,tuple):
                        result.extend(list(data))
                    else:
                        result.append(data)

                if self.group != 0:
                    return result[self.group]
            else:
                result = pre_result.group(self.group).strip()

            return result
        elif self.return_data == False and result is not None:
            return True
        return False
