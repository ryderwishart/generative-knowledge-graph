import spacy
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")
coref_resolution = pipeline("coreference-resolution")


def resolve_coreferences(text):
    result = coref_resolution(text)
    return result["coref_resolved"]


input_text = "John is a software engineer. He works at Google."
resolved_text = resolve_coreferences(input_text)
print("Resolved text:", resolved_text)
