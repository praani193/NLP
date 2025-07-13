import spacy

nlp = spacy.load("en_core_web_sm")

text = "I spent $20 on lunch on January 5, 2023."

doc = nlp(text)

for ent in doc.ents:
    if ent.label_ in ["DATE", "MONEY"]:
        print(f"{ent.text}: {ent.label_}")
