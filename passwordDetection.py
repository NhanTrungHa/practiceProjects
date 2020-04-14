# check length
# check if contains upper and lower
# check if it contains a digit

import re


def passwordDetection(password):
    length = re.compile(r'([a-zA-Z0-9]{8,})')
    upper = re.compile(r'[A-Z]+')
    lower = re.compile(r'[a-z]+')
    containsDigit = re.compile(r'([0-9]+)')

    if re.search(length, password):
        pass
    else:
        print("unsafe")
        return False

    if re.search(upper, password):
        pass
    else:
        print("unsafe")
        return False

    if re.search(lower, password):
        pass
    else:
        print("unsafe")
        return False

    if re.search(containsDigit, password):
        print("Password is safe")
    else:
        print("unsafe")
        return False


passwordDetection("ABCDEFGHIJKLMAO1232121abxcasdas")
passwordDetection("testing123")
passwordDetection("ABasds1")


