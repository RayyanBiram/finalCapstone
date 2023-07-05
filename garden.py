import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define the garden path sentences
gardenpathSentences = [
    "The old man the boats.",
    "The horse raced past the barn fell.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Tokenize and perform named entity recognition for each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    for token in doc:
        print("Token:", token.text, "\tNER:", token.ent_type_, "\tNER explanation:", spacy.explain(token.ent_type_))
    print("---")

# Entities looked up:
# 1. The entity category CARDINAL represents numeric values that denote quantities, including numbers, numerals, and counts.
# 2. The entity category GPE represents geopolitical entities such as countries, cities, states, and provinces.

