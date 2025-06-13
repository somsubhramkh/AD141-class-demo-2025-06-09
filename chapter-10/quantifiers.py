#!/usr/bin/env python3

import re

text = "color colour co coo cooo c o"

# match = re.findall(r"co*",text)
# print(match)


# match = re.findall(r"colo*r",text)
# print(match)

# match = re.findall(r"colou?r",text)
# print(match)


# match = re.findall(r"co{,3}",text)
# print(match)

match = re.findall(r"co{1,3}",text)
print(match)