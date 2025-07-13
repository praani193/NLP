import spacy
nlp = spacy.load("en_core_web_sm")

text = "Bill Gates founded Microsoft in 1975."
doc = nlp(text)
for ent in doc.ents:
    print(f"{ent.text}: {ent.label_}")
