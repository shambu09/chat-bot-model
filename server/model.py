import numpy as np
from log import Logger
from sentence_transformers import SentenceTransformer

log = Logger.log

def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

@Logger.wrap
def load_model():
    log("loaded model")
    sBert = SentenceTransformer('/home/shambu/Desktop/Dev/py/chat-bot/sentenceBert-set2vec-cos-sim/models/bert-base-nli-mean-tokens')
    return sBert

@Logger.wrap
def find_similiar(qs, u_embedding, t_embeddings):
    log(f'"{qs}"')
    cosine_matrix = cosine(t_embeddings, u_embedding.T)
    labels = np.argmax(cosine_matrix, axis=0)
    labels = np.squeeze(labels)
    return labels, cosine_matrix[labels]

if __name__ == '__main__':
   Logger.clear()