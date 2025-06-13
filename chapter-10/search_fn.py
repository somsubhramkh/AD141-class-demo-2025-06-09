#!/usr/bin/env python3

import re

text = "The quick brown fox jumped over the lazy dog. The fox can jump 10+ yards"

match = re.search("fox",text)
print(match)
print(match.start())
print(match.end())

not_a_match = re.search("\+",text)
print(not_a_match)
# print(not_a_match.start())
# print(not_a_match.end())

