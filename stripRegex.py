import re


def strip(string, x = None):
    whitespace = ""

    if not x:
        left = re.compile(r'^\s*')
        right = re.compile(r'\s*$')
        string = re.sub(left, "", string)
        string = re.sub(right, "", string)
    else:
        strip_char = re.compile(x)
        string = re.sub(strip_char, "", string)
    return string


print(strip("test ", "t"))
print(strip("    test    "))
