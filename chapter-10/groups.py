#!/usr/bin/env python3

import re

text = "banana, apple, blueberries"

# match = re.search("(ana)+",text)
# print(match)
# print(match.groups())
# print(match.group(0))


# match = re.search("(apple|banana)+([.,;])",text)
# print(match)
# print(match.groups())
# print(match.group(0))
# print(match.group(1))


# text = "This is a string of text"

# match = re.search("((.*) (.*)) (.*)", text)
# print(match.groups())
# print(match.group(0))
# print(match.group(1))
# print(match.group(2))
# print(match.group(3))
# print(match.group(4))


text = "The website, www.redhat.com, contains all our open-source products"

match = re.search("www\.(.+)\.(com|gov|org)", text)
print(match.groups())
print(match.group(0))
print(match.group(1))
print(match.group(2))


