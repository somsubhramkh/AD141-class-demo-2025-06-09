#!/usr/bin/env python3

import re

text = "The quick brown fox jumped over the lazy dog. The fox can jump 10+ yards"

match = re.search("[\w]{3,5}",text)
print(match)


# match = re.search("[\s]",text)
# print(match)

# match = re.search("[\d]{2}",text)
# print(match)

# match = re.search("[^\w ]",text)
# print(match)