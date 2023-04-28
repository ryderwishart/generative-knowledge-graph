import spacy

nlp = spacy.load("en_core_web_sm")


def preprocess(text):
    doc = nlp(text)
    tokenized_text = [token.text for token in doc]
    pos_tags = [token.pos_ for token in doc]
    dependency_parse = [(token.text, token.dep_, token.head.text)
                        for token in doc]

    return tokenized_text, pos_tags, dependency_parse


input_text = "This is a sample text for preprocessing."
tokens, pos, dependencies = preprocess(input_text)
print("Tokens:", tokens)
print("POS tags:", pos)
print("Dependency parse:", dependencies)
