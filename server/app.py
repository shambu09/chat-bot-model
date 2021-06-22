import numpy as np
from log import Logger
Logger.clear()
log = Logger.log

from flask import Flask, request
app = Flask(__name__)

from model import load_model, find_similiar
from utils import read_ans, read_qs, write_ans, write_qs


#-------------Load Data--------------#
QS_S = read_qs()
ANS_S = read_ans()

sBert = load_model()
t_embeddings = np.load("db.npy")
#------------------------------------#


def reload_db():
    global QS_S
    global ANS_S
    global t_embeddings

    QS_S = read_qs()
    ANS_S = read_ans()

    t_embeddings = sBert.encode(QS_S)
    np.save("db", t_embeddings)


#-------------------Reply with most similiar answer-----------------------#
@app.route('/',methods = ['POST'])
def answer():
        data = request.args
        qs = data["qs"]
        u_embedding = sBert.encode(qs)
        labels, similarity = find_similiar(qs, u_embedding, t_embeddings)
        
        if similarity > 0.2:
            return ANS_S[labels]

        return "Sorry I didn't get you!"


#------------------Add Question-Answer pairs-------------------------------#
@app.route('/add',methods = ['POST'])
def add():
    global QS_S
    global ANS_S

    data = request.args
    qs = str(data["qs"])
    ans = str(data["ans"])
    
    log("Question added to dataBase - " + qs)
    log("Answer added: "+ ans)

    QS_S.append(qs)
    ANS_S.append(ans)
    write_ans(ANS_S)
    write_qs(QS_S)

    reload_db()
    return "Add OK"

if __name__ == '__main__':
    app.run()