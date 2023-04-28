import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

def assign_semantic_labels(text):
    doc = nlp(text)
    triplets = []
    
    for token in doc:
        if token.dep_ in ("ROOT", "nsubj", "dobj"):
            triplet = (token.text, token.dep_, token.head.text)
            triplets.append(triplet)
            
    # Implement your custom logic for Halliday's semantic labels assignment here
    # For example, you can use rule-based methods or train a machine learning model
    semantic_labels = ["Label 1", "Label 2", "Label 3"]

    return triplets, semantic_labels

input_text = "The cat chases the dog."
triplets, labels = assign_semantic_labels(input_text)
print("Triplets:", triplets)
print("Semantic Labels:", labels)
