import spacy
from preprocess_text import text

# Load the pre-trained model
nlp = spacy.load("en_core_web_lg")

# Process the preprocessed text
doc = nlp(text)

# Extract entities
for ent in doc.ents:
    print(ent.text, ent.label_)