# Steps: tokenize → remove stopwords → lemmatize → keep only verbs & nouns
import spacy

# load English pipeline
nlp = spacy.load("en_core_web_sm")

text = "John enjoys playing football while Mary loves reading books in the library."

doc = nlp(text)

# keep only alphabetic tokens, not stopwords, and POS in {NOUN, PROPN, VERB}
keep_pos = {"NOUN", "PROPN", "VERB"}
filtered_lemmas = [
    tok.lemma_
    for tok in doc
    if tok.is_alpha and (not tok.is_stop) and tok.pos_ in keep_pos
]

print("Filtered lemmas (verbs & nouns only):", filtered_lemmas)
print("As text:", " ".join(filtered_lemmas))
