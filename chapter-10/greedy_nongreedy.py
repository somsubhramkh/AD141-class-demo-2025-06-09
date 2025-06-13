#!/usr/bin/env python3

import re

text = "<p>This is the first paragraph.</p><p>This is another paragraph</p>"

match = re.findall(r"<.*>",text)
print(match)


match = re.findall(r"<.*?>",text)
print(match)