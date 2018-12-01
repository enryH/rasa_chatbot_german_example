import spacy

nlp_de = spacy.load("de")

fahrrad = nlp_de(" fahrrad ")
fahrrad.vector
fahrrad_versicherung = nlp_de("Fahrradversicherung")

fahrrad.similarity(fahrrad_versicherung)


hund = nlp_de("Mein Fahrrad ist schön.")
hund.vector

diebstahl = nlp_de("Diebstahl")
diebstahl.vector

fahrrad = nlp_de("Fahrrad")
fahrrad.vector

gestohlen = nlp_de("gestohlen")
gestohlen.vector

auto = nlp_de("Auto")
auto.vector

words = ["Fahrrad", 
         "Diebstahl", "gestohlen", 
         "Auto", "Auto Fahrrad", "Auto gestohlen",
         ]

new_words = ["Haus", "Feuer", "Einbruch", "Motorrad", "Schaden", "Reiseversicherung", "Reise"]

def word_vector(nlp, _str):
    print(nlp(_str).vector)
    return None

for word in new_words:
    print(word)
    word_vector(nlp_de, word)
    print("\n\n")


satz = nlp_de('Ich muss einen Fahrraddiebstahl mitteilen.')
for token in satz:
    print(token)

satz = nlp_de("Ich hatte einen Autounfall heute.")
for token in satz:
    print(token)


import spacy

nlp_de = spacy.load("de")


paragraph = "Ich hatte einen Unfall mit meinem Auto."
paragraph = "Ich hatte einen AutoUnfall an einen stürmischen Tag."
satz = nlp_de(paragraph)
for token in satz:
    print( "token.text: {:>6}\ttoken.idx: {}".format(token.text, token.idx))


# pip install SoMaJo
from somajo import Tokenizer, SentenceSplitter
tokenizer = Tokenizer(split_camel_case=True, token_classes=False, extra_info=False)

paragraph = "Ich hatte einen AutoUnfall an einen stürmischen Tag."
tokens = tokenizer.tokenize(paragraph)

def get_indices(tokens, paragraph):
    index = 0
    startindices = []
    for token in tokens:
        new_index = paragraph.index(token)
        paragraph = paragraph[new_index:]
        index += new_index
        startindices.append(index)
    return zip(tokens, startindices)

for text, idx in get_indices(tokens, paragraph):
    print( "token.text: {:>6}\ttoken.idx: {}".format(text, idx))

# note that paragraphs are allowed to contain newlines
paragraph = "Ich hatte einen Autounfall an einen stürmischen Tag."
tokens = tokenizer.tokenize(paragraph)
for text, idx in get_indices(tokens, paragraph):
    print( "token.text: {:>11}\ttoken.idx: {}".format(text, idx))



# note that paragraphs are allowed to contain newlines
paragraph = "Ich hatte einen Unfall mit meinem Auto."
tokens = tokenizer.tokenize(paragraph)
for text, idx in get_indices(tokens, paragraph):
    print( "token.text: {:>6}\ttoken.idx: {}".format(text, idx))





print("\n".join(tokens), "\n")
# set is_tuple=True if token_classes=True or extra_info=True
sentence_splitter = SentenceSplitter(is_tuple=False)
sentences = sentence_splitter.split(tokens)

for sentence in sentences:
    print("\n".join(sentence), "\n")



