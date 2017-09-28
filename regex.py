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

from re import compile, search


class Regex(object):

    """A simple implementation ot the python.re package


    :param data: A string, the data to regex check
    :param regex: A string, the regex to match
    :param return_data: A string, if true, return the matched string
    :param group: A integer, the group to return
    """

    def __init__(self, data, regex, return_data=True, group=0):
        super(Regex, self).__init__()

        self.data = data
        self.regex = regex
        self.return_data = return_data
        self.group = group

    def match(self):
        """Used to get exploitable result of re.search"""

        to_match = compile(self.regex)
        result = to_match.search(self.data)

        if self.return_data and result is not None:
            return result.group(self.group).strip()
        elif self.return_data == False and result is not None:
            return True
        return False
