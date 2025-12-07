import re
from collections import defaultdict

def popular_words(text, words):
    text = text.lower()
    text_words = re.findall(r'\w+', text)
    counts = defaultdict(int)

    for word in text_words:
        counts[word] += 1
    return {w: counts[w] for w in words}

