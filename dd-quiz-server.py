from flask import Flask,jsonify, render_template, request, Response, json, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import flash
import os
# import numpy as np
import random


app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)

dbuser=str(os.environ.get('dbuser'))
dbpass=str(os.environ.get('dbpass'))

#AWS RDS
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + dbuser + ':' + dbpass + '@jacktestdb.c3bw7kcbozbg.ap-northeast-1.rds.amazonaws.com/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/samplejson",methods=['GET','POST'])
#@tracer.wrap()•
def getSampleJson():
    retVal={
        'key1': 1,
        'key2': "Value2",
        'key3': [{
            'key31':"Value31",
            'key32':"Value32"
        },{
            'key31':"Value311",
            'key32':"value322"
        }]
    }
    return retVal

@app.route("/quiz",methods=['POST'])
def getAllQuiz():
    reqData=request.get_json()
    count=reqData["num"]
    maxNum=4
    # quizNumList=np.random.randint(1,maxNum+1,size=count)
    quizNumList=random.sample(range(1,maxNum+1),count)
    quizList=[]
    for i in quizNumList:
        print ("i in quizNumList is " + str(i))
        quizList.append(getQuiz(i))
    #for test
    # for i in range(len(quizList)):
    #     print(quizList[i]['id'])

    return json.dumps(quizList)

def getRandomNum(count):
    retList=[]
    for i in range(count):
        retList.append()


def getQuiz(quizid):
    db=SQLAlchemy(app)
    Quiz=db.session.execute('select * from quiztable where id=' + str(quizid) ).fetchall()
    quizJson={"id":Quiz[0]['id'],'question':Quiz[0]['question'],'answers':Quiz[0]['answers'],'right':Quiz[0]['right'],'category':Quiz[0]['category']}

    return quizJson

if __name__ == "__main__":
  port = int(os.getenv("PORT", 8080))
  app.run(host="0.0.0.0",port=port)