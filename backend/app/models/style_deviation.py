import spacy
nlp = spacy.load("en_core_web_sm")

def style_score(text):
    doc = nlp(text)
    sent_lens = [len(sent) for sent in doc.sents]
    passive = sum(1 for t in doc if t.dep_ == "auxpass")
    return (sum(sent_lens)/max(len(sent_lens),1)) + passive
