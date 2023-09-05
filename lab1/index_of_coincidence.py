import re

def index_of_coincidence(text):

    # Remove all non-alphabetic characters
    text = re.sub(r'[^A-Za-z]', '', text)

    # Calculate the index of coincidence
    n = len(text)
    if n == 0:
        return 0
    return sum([text.count(c) * (text.count(c) - 1) for c in set(text)]) / (n * (n - 1))
