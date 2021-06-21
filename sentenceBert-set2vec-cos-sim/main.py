import argparse
import numpy as np
from log import Logger
from sentence_transformers import SentenceTransformer
from data import training_qs, answers, user_qs, user_answers

Logger.clear()
log = Logger.log
sBert = SentenceTransformer('models/bert-base-nli-mean-tokens')
t_embeddings = sBert.encode(training_qs)


def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))


def answer(qs):
    u_embedding = sBert.encode(qs)
    cosine_matrix = cosine(t_embeddings, u_embedding.T)
    labels = np.argmax(cosine_matrix, axis=0)
    labels = np.squeeze(labels)
    log(f"\ncosine matrix : {cosine_matrix}\nlabel : {labels} - {cosine_matrix[labels]}")

    if not isinstance(qs, list):
        if cosine_matrix[labels] > 0.3:
            return f"Bot : {answers[labels]}\n(matched training question : '{training_qs[labels]}')\n\n"
        else:
            return "I didn't get you\n\n"
    else:
        for i in range(labels.shape[0]):
            print(
                f"User: {qs[i]}\nBot : {answers[labels[0]]}\nmatched training question : '{training_qs[labels[0]]}'\n\n"
            )


#-------------------------------------------------#
parser = argparse.ArgumentParser("Bot Mode")
parser.add_argument("-i",
                    "--interactive",
                    action="store_true",
                    help="Interactive Mode")
args = parser.parse_args()
#-------------------------------------------------#

if args.interactive:
    print("\nEnter a Question:\nPress q to quit\n")
    while (True):
        qs = str(input("User: "))
        if qs == "q":
            break
        print(answer(qs))

else:
    u_embeddings = sBert.encode(user_qs)

    cosine_matrix = cosine(t_embeddings, u_embeddings.T)
    log(f"\n{cosine_matrix}")

    labels = np.argmax(cosine_matrix, axis=0)

    for i in range(labels.shape[0]):
        log(f"\n{labels[i]}\n")
        print(
            f"user question : {user_qs[i]}\nmatched training question : {training_qs[labels[i]]}\npredicted answer : {answers[labels[i]]}\nreal answer : {user_answers[i]}\n\n"
        )