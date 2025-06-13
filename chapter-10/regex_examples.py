#!/usr/bin/env python3
import re

text = "The quick brown fox jumped over the lazy dog. \
        The fox could jump 10+ yards"

# print(re.search("fox",text))
# print(re.search("jump",text))
# print(re.search("\+",text))
# print(re.search("\d",text))
# print(re.search("\D",text))
# print(re.search("[jq]\w",text))
# print(re.search("[a-z]{4}",text))
# print(re.search("f.x",text))
# print(re.search("^The",text))

# print(re.match("The",text))


# print(re.match("\d","123abc"))
# print(re.match("\d","abc123"))


# print(re.search("a*bc","aaaaaabc"))
# print(re.search("a+bc","aaaaaabc"))
# print(re.search("a{2,4}bc","aaaaaabc"))


# list_of_foxes = re.findall("fox",text)
# print(list_of_foxes)


# match = re.search("\d+","Hello world 1234")
# print(match.group())


# match = re.search("Name: \w+, Age: \d+","Name: John, Age: 20")
# print(match.group())


# words = re.findall("[qf]\w+",text)
# print(words)

# words = re.findall(r"\b(\w{3})\b",text)
# print(words)


new_text = re.sub(r"fox","cat",text)
print(new_text)

new_text = re.sub(r"\d+","X",text)
print(new_text)


text = "I have 2 laptops and 3 phones"


def double(match):
    return str(int(match.group(0))*2)

doubles_text = re.sub(r"\d+",double,text)
print(doubles_text)