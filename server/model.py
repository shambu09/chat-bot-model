import numpy as np
from log import Logger
from sentence_transformers import SentenceTransformer

Logger.clear()
log = Logger.log

def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

@Logger.wrap
def load_model():
    log("loaded model")
    sBert = SentenceTransformer('/home/shambu/Desktop/Dev/py/chat-bot/sentenceBert-set2vec-cos-sim/models/bert-base-nli-mean-tokens')
    t_embeddings = np.load("db.npy")
    return sBert, t_embeddings

@Logger.wrap
def find_similiar(qs, sBert, t_embeddings):
    u_embedding = sBert.encode(qs)
    cosine_matrix = cosine(t_embeddings, u_embedding.T)
    labels = np.argmax(cosine_matrix, axis=0)
    labels = np.squeeze(labels)
    return labels