"""


Link: https://github.com/pyexcel/pyexcel-ods

Usage
"""

import os
import sys

if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import BytesIO as StringIO
PY2 = sys.version_info[0] == 2
if PY2 and sys.version_info[1] < 7:
    from ordereddict import OrderedDict
else:
    from collections import OrderedDict

from pyexcel_ods3 import save_data

# set demo path_file
path_file = r'data/fileIO_pyexcel_01.xlsx'

# write to an `ods` file
data = OrderedDict()
data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})
data.update({"Sheet 2": [["row 1", "row 2", "row 3"]]})
save_data(path_file, data)

# read from an `ods` file
from pyexcel_ods3 import get_data

rdata = get_data(path_file)

print('\nprint(rdata)')
print(rdata)

print('\nfrom pprint import PrettyPrinter')
from pprint import PrettyPrinter
print('PrettyPrinter(sort_dicts=False).pprint(rdata)')
PrettyPrinter(sort_dicts=False).pprint(rdata)

print('\nimport json')
import json
print('print(json.dumps(rdata))')
print(json.dumps(rdata))

print('\nimport pprint')
import pprint
print('pprint.pprint(json.dumps(rdata)))')
pprint.pprint(json.dumps(rdata))
