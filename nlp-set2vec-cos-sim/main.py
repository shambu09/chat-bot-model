import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


from data import training_qs, answers, user_qs, user_answers

tokenized_sent = []
for s in training_qs:
    tokenized_sent.append(word_tokenize(s.lower()))

def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))


tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(tokenized_sent)]
model = Doc2Vec(tagged_data, vector_size = 20, window = 2, min_count = 1, epochs = 100)

for k, s in enumerate(user_qs):
    test_doc = word_tokenize(s.lower())
    test_doc_vector = model.infer_vector(test_doc)
    i = model.docvecs.most_similar(positive = [test_doc_vector])[0][0]
    print(f"\n\nuser question : {s}\nmatched training question : {training_qs[i]}\npredicted answer : {answers[i]}\nreal answer : {user_answers[k]}")
