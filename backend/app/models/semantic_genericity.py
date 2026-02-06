GENERIC_TERMS = ["ensure", "appropriate", "applicable", "as required"]

def genericity_score(text):
    return sum(text.lower().count(t) for t in GENERIC_TERMS) / max(len(text.split()),1)
